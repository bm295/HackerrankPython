from __future__ import annotations

import re
from pathlib import PurePosixPath

from architecture_agent.types import FileRecord, RepositorySnapshot

MANIFEST_NAMES = {"package.json", "tsconfig.json", "pyproject.toml", "requirements.txt", "Cargo.toml", "go.mod"}
ENTRYPOINT_RE = re.compile(r"(^|/)(main|cli|index|app)\.(ts|js|py|go|cs|jsx|tsx)$")
EVIDENCE_RE = re.compile(r"service|repository|controller|adapter|provider|agent|scanner|analyzer", re.IGNORECASE)


def build_snapshot(root: str, files: list[FileRecord], dirs: int) -> RepositorySnapshot:
    manifests = [record.path for record in files if PurePosixPath(record.path).name in MANIFEST_NAMES]
    entry_points = [record.path for record in files if ENTRYPOINT_RE.search(record.path)]
    evidence_files = [record.path for record in files if record.text and EVIDENCE_RE.search(record.path)]

    if any(record.path.startswith("architecture_agent/") for record in files):
        repo_type = "Python CLI application"
    elif any(record.path.startswith("src/") for record in files):
        repo_type = "Application with source layout"
    else:
        repo_type = "Unknown"

    return RepositorySnapshot(
        root=root,
        type=repo_type,
        counts={"files": len(files), "dirs": dirs},
        entry_points=entry_points,
        manifests=manifests,
        evidence_files=evidence_files,
    )
