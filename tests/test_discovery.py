from __future__ import annotations

import unittest

from architecture_agent.discovery import build_search_queries, discover_topics
from architecture_agent.types import RepositoryProfile, SearchResult


class FakeSearchProvider:
    def __init__(self) -> None:
        self.queries: list[str] = []

    def search(self, query: str, limit: int) -> list[SearchResult]:
        self.queries.append(query)
        return [
            SearchResult("Caching best practices for web applications", "https://developer.example.org/caching"),
            SearchResult("Cache invalidation architecture", "https://docs.example.org/cache-invalidation"),
            SearchResult("Unrelated product announcement", "https://example.com/product"),
        ][:limit]


class DiscoveryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.profile = RepositoryProfile(
            languages=["Python"],
            frameworks=["FastAPI"],
            dependencies=["redis"],
            signals=["cache usage", "HTTP API"],
        )

    def test_queries_are_derived_from_repository_profile(self) -> None:
        queries = build_search_queries(self.profile)
        self.assertIn("Python", queries[0])
        self.assertIn("FastAPI", queries[0])
        self.assertIn("cache usage", queries[0])

    def test_online_results_become_ranked_topic_candidates(self) -> None:
        provider = FakeSearchProvider()
        candidates = discover_topics(self.profile, provider)
        self.assertEqual("caching", candidates[0].topic.id)
        self.assertEqual(1.0, candidates[0].relevance_score)
        self.assertTrue(candidates[0].topic.source_urls)
        self.assertEqual(2, len(provider.queries))

    def test_requested_topic_guides_search(self) -> None:
        provider = FakeSearchProvider()
        discover_topics(self.profile, provider, requested_topic="caching")
        self.assertEqual(1, len(provider.queries))
        self.assertIn("caching", provider.queries[0])


if __name__ == "__main__":
    unittest.main()
