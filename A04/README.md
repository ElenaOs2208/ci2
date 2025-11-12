# A04 – Vytvoření SQLite databáze z CSV souborů

## Cíl úkolu
Cílem je vytvořit Python skript, který:
- vytvoří databázi `db.sqlite`,
- načte data z CSV souborů uložených v archivu `world.zip`,
- vytvoří tabulky `city`, `country`, `countrylanguage`,
- a odpoví na otázku č. 3:
  > Jaký je celkový počet obyvatel zemí s angličtinou jako oficiálním jazykem?

## Použité technologie
- **Python 3.13**
- Moduly: `sqlite3`, `csv`, `zipfile`, `os`, `sys`
- Databáze: **SQLite**

## Postup
1. Klonuj repozitář:
   ```bash
   git clone https://github.com/Anson1907/ci2.git
  ## spustit skript
   py db.py city.csv country.csv countrylanguage.csv
   
##vysledek 
 Jaký je celkový počet obyvatel zemí s angličtinou jako oficiálním jazykem?
Odpověď: 459158800


   cd ci2/A04

