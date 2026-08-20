from __future__ import annotations

import unittest

from architecture_agent.selector import select_topic
from architecture_agent.topics import TOPICS


class SelectorTests(unittest.TestCase):
    def test_selection_is_deterministic(self) -> None:
        first = select_topic(TOPICS, 42, lambda _: True)
        second = select_topic(TOPICS, 42, lambda _: True)
        self.assertEqual(first.id, second.id)


if __name__ == "__main__":
    unittest.main()
