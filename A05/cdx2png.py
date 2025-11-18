import os
import sys
import pybel

def main():
    if len(sys.argv) < 2:
        print("Použití: py cdx2png.py *.cdxml [nebo jiné soubory]")
        sys.exit(1)

    cdxml_files = [f for f in sys.argv[1:] if f.endswith(".cdxml")]
    if not cdxml_files:
        print("Nebyl nalezen žádný .cdxml soubor.")
        sys.exit(1)

    min_mol = None
    max_mol = None
    min_mass = float('inf')
    max_mass = 0.0

    for f in cdxml_files:
        mol = next(pybel.readfile("cdxml", f))
        mol.draw(show=False, filename=f.replace(".cdxml", ".png"))

        mass = mol.molwt
        if mass < min_mass:
            min_mass = mass
            min_mol = f
        if mass > max_mass:
            max_mass = mass
            max_mol = f

    print(f"Nejmenší molekula: {min_mol} (Mr = {min_mass:.2f})")
    print(f"Největší molekula: {max_mol} (Mr = {max_mass:.2f})")

if __name__ == "__main__":
    main()
