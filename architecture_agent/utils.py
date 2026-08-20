from __future__ import annotations

import hashlib


def seeded_random(seed: int = 1):
    value = seed % 2147483647
    if value <= 0:
        value += 2147483646

    def inner() -> float:
        nonlocal value
        value = (value * 16807) % 2147483647
        return value / 2147483647

    return inner


def hash_text(text: str) -> str:
    return hashlib.sha1(text.encode("utf-8")).hexdigest()
