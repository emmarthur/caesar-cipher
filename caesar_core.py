"""
Caesar cipher — shared logic for reference script and FastAPI web app.

Letters shift along the alphabet; digits, spaces, and punctuation stay as-is.
"""

from __future__ import annotations

from typing import Literal

MIN_SHIFT = 1
MAX_SHIFT = 25
Mode = Literal["encrypt", "decrypt"]


def normalize_shift(shift: int) -> int:
    if not MIN_SHIFT <= shift <= MAX_SHIFT:
        raise ValueError(f"Shift must be between {MIN_SHIFT} and {MAX_SHIFT}.")
    return shift


def _shift_char(char: str, offset: int) -> str:
    if "A" <= char <= "Z":
        base = ord("A")
        return chr((ord(char) - base + offset) % 26 + base)
    if "a" <= char <= "z":
        base = ord("a")
        return chr((ord(char) - base + offset) % 26 + base)
    return char


def caesar_transform(text: str, shift: int, mode: Mode) -> str:
    """Encrypt or decrypt `text` with a Caesar shift (letters only)."""
    key = normalize_shift(shift)
    offset = key if mode == "encrypt" else -key
    return "".join(_shift_char(c, offset) for c in text)
