from __future__ import annotations

import unittest

from architecture_agent.analyzer import build_profile
from architecture_agent.types import FileRecord


class AnalyzerProfileTests(unittest.TestCase):
    def test_profile_extracts_repository_signals(self) -> None:
        files = [
            FileRecord("pyproject.toml", 20, ".toml", 'redis = "^5"\nfastapi = "^1"'),
            FileRecord("app.py", 30, ".py", "from fastapi import FastAPI\nfrom functools import lru_cache"),
        ]
        profile = build_profile(files)
        self.assertEqual(["Python"], profile.languages)
        self.assertIn("FastAPI", profile.frameworks)
        self.assertIn("cache usage", profile.signals)
        self.assertIn("redis", profile.dependencies)


if __name__ == "__main__":
    unittest.main()
