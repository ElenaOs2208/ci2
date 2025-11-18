import sys
import glob
import subprocess
import os

def convert_cdxml_to_png(file):
    """Use OpenBabel command-line tool to convert .cdxml → .png"""
    png_name = file.replace(".cdxml", ".png")
    cmd = ["obabel", file, "-O", png_name]
    subprocess.run(cmd, check=True)
    return png_name

def convert_cdxml_to_mol(file):
    """Convert CDXML → MOL so we can read molecular weight"""
    mol_name = file.replace(".cdxml", ".mol")
    cmd = ["obabel", file, "-O", mol_name]
    subprocess.run(cmd, check=True)
    return mol_name

def get_molecular_weight_from_mol(mol_file):
    """Read MW from MOL using 'obabel -oinfo'."""
    cmd = ["obabel", mol_file, "-oinfo"]
    result = subprocess.run(cmd, capture_output=True, text=True)

    for line in result.stdout.splitlines():
        if "Molecular weight" in line:
            try:
                return float(line.split("=")[1].strip())
            except:
                pass
    return None

def main():
    args = sys.argv[1:]
    if not args:
        print("Usage: python cdx2png.py *.cdxml")
        sys.exit(1)

    files = []
    for arg in args:
        files.extend(glob.glob(arg))

    if not files:
        print("No CDXML files found.")
        sys.exit(1)

    results = []

    for file in files:
        try:
            png = convert_cdxml_to_png(file)
            mol = convert_cdxml_to_mol(file)
            mr = get_molecular_weight_from_mol(mol)
            results.append((file, mr))
            print(f"Converted: {file} → {png}   (Mr = {mr})")
        except Exception as e:
            print(f"Error converting {file}: {e}")

    valid = [item for item in results if item[1] is not None]

    print("\n=== SUMMARY ===")

    if not valid:
        print("No valid molecular weights found. The CDXML files appear to contain no chemically interpretable structures.")
        sys.exit(0)

    min_mol = min(valid, key=lambda x: x[1])
    max_mol = max(valid, key=lambda x: x[1])

    print(f"Lowest Mr:  {min_mol[0]}   (Mr = {min_mol[1]})")
    print(f"Highest Mr: {max_mol[0]}   (Mr = {max_mol[1]})")

if __name__ == "__main__":
    main()
