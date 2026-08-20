from __future__ import annotations

import re
from urllib.error import URLError
from urllib.request import Request, urlopen

from architecture_agent.types import ResearchSource

TITLE_RE = re.compile(r"<title>([^<]+)</title>", re.IGNORECASE)


def research_topic(urls: list[str], count: int = 3) -> list[ResearchSource]:
    results: list[ResearchSource] = []
    for url in urls[:count]:
        request = Request(url, headers={"User-Agent": "ArchitectureExplorerAgent/1.0"})
        try:
            with urlopen(request, timeout=15) as response:
                text = response.read().decode("utf-8", errors="ignore")
            title_match = TITLE_RE.search(text)
            title = title_match.group(1).strip() if title_match else url
            excerpt = " ".join(text.split())[:240]
            results.append(
                ResearchSource(
                    title=title,
                    url=url,
                    reason="Authoritative or canonical reference for the selected topic.",
                    excerpt=excerpt,
                )
            )
        except (URLError, TimeoutError, OSError):
            results.append(
                ResearchSource(
                    title=url,
                    url=url,
                    reason="Source unavailable during this run.",
                )
            )
    return results
