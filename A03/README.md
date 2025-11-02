\# Assignment A03 – Task 3



\*\*Repository:\*\* \[https://github.com/ElenaOs2208/ci2](https://github.com/ElenaOs2208/ci2)



\## Description

This script (`sdbs\_parser.py`) parses the HTML file `sdbs\_benzidine.html`

downloaded from the SDBS database and prints the names of all compounds found

on the first page of results (inside `<td class="comp-name">` elements).



\## How to run



```bash

\# Clone repository

git clone git@github.com:ElenaOs2208/ci2.git

cd ci2/A03



\# Create and activate virtual environment

py -m venv venv

source venv/Scripts/activate   # (on Windows Git Bash)

\# venv\\Scripts\\activate        # (on Windows CMD/PowerShell)



\# Install required package

pip install beautifulsoup4



\# Run the script

py sdbs\_parser.py sdbs\_benzidine.html



