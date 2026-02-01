# A05 – CDXML to PNG conversion using OpenBabel

This assignment converts a set of ChemDraw CDXML files into PNG images using the OpenBabel program.
At the same time, it identifies the molecules with the lowest and highest relative molecular weight (Mr).

## Requirements

- Linux (tested on Ubuntu)
- Python 3.10+
- OpenBabel

## Installation

Clone the repository:

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd A05Create and activate a virtual environment: 
python3 -m venv venv
source venv/bin/activate
Install OpenBabel if not already installed:
Files

cdx2png.py – Python script for converting CDXML files to PNG and computing Mr

*.cdxml – input ChemDraw files

*.png – generated imagesUsage

Run the script in the A05 directory:
sudo apt install openbabel

Usage

Run the script in the A05 directory:
./cdx2png.py *.cdxml
The script:

creates PNG images with the same base name as the CDXML files

prints the molecules with the lowest and highest molecular weight (Mr)

Example output:
Lowest Mr: rx00153.cdxml (87.4845)
Highest Mr: rx00259.cdxml (336.3)
