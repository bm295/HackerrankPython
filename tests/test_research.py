from __future__ import annotations

import unittest

from architecture_agent.research import research_topic


class ResearchTests(unittest.TestCase):
    def test_provider_handles_failures(self) -> None:
        result = research_topic(["https://example.invalid"], 1)
        self.assertEqual(len(result), 1)
        self.assertIn("example.invalid", result[0].url)


if __name__ == "__main__":
    unittest.main()
