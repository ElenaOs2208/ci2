from flask import Flask, render_template, request, jsonify
import requests
import subprocess
import uuid
import os

app = Flask(__name__)

STATIC_DIR = "static"

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/process", methods=["POST"])
def process_smiles():
    data = request.get_json()
    smiles = data.get("smiles")

    if not smiles:
        return jsonify({"error": "No SMILES provided"}), 400

    uid = str(uuid.uuid4())

    mol_file = os.path.join(STATIC_DIR, f"{uid}.mol")
    pov_file = os.path.join(STATIC_DIR, f"{uid}.pov")
    png_file = os.path.join(STATIC_DIR, f"{uid}.png")

    # =========================
    # ChEMBL remote API lookup
    # =========================
    chembl_data = {}
    try:
        url = "https://www.ebi.ac.uk/chembl/api/data/molecule.json"
        params = {
            "smiles": smiles,
            "limit": 1
        }
        r = requests.get(url, params=params, timeout=10)
        r.raise_for_status()
        result = r.json()

        if result.get("molecules"):
            mol = result["molecules"][0]
            chembl_data = {
                "chembl_id": mol.get("molecule_chembl_id"),
                "pref_name": mol.get("pref_name"),
                "formula": mol.get("molecule_properties", {}).get("full_molformula"),
                "molecular_weight": mol.get("molecule_properties", {}).get("full_mwt")
            }
    except Exception:
        chembl_data = {
            "error": "ChEMBL lookup failed"
        }

    # =========================
    # Open Babel: SMILES → 3D
    # =========================
    subprocess.run(
        ["obabel", f"-:{smiles}", "-O", mol_file, "--gen3d"],
        check=True
    )

    # =========================
    # Open Babel: MOL → POV
    # =========================
    subprocess.run(
        ["obabel", mol_file, "-O", pov_file],
        check=True
    )

    # =========================
    # POV-Ray: POV → PNG
    # =========================
    subprocess.run(
        [
            "povray",
            f"+I{pov_file}",
            f"+O{png_file}",
            "+W600", "+H600",
            "+D", "+FN",
            "+L/usr/share/povray/include"
        ],
        check=True
    )

    return jsonify({
        "image": png_file,
        "chembl": chembl_data
    })


if __name__ == "__main__":
    app.run(debug=True)

