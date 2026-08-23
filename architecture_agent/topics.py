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
    Topic(
        id="separation-of-concerns",
        name="Separation of Concerns",
        description="Keep distinct reasons to change in separate modules or layers.",
        source_urls=[
            "https://www.sei.cmu.edu/blog/what-is-software-architecture/",
            "https://learn.microsoft.com/en-us/azure/architecture/guide/design-principles/",
        ],
    ),
    Topic(
        id="modularity",
        name="Modularity",
        description="Group related responsibilities into cohesive, independently evolvable units.",
        source_urls=[
            "https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/",
            "https://www.sei.cmu.edu/blog/what-is-software-architecture/",
        ],
    ),
    Topic(
        id="encapsulation",
        name="Encapsulation",
        description="Hide volatile details behind stable boundaries and narrow APIs.",
        source_urls=[
            "https://martinfowler.com/articles/injection.html",
            "https://www.sei.cmu.edu/blog/what-is-software-architecture/",
        ],
    ),
    Topic(
        id="interface-design",
        name="Interface Design",
        description="Shape interfaces around consumer needs and stable contracts.",
        source_urls=[
            "https://learn.microsoft.com/en-us/azure/architecture/guide/design-principles/",
            "https://learn.microsoft.com/en-us/azure/architecture/guide/",
        ],
    ),
    Topic(
        id="persistence-boundaries",
        name="Persistence Boundaries",
        description="Keep storage concerns outside domain and application logic.",
        source_urls=[
            "https://martinfowler.com/articles/injection.html",
            "https://martinfowler.com/articles/microservice-testing/",
        ],
    ),
    Topic(
        id="architectural-conformance",
        name="Architectural Conformance",
        description="Use automated checks to prevent dependency rules from regressing.",
        source_urls=[
            "https://martinfowler.com/articles/microservice-testing/",
            "https://www.sei.cmu.edu/blog/what-is-software-architecture/",
        ],
    ),
    Topic(
        id="cross-cutting-concerns",
        name="Cross-cutting Concerns",
        description="Centralize shared technical concerns instead of duplicating them.",
        source_urls=[
            "https://martinfowler.com/articles/injection.html",
            "https://learn.microsoft.com/en-us/azure/architecture/guide/design-principles/",
        ],
    ),
    Topic(
        id="global-state",
        name="Global State",
        description="Reduce hidden shared state that couples unrelated code paths.",
        source_urls=[
            "https://www.sei.cmu.edu/blog/what-is-software-architecture/",
            "https://martinfowler.com/articles/injection.html",
        ],
    ),
    Topic(
        id="dependency-cycles",
        name="Dependency Cycles",
        description="Break cycles so modules can evolve and test independently.",
        source_urls=[
            "https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/",
            "https://www.sei.cmu.edu/blog/what-is-software-architecture/",
        ],
    ),
    Topic(
        id="data-coupling",
        name="Data Coupling",
        description="Pass only the data a consumer needs and avoid structure leakage.",
        source_urls=[
            "https://learn.microsoft.com/en-us/azure/architecture/guide/design-principles/",
            "https://www.sei.cmu.edu/blog/what-is-software-architecture/",
        ],
    ),
]
