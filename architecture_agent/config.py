from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(slots=True)
class AppConfig:
    max_files_analyzed: int = 120
    max_file_size: int = 200000
    ignored_dirs: list[str] | None = None
    ignored_patterns: list[str] | None = None
    research_source_count: int = 3
    random_seed: int | None = None
    log_level: str = "info"


def _split_csv(value: str) -> list[str]:
    return [item.strip() for item in value.split(",") if item.strip()]


def load_config(env: dict[str, str] | None = None) -> AppConfig:
    data = env or dict(os.environ)
    return AppConfig(
        max_files_analyzed=int(data.get("MAX_FILES_ANALYZED", "120")),
        max_file_size=int(data.get("MAX_FILE_SIZE", "200000")),
        ignored_dirs=_split_csv(data.get("IGNORED_DIRS", "node_modules,dist,build,coverage,.git,vendor,.angular,.venv,__pycache__")),
        ignored_patterns=_split_csv(data.get("IGNORED_PATTERNS", "*.min.js,*.map")),
        research_source_count=int(data.get("RESEARCH_SOURCE_COUNT", "3")),
        random_seed=int(data["RANDOM_SEED"]) if data.get("RANDOM_SEED") else None,
        log_level=data.get("LOG_LEVEL", "info"),
    )
