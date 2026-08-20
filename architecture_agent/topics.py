from __future__ import annotations

from architecture_agent.types import Topic

TOPICS: list[Topic] = [
    Topic(
        id="dependency-inversion",
        name="Dependency Inversion",
        description="High-level policy should not depend directly on low-level details.",
        source_urls=[
            "https://martinfowler.com/articles/injection.html",
            "https://martinfowler.com/bliki/InversionOfControl.html",
            "https://martinfowler.com/tags/application%20architecture.html",
        ],
    ),
    Topic(
        id="information-hiding",
        name="Information Hiding",
        description="Hide volatile details behind stable boundaries.",
        source_urls=[
            "https://www.cs.utexas.edu/users/EWD/transcriptions/EWD04xx/EWD447.html",
            "https://www.sei.cmu.edu/blog/what-is-software-architecture/",
        ],
    ),
    Topic(
        id="staged-context",
        name="Staged Context Construction",
        description="Build AI context in layers to manage token budget and relevance.",
        source_urls=[
            "https://platform.openai.com/docs/guides",
            "https://martinfowler.com/articles/microservice-testing/",
        ],
    ),
]
