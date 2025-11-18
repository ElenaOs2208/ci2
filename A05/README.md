# A05 – CDXML → PNG konverze

## Popis
Skript `cdx2png.py` převádí soubory **ChemDraw (.cdxml)** na obrázky **.png** pomocí knihovny Pybel (OpenBabel).
Zároveň najde molekulu s nejnižší a nejvyšší relativní molekulovou hmotností (Mr) a vypíše jejich názvy a hodnoty.

## Postup
```bash
git clone https://github.com/ElenaOs2208/ci2.git
cd ci2/A05
python -m venv venv
source venv/Scripts/activate   # Windows
pip install -r requirements.txt
py cdx2png.py *.cdxml
