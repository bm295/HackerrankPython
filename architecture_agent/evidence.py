from __future__ import annotations

import re

from architecture_agent.types import EvidenceItem, FileRecord, Topic

PATH_RE = re.compile(r"service|repository|provider|scanner|analyzer|config|fetch|client|http|db|sql|route", re.IGNORECASE)


def find_evidence(files: list[FileRecord], topic: Topic) -> list[EvidenceItem]:
    hits = [record for record in files if record.text and PATH_RE.search(record.path)][:8]
    evidence: list[EvidenceItem] = []
    for record in hits:
        if topic.id == "dependency-inversion" and record.text and "new " in record.text:
            note = "Concrete construction indicates direct dependency wiring."
        elif topic.id == "dependency-inversion" and record.text and "subprocess" in record.text:
            note = "Concrete process invocation is embedded directly in the module."
        else:
            note = "Relevant architectural file."
        evidence.append(EvidenceItem(file=record.path, note=note))
    return evidence
