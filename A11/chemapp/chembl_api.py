import requests

CHEMBL_BASE_URL = "https://www.ebi.ac.uk/chembl/api/data/molecule.json"


def get_molecule_info(smiles):
    params = {
        "smiles": smiles,
        "limit": 1
    }
    response = requests.get(CHEMBL_BASE_URL, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()

    if data["page_meta"]["total_count"] == 0:
        return None

    return data["molecules"][0]
