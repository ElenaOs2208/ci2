from chembl_webresource_client.new_client import new_client

def get_compound_info_from_smiles(smiles: str):
    """
    Vyhledá sloučeninu podle SMILES v databázi ChEMBL a vrátí první výsledek.
    Pokud není nalezena, vrací None.
    """
    molecule = new_client.molecule
    results = molecule.filter(smiles=smiles)

    if len(results) == 0:
        return None

    return results[0]


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        smiles = sys.argv[1]
        compound = get_compound_info_from_smiles(smiles)
        print(compound)
    else:
        print("Použití: python3 chembl_api.py \"SMILES\"")
