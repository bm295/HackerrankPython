from __future__ import annotations

from collections.abc import Callable

from architecture_agent.types import Topic
from architecture_agent.utils import seeded_random


def select_topic(topics: list[Topic], seed: int, applicable: Callable[[Topic], bool]) -> Topic:
    rand = seeded_random(seed)
    pool = topics[:]
    while pool:
        index = int(rand() * len(pool))
        topic = pool.pop(index)
        if applicable(topic):
            return topic
    return topics[0]
