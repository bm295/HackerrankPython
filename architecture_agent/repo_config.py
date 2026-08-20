from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class RepoConfig:
    ignored_dirs: list[str]


def load_repo_config(root: str) -> RepoConfig:
    path = Path(root) / ".architecture-agent.json"
    if not path.exists():
        return RepoConfig(ignored_dirs=[])
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return RepoConfig(ignored_dirs=[])
    ignored_dirs = data.get("ignoredDirs", [])
    if not isinstance(ignored_dirs, list):
        ignored_dirs = []
    return RepoConfig(ignored_dirs=[str(item) for item in ignored_dirs])
