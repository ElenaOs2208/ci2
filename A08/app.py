from flask import Flask, render_template, request
from chembl_api import get_compound_info_from_smiles

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        smiles = request.form.get("smiles", "").strip()

        if not smiles:
            return render_template("index.html", error="Zadejte SMILES řetězec.")

        compound = get_compound_info_from_smiles(smiles)

        if compound is None:
            return render_template("index.html", error="Sloučenina nebyla nalezena.")

        return render_template("results.html", smiles=smiles, compound=compound)

    return render_template("index.html")


if __name__ == "__main__":
    import sys
    app.run(debug=True)
