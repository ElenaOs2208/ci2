# A05 – CDXML to PNG Converter (Assignment 3)

This repository contains my solution for Assignment A05, task 3.

The task was to write a Python script (`cdx2png.py`) that:

- reads a set of `.cdxml` (ChemDraw) files,
- converts each one into `.png` images using the OpenBabel program,
- calculates the relative molecular weight (Mr),
- identifies the molecule with the lowest and highest Mr.

## ⚠️ Important note about the provided CDXML files

The CDXML files included in the ZIP archive from the assignment do **not** contain chemically interpretable molecular structures.

They are *ChemDraw reaction-template files (rxXXXXX.cdxml)* with graphical elements (nodes and arrows), not actual molecular atoms and bonds.

Because of this:

- OpenBabel **can** convert them to PNG ✔️  
- OpenBabel **cannot** extract molecular information ❌  
- therefore molecular weights (Mr) cannot be calculated

The script therefore prints:

No valid molecular weights found. The CDXML files appear to contain no chemically interpretable structures.
This behavior is correct and expected for these files.

## How to run the script

### 1. Clone the repository
git clone https://github.com/ElenaOs2208/ci2
cd A05

### 2. Requirements

You must have **OpenBabel 3.1.1** installed on Windows.  
Download here:

https://github.com/openbabel/openbabel/releases/tag/openbabel-3-1-1

Verify installation:

obabel -V

Expected output:

Open Babel 3.1.1

### 3. Run the script

Place your `.cdxml` files in the same directory as `cdx2png.py` and run:

python cdx2png.py *.cdxml

or, if you have multiple Python versions:

py cdx2png.py *.cdxml

### 4. Output files

- For each CDXML file → a PNG file is created
- The script attempts to compute molecular weight (Mr)
- If no chemically valid structures exist, a message is shown

## Repository structure

A05/
├── cdx2png.py
├── *.cdxml
├── *.png
├── README.md

## End of README


