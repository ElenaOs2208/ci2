from django.shortcuts import render
from .models import SmilesSearch
from .chembl_api import get_molecule_info
from .povray_utils import generate_povray_image
import json


def home(request):
    return render(request, "home.html")


def chembl_view(request):
    result = None
    result_json = None
    smiles = ""
    error = None

    if request.method == "POST":
        smiles = request.POST.get("smiles", "").strip()

        if smiles:
            SmilesSearch.objects.create(smiles=smiles)

            try:
                chembl_result = get_molecule_info(smiles)

                if chembl_result is None:
                    error = "No molecule found in ChEMBL."
                else:
                    # strukturovaná data pro tabulku
                    result = chembl_result
                    # hezky formátovaný JSON pro <details>
                    result_json = json.dumps(chembl_result, indent=4)

            except Exception as e:
                error = f"ChEMBL connection error: {e}"

    return render(
        request,
        "chembl.html",
        {
            "result": result,
            "result_json": result_json,
            "smiles": smiles,
            "error": error,
        },
    )


def povray_view(request):
    image_path = None
    smiles = ""
    error = None

    if request.method == "POST":
        smiles = request.POST.get("smiles", "").strip()

        if smiles:
            try:
                image_path = generate_povray_image(smiles)
            except Exception as e:
                error = f"PovRay error: {e}"

    return render(
        request,
        "povray.html",
        {
            "image_path": image_path,
            "smiles": smiles,
            "error": error,
        },
    )

