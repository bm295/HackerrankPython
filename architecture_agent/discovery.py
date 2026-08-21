from __future__ import annotations

import re
from urllib.parse import urlparse

from architecture_agent.search import SearchProvider
from architecture_agent.types import RepositoryProfile, SearchResult, Topic, TopicCandidate

AUTHORITATIVE_DOMAINS = (".org", ".edu", "docs.", "developer.", "learn.microsoft.com", "aws.amazon.com", "cloud.google.com")
TITLE_SUFFIX_RE = re.compile(
    r"\s+(best practices|patterns|guide|architecture|for\b.*|in\b.*|with\b.*).*$",
    re.IGNORECASE,
)


def build_search_queries(profile: RepositoryProfile, requested_topic: str | None = None) -> list[str]:
    context = " ".join([*profile.languages[:2], *profile.frameworks[:2], *profile.signals[:3]]) or "software repository"
    if requested_topic:
        return [f"{context} {requested_topic} architecture best practices"]
    return [
        f"{context} software architecture best practices",
        f"{context} performance reliability design patterns",
    ]


def discover_topics(
    profile: RepositoryProfile,
    provider: SearchProvider,
    result_limit: int = 8,
    requested_topic: str | None = None,
) -> list[TopicCandidate]:
    queries = build_search_queries(profile, requested_topic)
    grouped: dict[str, list[SearchResult]] = {}
    for query in queries:
        for result in provider.search(query, result_limit):
            name = _topic_from_title(result.title)
            if name:
                grouped.setdefault(_group_key(name), []).append(result)

    candidates: list[TopicCandidate] = []
    signal_text = " ".join(profile.signals).casefold()
    for key, results in grouped.items():
        unique_results = list({result.url: result for result in results}.values())
        urls = [result.url for result in unique_results]
        source_quality = sum(_is_authoritative(url) for url in urls) / len(urls)
        relevance = min(1.0, 0.25 * len(urls) + (0.5 if _matches_signals(key, signal_text) else 0.0))
        topic_name = _topic_from_title(unique_results[0].title) or key.title()
        candidates.append(TopicCandidate(
            topic=Topic(
                id=re.sub(r"[^a-z0-9]+", "-", topic_name.casefold()).strip("-"),
                name=topic_name,
                description=f"Discovered online for repository signals: {', '.join(profile.signals) or 'general architecture'}.",
                source_urls=urls,
            ),
            repository_signals=profile.signals,
            search_queries=queries,
            relevance_score=relevance,
            source_quality_score=source_quality,
        ))
    return sorted(candidates, key=lambda item: (-item.relevance_score, -item.source_quality_score, item.topic.id))


def _is_authoritative(url: str) -> bool:
    host = urlparse(url).hostname or ""
    return any(marker in host for marker in AUTHORITATIVE_DOMAINS)


def _matches_signals(topic: str, signals: str) -> bool:
    topic_stems = {_stem(word) for word in re.findall(r"[a-z]{4,}", topic)}
    signal_stems = {_stem(word) for word in re.findall(r"[a-z]{4,}", signals)}
    return bool(topic_stems & signal_stems)


def _topic_from_title(title: str) -> str:
    segment = re.split(r"\s+[|:–—-]\s+", title, maxsplit=1)[0]
    topic = TITLE_SUFFIX_RE.sub("", segment).strip(" .:—–-")
    words = topic.split()
    if not words or len(words) > 8:
        return ""
    return topic.title()


def _group_key(topic: str) -> str:
    words = [_stem(word) for word in re.findall(r"[a-z0-9]+", topic.casefold())]
    if words and words[0] == "cach":
        return "caching"
    return "-".join(words)


def _stem(word: str) -> str:
    if word.casefold().startswith("cach"):
        return "cach"
    return re.sub(r"(ing|tion|s|ed)$", "", word.casefold())
