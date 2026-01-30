import requests

def get_molecule_data(smiles: str) -> dict:
    """
    Retrieve basic molecule data from PubChem using SMILES.
    """
    url = (
        "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/"
        "smiles/property/MolecularFormula,MolecularWeight/JSON"
    )

    response = requests.post(url, data={"smiles": smiles})
    response.raise_for_status()

    data = response.json()
    props = data["PropertyTable"]["Properties"][0]

    return {
        "formula": props["MolecularFormula"],
        "weight": props["MolecularWeight"]
    }
