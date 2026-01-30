import re
from playwright.sync_api import Page, expect

BASE_URL = "http://localhost:5000"


def test_search_by_smiles(page: Page):
    """
    End-to-end test: search molecule by SMILES.
    Verifies that the server processes input and generates an image.
    """

    # Open homepage
    page.goto(BASE_URL)

    # Fill SMILES input
    smiles_input = page.get_by_role("textbox", name="Enter SMILES")
    smiles_input.fill("CC(=O)Oc1ccccc1C(=O)O")

    # Submit search
    page.get_by_role("button", name="Search").click()

    # Verify molecule image is displayed and has src attribute
    molecule_image = page.locator("img")
    expect(molecule_image).to_be_visible(timeout=10000)
    expect(molecule_image).to_have_attribute("src", re.compile(".+"))


