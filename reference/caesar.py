"""Terminal Caesar cipher — book-style encrypt/decrypt loop."""

from __future__ import annotations

import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from caesar_core import MAX_SHIFT, MIN_SHIFT, caesar_transform, normalize_shift  # noqa: E402


def ask_mode() -> str:
    while True:
        choice = input("Do you want to (e)ncrypt or (d)ecrypt? ").strip().lower()
        if choice in {"e", "encrypt"}:
            return "encrypt"
        if choice in {"d", "decrypt"}:
            return "decrypt"
        print("Please enter e or d.")


def ask_shift() -> int:
    while True:
        raw = input(f"Enter the key number ({MIN_SHIFT}-{MAX_SHIFT}): ").strip()
        if not raw.isdecimal():
            print("Enter a whole number.")
            continue
        shift = int(raw)
        try:
            return normalize_shift(shift)
        except ValueError as exc:
            print(exc)


def main() -> None:
    mode = ask_mode()
    shift = ask_shift()
    message = input("Enter message: ")
    print(caesar_transform(message, shift, mode))  # type: ignore[arg-type]  # mode validated above


if __name__ == "__main__":
    main()
