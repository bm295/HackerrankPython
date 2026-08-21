from __future__ import annotations

import re

from architecture_agent.types import EvidenceItem, FileRecord, Topic

PATH_RE = re.compile(r"service|repository|provider|scanner|analyzer|config|fetch|client|http|db|sql|route", re.IGNORECASE)
TOPIC_PATTERNS = {
    "caching": re.compile(r"\b(redis|memcached|cache|lru_cache|ttl)\b", re.IGNORECASE),
    "authentication": re.compile(r"\b(jwt|oauth|authentication|authorization)\b", re.IGNORECASE),
    "message queue": re.compile(r"\b(celery|queue|kafka|rabbitmq|worker)\b", re.IGNORECASE),
    "observability": re.compile(r"\b(logging|metrics|tracing|opentelemetry|prometheus)\b", re.IGNORECASE),
}


def find_evidence(files: list[FileRecord], topic: Topic) -> list[EvidenceItem]:
    topic_pattern = next((pattern for name, pattern in TOPIC_PATTERNS.items() if name in topic.name.casefold()), None)
    if topic_pattern:
        hits = [record for record in files if record.text and topic_pattern.search(record.text)][:8]
    else:
        hits = [record for record in files if record.text and PATH_RE.search(record.path)][:8]
    evidence: list[EvidenceItem] = []
    for record in hits:
        if topic.id == "dependency-inversion" and record.text and "new " in record.text:
            note = "Concrete construction indicates direct dependency wiring."
        elif topic.id == "dependency-inversion" and record.text and "subprocess" in record.text:
            note = "Concrete process invocation is embedded directly in the module."
        elif topic_pattern:
            match = topic_pattern.search(record.text or "")
            note = f"Repository signal '{match.group(0)}' supports this topic." if match else "Relevant topic signal."
        else:
            note = "Relevant architectural file."
        evidence.append(EvidenceItem(file=record.path, note=note))
    return evidence
