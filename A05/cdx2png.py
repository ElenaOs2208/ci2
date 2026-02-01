#!/usr/bin/env python3

import sys
import subprocess
from pathlib import Path


def molecular_weight(cdxml_file):
    result = subprocess.check_output(
        ["obabel", cdxml_file, "-osmi", "--append", "MW"],
        text=True
    )
    line = result.strip()
    # vezmeme poslední číslo na řádku (Mr)
    try:
        return float(line.split()[-1])
    except ValueError:
        return None


def main():
    files = sys.argv[1:]
    if not files:
        print("Usage: cdx2png.py *.cdxml")
        sys.exit(1)

    min_mw = (None, float("inf"))
    max_mw = (None, 0)

    for f in files:
        cdxml = Path(f)
        png = cdxml.with_suffix(".png")

        # CDXML → PNG
        subprocess.run(
            ["obabel", str(cdxml), "-O", str(png)],
            check=True
        )

        # Mr přes OpenBabel
        mw = molecular_weight(str(cdxml))
        if mw is not None:
            if mw < min_mw[1]:
                min_mw = (cdxml.name, mw)
            if mw > max_mw[1]:
                max_mw = (cdxml.name, mw)

    print(f"Lowest Mr: {min_mw[0]} ({min_mw[1]})")
    print(f"Highest Mr: {max_mw[0]} ({max_mw[1]})")


if __name__ == "__main__":
    main()

