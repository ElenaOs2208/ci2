# sdbs_parser.py
# Author: Elena Os
# Description: Assignment A03 - Task 3
# Extracts compound names from an SDBS HTML results page.

import sys
from bs4 import BeautifulSoup

def main():
    if len(sys.argv) < 2:
        print("Usage: python sdbs_parser.py <html_file>")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        # otevři HTML soubor s kódováním utf-8
        with open(filename, encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'html.parser')

        # najdi všechny <td class="comp-name"> elementy
        compounds = soup.find_all('td', class_='comp-name')

        # vypiš každý název na samostatný řádek
        for c in compounds:
            print(c.get_text(strip=True))

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

if __name__ == "__main__":
    main()
