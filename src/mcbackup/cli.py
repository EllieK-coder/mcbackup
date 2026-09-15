import shutil
from pathlib import Path


def main() -> None:
    world = Path(r"C:\Users\Elianna\curseforge\minecraft\Instances\Autocraft\saves\test")
    dest = Path.home() / "mcbackups" / "world-backup"
    dest.parent.mkdir(parents=True, exist_ok=True)

    archive = shutil.make_archive(str(dest), "zip", root_dir=world)
    size_mb = Path(archive).stat().st_size / 1_000_000
    print(f"Backed up to {archive} ({size_mb:.1f} MB)")