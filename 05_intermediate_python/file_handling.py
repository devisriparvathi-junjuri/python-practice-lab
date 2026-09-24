"""Use pathlib and context managers for safe file handling."""

from pathlib import Path


def save_note(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def load_note(path: Path) -> str:
    return path.read_text(encoding="utf-8")


if __name__ == "__main__":
    print("Use save_note(Path('note.txt'), '...') in a temporary practice folder.")
