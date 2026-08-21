from __future__ import annotations

import re
from pathlib import PurePosixPath

from architecture_agent.types import FileRecord, RepositoryProfile, RepositorySnapshot

MANIFEST_NAMES = {"package.json", "tsconfig.json", "pyproject.toml", "requirements.txt", "Cargo.toml", "go.mod"}
ENTRYPOINT_RE = re.compile(r"(^|/)(main|cli|index|app)\.(ts|js|py|go|cs|jsx|tsx)$")
EVIDENCE_RE = re.compile(r"service|repository|controller|adapter|provider|agent|scanner|analyzer", re.IGNORECASE)
LANGUAGE_BY_EXTENSION = {
    ".py": "Python", ".js": "JavaScript", ".ts": "TypeScript", ".go": "Go",
    ".rs": "Rust", ".java": "Java", ".cs": "C#",
}
FRAMEWORK_PATTERNS = {
    "Django": r"\bdjango\b", "FastAPI": r"\bfastapi\b", "Flask": r"\bflask\b",
    "React": r"\breact\b", "Express": r"\bexpress\b", "Spring": r"\bspringframework\b",
}
SIGNAL_PATTERNS = {
    "cache usage": r"\b(redis|memcached|cache|lru_cache)\b",
    "database access": r"\b(sqlalchemy|django\.db|select\s+.+\s+from|mongodb|postgres)\b",
    "HTTP API": r"\b(route|endpoint|fastapi|flask|express|controller)\b",
    "external HTTP calls": r"\b(requests\.|httpx\.|urlopen|fetch\()",
    "background processing": r"\b(celery|rq\b|sidekiq|background.?job|queue)\b",
    "authentication": r"\b(jwt|oauth|authentication|authorization)\b",
}


def build_profile(files: list[FileRecord]) -> RepositoryProfile:
    languages = sorted({LANGUAGE_BY_EXTENSION[r.ext.lower()] for r in files if r.ext.lower() in LANGUAGE_BY_EXTENSION})
    searchable = "\n".join(r.text[:50_000] for r in files if r.text)
    frameworks = sorted(name for name, pattern in FRAMEWORK_PATTERNS.items() if re.search(pattern, searchable, re.IGNORECASE))
    signals = sorted(name for name, pattern in SIGNAL_PATTERNS.items() if re.search(pattern, searchable, re.IGNORECASE | re.DOTALL))
    dependencies: set[str] = set()
    for record in files:
        if PurePosixPath(record.path).name not in MANIFEST_NAMES or not record.text:
            continue
        dependencies.update(re.findall(r'(?m)^[\s"\']*([A-Za-z][\w.-]+)["\']?\s*(?:[=<>~^:]|$)', record.text))
    return RepositoryProfile(languages, frameworks, sorted(dependencies)[:30], signals)


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
