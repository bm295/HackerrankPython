from __future__ import annotations

import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class PreparedRepository:
    root: str
    cloned: bool


def prepare_repository_input(input_value: str) -> PreparedRepository:
    if input_value.startswith("http://") or input_value.startswith("https://") or input_value.endswith(".git"):
        target_dir = tempfile.mkdtemp(prefix="architecture-agent-")
        subprocess.run(
            ["git", "clone", "--depth", "1", input_value, target_dir],
            check=True,
            capture_output=True,
            text=True,
        )
        return PreparedRepository(root=target_dir, cloned=True)
    return PreparedRepository(root=str(Path(input_value).resolve()), cloned=False)
