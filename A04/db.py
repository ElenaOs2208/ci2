import sqlite3
import csv
import zipfile
import os
import sys

class DatabaseCreator:
    def __init__(self, args):
        self.db_name = "db.sqlite"
        self.zip_name = "world.zip"
        self.csv_files = args
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self.create_from_csv()

    def create_from_csv(self):
        with zipfile.ZipFile(self.zip_name, 'r') as z:
            for csv_name in self.csv_files:
                table_name = os.path.splitext(csv_name)[0]
                if not self.table_exists(table_name):
                    print(f"Vytvářím tabulku {table_name}...")
                    with z.open(csv_name) as f:
                        text = f.read().decode("utf-8", errors="ignore").splitlines()
                        reader = csv.reader(text, delimiter=';', quotechar='"')
                        headers = next(reader)
                        columns = ", ".join([f'"{h}" TEXT' for h in headers])
                        self.cursor.execute(f"CREATE TABLE {table_name} ({columns})")
                        for row in reader:
                            placeholders = ", ".join(["?"] * len(row))
                            self.cursor.execute(f"INSERT INTO {table_name} VALUES ({placeholders})", row)
            self.conn.commit()
        self.answer_question()

    def table_exists(self, table_name):
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
        return self.cursor.fetchone() is not None

    def answer_question(self):
        print("Jaký je celkový počet obyvatel zemí s angličtinou jako oficiálním jazykem?")
        query = """
            SELECT SUM(country.Population)
            FROM country
            JOIN countrylanguage ON country.Code = countrylanguage.CountryCode
            WHERE countrylanguage.Language = 'English' AND countrylanguage.IsOfficial = 'T'
        """
        self.cursor.execute(query)
        result = self.cursor.fetchone()[0]
        print("Odpověď:", result)

if __name__ == "__main__":
    DatabaseCreator(sys.argv[1:])
