import subprocess
import uuid
import os

def generate_molecule_image(smiles: str) -> str:
    """
    Generate 3D molecule image from SMILES using Open Babel.
    Returns relative path to PNG image.
    """
    uid = str(uuid.uuid4())
    mol_file = f"static/images/{uid}.mol"
    png_file = f"static/images/{uid}.png"

    # SMILES -> MOL (3D)
    subprocess.run(
        ["obabel", f"-:{smiles}", "-O", mol_file, "--gen3d"],
        check=True
    )

    # MOL -> PNG
    subprocess.run(
        ["obabel", mol_file, "-O", png_file],
        check=True
    )

    return png_file

