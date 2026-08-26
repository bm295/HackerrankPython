from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from architecture_explorer_agent.repo_config import load_repo_config


class RepoConfigTests(unittest.TestCase):
    def test_load_repo_config_reads_short_name(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / ".architecture-explorer.json"
            path.write_text(json.dumps({"ignoredDirs": ["legacy", "tmp"]}), encoding="utf-8")

            config = load_repo_config(tmpdir)

        self.assertEqual(["legacy", "tmp"], config.ignored_dirs)

    def test_load_repo_config_ignores_missing_file(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            config = load_repo_config(tmpdir)

        self.assertEqual([], config.ignored_dirs)


if __name__ == "__main__":
    unittest.main()
