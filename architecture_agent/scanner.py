from __future__ import annotations

from dataclasses import dataclass
from fnmatch import fnmatch
from pathlib import Path

from architecture_agent.types import FileRecord

TEXT_EXTENSIONS = {
    ".ts",
    ".tsx",
    ".js",
    ".jsx",
    ".json",
    ".md",
    ".yml",
    ".yaml",
    ".toml",
    ".txt",
    ".py",
    ".go",
    ".java",
    ".rs",
    ".cs",
    ".xml",
    ".html",
    ".css",
    ".scss",
}


@dataclass(slots=True)
class ScanResult:
    files: list[FileRecord]
    dirs: int


def _is_text_candidate(path: Path) -> bool:
    return path.suffix.lower() in TEXT_EXTENSIONS or path.name in {"package.json", "tsconfig.json", "README.md", "pyproject.toml"}


def scan_repository(
    root: str,
    *,
    ignored_dirs: list[str],
    ignored_patterns: list[str],
    max_files_analyzed: int,
    max_file_size: int,
) -> ScanResult:
    base = Path(root)
    files: list[FileRecord] = []
    dirs = 0

    def walk(directory: Path) -> None:
        nonlocal dirs
        dirs += 1
        for entry in sorted(directory.iterdir(), key=lambda item: item.name.lower()):
            if entry.name in ignored_dirs:
                continue
            if entry.is_dir():
                walk(entry)
                if len(files) >= max_files_analyzed:
                    return
                continue
            if len(files) >= max_files_analyzed:
                return
            if any(fnmatch(entry.name, pattern) for pattern in ignored_patterns):
                continue
            try:
                size = entry.stat().st_size
            except OSError:
                continue
            if size > max_file_size:
                continue
            relative = entry.relative_to(base).as_posix()
            record = FileRecord(path=relative, size=size, ext=entry.suffix.lower())
            if _is_text_candidate(entry):
                try:
                    text = entry.read_text(encoding="utf-8")
                except UnicodeDecodeError:
                    text = entry.read_text(encoding="utf-8", errors="ignore")
                record.text = text
                record.lines = len(text.splitlines())
            files.append(record)

    walk(base)
    return ScanResult(files=files, dirs=dirs)
