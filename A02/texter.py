# texter.py
# Author: Elena Os
# Encoding: UTF-8
# Description: Assignment A02 - Task 2
# Counts total number of lines and number of lines containing the word "sed".

import sys


class Texter:
    """Analyze a text file for assignment A02 (task 2)."""

    def __init__(self, filename: str) -> None:
        self.filename = filename

    def run(self) -> None:
        """Print total line count and lines containing 'sed' (case-insensitive)."""
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                lines = file.readlines()

            total_lines = len(lines)
            sed_lines = sum(1 for line in lines if "sed" in line.lower())

            print(f"Total number of lines: {total_lines}")
            print(f"Lines containing 'sed': {sed_lines}")

        except FileNotFoundError:
            print(f"Error: File '{self.filename}' not found.")
        except Exception as exc:
            print(f"An error occurred: {exc}")


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python texter.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    analyzer = Texter(filename)
    analyzer.run()


if __name__ == "__main__":
    main()
