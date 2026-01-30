import subprocess
import uuid
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_IMG_DIR = BASE_DIR / "static" / "images"


def generate_povray_image(smiles):
    STATIC_IMG_DIR.mkdir(parents=True, exist_ok=True)

    uid = uuid.uuid4().hex
    mol_file = STATIC_IMG_DIR / f"{uid}.mol"
    pov_file = STATIC_IMG_DIR / f"{uid}.pov"
    png_file = STATIC_IMG_DIR / f"{uid}.png"

    # 1️⃣ SMILES → 3D MOL (OpenBabel)
    subprocess.run(
        [
            "obabel",
            "-:" + smiles,
            "-O",
            str(mol_file),
            "--gen3d",
        ],
        check=True,
    )

    # 2️⃣ MOL → POV (OpenBabel)
    subprocess.run(
        [
            "obabel",
            str(mol_file),
            "-O",
            str(pov_file),
        ],
        check=True,
    )

    # 3️⃣ POV → PNG (PovRay)
    subprocess.run(
        [
            "povray",
            "+I" + str(pov_file),
            "+O" + str(png_file),
            "+W500",
            "+H400",
            "-D",
        ],
        cwd=STATIC_IMG_DIR,   # ⬅️ KLÍČOVÉ (kvůli babel_povray3.inc)
        check=True,
    )

    return f"images/{uid}.png"


