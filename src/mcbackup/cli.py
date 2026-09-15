import shutil
from datetime import datetime
from pathlib import Path


def main() -> None:
    world = Path(r"C:\Users\Elianna\curseforge\minecraft\Instances\Autocraft\saves\test")
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    dest = Path.home() / "mcbackups" / f"world-{stamp}"
    dest.parent.mkdir(parents=True, exist_ok=True)

    archive = shutil.make_archive(str(dest), "zip", root_dir=world)
    size_mb = Path(archive).stat().st_size / 1_000_000
    print(f"Backed up to {archive} ({size_mb:.1f} MB)")