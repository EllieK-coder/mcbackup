from pathlib import Path

import pytest

from mcbackup.rotate import select_for_deletion


def make(names: list[str]) -> list[Path]:
    return [Path(f"C:/backups/{n}") for n in names]


def test_keeps_newest_and_deletes_the_rest():
    archives = make([
        "world-20260101-120000.zip",
        "world-20260103-120000.zip",
        "world-20260102-120000.zip",
    ])
    doomed = select_for_deletion(archives, keep=1)
    assert [p.name for p in doomed] == [
        "world-20260102-120000.zip",
        "world-20260101-120000.zip",
    ]


def test_keeps_everything_when_under_the_limit():
    archives = make(["world-20260101-120000.zip"])
    assert select_for_deletion(archives, keep=5) == []


def test_empty_directory_is_fine():
    assert select_for_deletion([], keep=3) == []


def test_keep_zero_deletes_everything():
    archives = make(["world-20260101-120000.zip", "world-20260102-120000.zip"])
    assert len(select_for_deletion(archives, keep=0)) == 2


def test_negative_keep_is_rejected():
    with pytest.raises(ValueError):
        select_for_deletion([], keep=-1)