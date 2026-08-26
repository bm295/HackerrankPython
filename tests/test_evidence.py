from __future__ import annotations

import unittest

from architecture_explorer_agent.evidence import find_evidence
from architecture_explorer_agent.types import FileRecord, Topic


class EvidenceTests(unittest.TestCase):
    def test_evidence_finder_returns_relevant_files(self) -> None:
        files = [FileRecord(path="architecture_explorer_agent/service.py", size=10, ext=".py", text="subprocess.run(['git'])")]
        topic = Topic(id="dependency-inversion", name="Dependency Inversion", description="", source_urls=[])
        result = find_evidence(files, topic)
        self.assertEqual(len(result), 1)


if __name__ == "__main__":
    unittest.main()
