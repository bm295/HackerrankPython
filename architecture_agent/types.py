from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Literal


@dataclass(slots=True)
class FileRecord:
    path: str
    size: int
    ext: str
    text: str | None = None
    lines: int | None = None


@dataclass(slots=True)
class RepositorySnapshot:
    root: str
    type: str
    counts: dict[str, int]
    entry_points: list[str]
    manifests: list[str]
    evidence_files: list[str]


@dataclass(slots=True)
class Topic:
    id: str
    name: str
    description: str
    source_urls: list[str]


@dataclass(slots=True)
class ResearchSource:
    title: str
    url: str
    reason: str
    excerpt: str | None = None


@dataclass(slots=True)
class EvidenceItem:
    file: str
    note: str


Confidence = Literal["High", "Medium", "Low"]


@dataclass(slots=True)
class ApplicationPoint:
    file: str
    current_design: str
    issue: str
    concept: str
    proposed_design: str


@dataclass(slots=True)
class Recommendation:
    summary: str
    benefits: list[str]
    tradeoffs: list[str]
    confidence: Confidence


@dataclass(slots=True)
class AnalysisReport:
    repository: RepositorySnapshot
    architecture: dict[str, object]
    selected_topic: Topic
    research: list[ResearchSource]
    evidence: list[EvidenceItem]
    application_point: ApplicationPoint
    recommendation: Recommendation

    def to_dict(self) -> dict[str, object]:
        return asdict(self)

