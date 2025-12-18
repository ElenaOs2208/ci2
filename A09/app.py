from image_generator import generate_molecule_image
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

from chemistry_api import get_molecule_data

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/search", methods=["POST"])
def api_search():
    data = request.get_json()
    smiles = data.get("smiles", "")

    molecule = get_molecule_data(smiles)
    image_path = generate_molecule_image(smiles)

    return jsonify({
        "smiles": smiles,
        "formula": molecule["formula"],
        "weight": molecule["weight"],
        "image": image_path
    })


if __name__ == "__main__":
    app.run(debug=True)

