from __future__ import annotations

from html import unescape
from typing import Protocol
from urllib.parse import parse_qs, quote_plus, unquote, urlparse
from urllib.request import Request, urlopen
import re

from architecture_agent.types import SearchResult


class SearchProvider(Protocol):
    def search(self, query: str, limit: int) -> list[SearchResult]: ...


class DuckDuckGoSearchProvider:
    """Small dependency-free provider for DuckDuckGo's HTML search endpoint."""

    RESULT_RE = re.compile(
        r'<a[^>]+class="[^"]*result__a[^"]*"[^>]+href="([^"]+)"[^>]*>(.*?)</a>',
        re.IGNORECASE | re.DOTALL,
    )
    TAG_RE = re.compile(r"<[^>]+>")

    def __init__(self, endpoint: str, timeout: int = 10) -> None:
        self.endpoint = endpoint
        self.timeout = timeout

    def search(self, query: str, limit: int) -> list[SearchResult]:
        separator = "&" if "?" in self.endpoint else "?"
        request = Request(
            f"{self.endpoint}{separator}q={quote_plus(query)}",
            headers={"User-Agent": "ArchitectureExplorerAgent/1.0"},
        )
        with urlopen(request, timeout=self.timeout) as response:
            page = response.read().decode("utf-8", errors="ignore")
        results: list[SearchResult] = []
        for raw_url, raw_title in self.RESULT_RE.findall(page):
            url = unescape(raw_url)
            redirect_target = parse_qs(urlparse(url).query).get("uddg")
            if redirect_target:
                url = unquote(redirect_target[0])
            title = unescape(self.TAG_RE.sub("", raw_title)).strip()
            if title and url.startswith(("http://", "https://")):
                results.append(SearchResult(title=title, url=url))
            if len(results) >= limit:
                break
        return results
