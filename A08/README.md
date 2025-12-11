# A08 — Flask aplikace pro vyhledávání sloučenin podle SMILES (ChEMBL)

Tento úkol implementuje jednoduchou webovou aplikaci v Pythonu pomocí Flask.
Uživatel zadá chemickou strukturu ve formátu **SMILES**, aplikace odešle dotaz do databáze **ChEMBL** a zobrazí informace o nalezené sloučenině.

Aplikace využívá:

- standardní Python knihovny 
- balík **chembl_webresource_client**
- knihovnu **Flask**
- webové rozhraní v HTML + CSS

Aplikace extrahuje **první nalezenou sloučeninu** z výsledků databáze ChEMBL.

---

##  Struktura projektu

```
A08/
│ app.py
│ chembl_api.py
│ requirements.txt
│ README.md
│
├── templates/
│     base.html
│     index.html
│     results.html
│
└── static/
      style.css
```

---

##  Instalace a spuštění aplikace

### 1️ Klonování repozitáře

```
git clone https://github.com/ElenaOs2208/ci2
cd ci2/A08
```

---

### 2️ Vytvoření a aktivace virtuálního prostředí

```
python3 -m venv venv
source venv/bin/activate
```

---

### 3️ Instalace závislostí

```
pip install -r requirements.txt
```

---

### 4️ Spuštění aplikace

```
python3 app.py
```

Aplikace běží zde:

```
http://127.0.0.1:5000/
```

---

## Použití

1. Otevřete webový prohlížeč 
2. Zadejte SMILES 
3. Odešlete formulář 
4. Zobrazí se informace o první nalezené sloučenině 
5. Lze provést nové vyhledávání 

---

# Ukázkový výstup pro *salicylic acid* (sloučenina č. 7)

### Použitý SMILES:
```
OC(=O)c1ccccc1O
```

### Výstup aplikace:
```
ChEMBL ID: CHEMBL505
Název: SALICYLIC ACID
Molekulová formule: C7H6O3
Molekulová hmotnost: 138.12
```

---

##  Poznámka

Některé sloučeniny ze seznamu nejsou v databázi ChEMBL. 
Aplikace v takových případech korektně zobrazí, že sloučenina nebyla nalezena.

