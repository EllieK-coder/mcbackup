from pathlib import Path


def find_archives(backup_dir: Path) -> list[Path]:
    return list(backup_dir.glob("world-*.zip"))


def select_for_deletion(archives: list[Path], keep: int) -> list[Path]:
    if keep < 0:
        raise ValueError("keep must be non-negative")
    newest_first = sorted(archives, key=lambda p: p.name, reverse=True)
    return newest_first[keep:]