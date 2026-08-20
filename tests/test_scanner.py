from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from architecture_agent.scanner import scan_repository


class ScannerTests(unittest.TestCase):
    def test_scanner_ignores_configured_directories(self) -> None:
        with tempfile.TemporaryDirectory(prefix="archscan-") as root:
            base = Path(root)
            (base / "node_modules").mkdir()
            (base / "src").mkdir()
            (base / "src" / "a.py").write_text("value = 1\n", encoding="utf-8")
            (base / "node_modules" / "skip.py").write_text("bad\n", encoding="utf-8")
            result = scan_repository(
                root,
                ignored_dirs=["node_modules"],
                ignored_patterns=[],
                max_files_analyzed=5,
                max_file_size=1000,
            )
            self.assertFalse(any("node_modules" in item.path for item in result.files))
            self.assertTrue(any(item.path.endswith("a.py") for item in result.files))


if __name__ == "__main__":
    unittest.main()
