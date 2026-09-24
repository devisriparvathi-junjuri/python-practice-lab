"""Organize files by extension using pathlib."""

import argparse
import shutil
from pathlib import Path


def destination_for(file_path: Path) -> str:
    return file_path.suffix.lower().lstrip(".") or "no_extension"


def organize(folder: Path, *, dry_run: bool = True) -> list[tuple[Path, Path]]:
    if not folder.is_dir():
        raise ValueError("folder must be an existing directory")
    moves: list[tuple[Path, Path]] = []
    for file_path in folder.iterdir():
        if file_path.is_file() and file_path.name != Path(__file__).name:
            destination = folder / destination_for(file_path) / file_path.name
            moves.append((file_path, destination))
            if not dry_run:
                destination.parent.mkdir(exist_ok=True)
                shutil.move(str(file_path), str(destination))
    return moves


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("folder", type=Path)
    parser.add_argument("--apply", action="store_true", help="perform moves instead of previewing")
    args = parser.parse_args()
    for source, destination in organize(args.folder, dry_run=not args.apply):
        print(f"{source.name} -> {destination.parent.name}/")

if __name__ == "__main__":
    main()
