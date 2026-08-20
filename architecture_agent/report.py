from __future__ import annotations

from architecture_agent.types import AnalysisReport


def to_markdown(report: AnalysisReport) -> str:
    lines = [
        "# Architecture Explorer Report",
        "",
        "## Repository Snapshot",
        f"- Root: {report.repository.root}",
        f"- Style: {report.repository.type}",
        f"- Files: {report.repository.counts['files']}",
        "",
        "## Topic",
        f"- {report.selected_topic.name}",
        "",
        "## Evidence",
    ]
    lines.extend(f"- {item.file}: {item.note}" for item in report.evidence)
    lines.extend(
        [
            "",
            "## Recommendation",
            f"- {report.recommendation.summary}",
            f"- Confidence: {report.recommendation.confidence}",
        ]
    )
    return "\n".join(lines)
