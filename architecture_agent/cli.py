from __future__ import annotations

import argparse
import json
from pathlib import Path

from architecture_agent.analyzer import build_profile, build_snapshot
from architecture_agent.config import load_config
from architecture_agent.evidence import find_evidence
from architecture_agent.discovery import discover_topics
from architecture_agent.intake import prepare_repository_input
from architecture_agent.repo_config import load_repo_config
from architecture_agent.report import to_markdown
from architecture_agent.research import research_topic
from architecture_agent.scanner import scan_repository
from architecture_agent.search import DuckDuckGoSearchProvider, SearchProvider
from architecture_agent.selector import select_topic
from architecture_agent.topics import TOPICS
from architecture_agent.types import AnalysisReport, ApplicationPoint, Recommendation


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="architecture-agent")
    subparsers = parser.add_subparsers(dest="command")
    analyze = subparsers.add_parser("analyze")
    analyze.add_argument("repository")
    analyze.add_argument("--seed", type=int)
    analyze.add_argument("--topic")
    analyze.add_argument("--topic-mode", choices=("catalog", "discover", "hybrid"))
    analyze.add_argument("--json", action="store_true", dest="as_json")
    analyze.add_argument("--output")
    return parser


def run_analysis(args: argparse.Namespace, search_provider: SearchProvider | None = None) -> AnalysisReport:
    config = load_config()
    seed = args.seed if args.seed is not None else (config.random_seed or 42)
    prepared = prepare_repository_input(args.repository)
    repo_config = load_repo_config(prepared.root)
    scan = scan_repository(
        prepared.root,
        ignored_dirs=[*(config.ignored_dirs or []), *repo_config.ignored_dirs],
        ignored_patterns=config.ignored_patterns or [],
        max_files_analyzed=config.max_files_analyzed,
        max_file_size=config.max_file_size,
    )
    snapshot = build_snapshot(prepared.root, scan.files, scan.dirs)
    profile = build_profile(scan.files)
    normalized_topic = args.topic.lower() if args.topic else None
    mode = args.topic_mode or config.topic_mode
    if mode not in {"catalog", "discover", "hybrid"}:
        raise ValueError(f"Unsupported topic mode: {mode}")
    candidates = []
    if mode in {"discover", "hybrid"}:
        provider = search_provider or DuckDuckGoSearchProvider(config.search_endpoint, config.search_timeout)
        try:
            candidates = discover_topics(profile, provider, config.search_result_count, normalized_topic)
        except (OSError, TimeoutError):
            if mode == "discover":
                raise RuntimeError("Online topic discovery failed and no catalog fallback was enabled") from None
    if candidates:
        topic = candidates[0].topic
    else:
        matching_topics = [item for item in TOPICS if normalized_topic is None or item.name.lower() == normalized_topic or item.id.lower() == normalized_topic]
        if normalized_topic and not matching_topics:
            raise ValueError(f"No topic named '{args.topic}' was discovered or found in the catalog")
        if mode == "discover":
            raise ValueError("Online search did not discover any architecture topics")
        topic = select_topic(matching_topics or TOPICS, seed, lambda item: bool(item.source_urls))
    research = research_topic(topic.source_urls, config.research_source_count)
    evidence = find_evidence(scan.files, topic)
    confidence = "Medium" if evidence else "Low"
    return AnalysisReport(
        repository=snapshot,
        architecture={
            "style": snapshot.type,
            "buildingBlocks": ["CLI", "Scanner", "Analyzer", "Topic Discovery", "Topic Selector", "Research Provider"],
            "dependencyDirection": "CLI -> services -> filesystem/network",
            "externalDependencies": ["Python runtime"],
        },
        selected_topic=topic,
        research=research,
        evidence=evidence,
        application_point=ApplicationPoint(
            file=evidence[0].file if evidence else "N/A",
            current_design="Direct, concrete dependency or responsibility is embedded in the file.",
            issue="Potentially low flexibility around a selected architecture concern.",
            concept=topic.name,
            proposed_design="Introduce a stable boundary only if the evidence justifies it.",
        ),
        recommendation=Recommendation(
            summary=f"Use {topic.name} as the lens for the next refactoring step, but keep changes minimal and evidence-driven.",
            benefits=["better modifiability", "clearer boundaries", "improved testability"],
            tradeoffs=["more types and indirection", "extra conceptual overhead"],
            confidence=confidence,
        ),
    )


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    if args.command != "analyze":
        parser.print_help()
        raise SystemExit(1)
    report = run_analysis(args)
    output = json.dumps(report.to_dict(), indent=2) if args.as_json else to_markdown(report)
    if args.output:
        Path(args.output).write_text(output, encoding="utf-8")
    else:
        print(output)


if __name__ == "__main__":
    main()
