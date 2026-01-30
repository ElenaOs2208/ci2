Project structure
A10/
├── app.py
├── chemistry_api.py
├── chembl_api.py
├── image_generator.py
├── templates/
├── static/
├── tests/
│   └── test_web.py
├── requirements.txt
└── README.md
Requirements

Python 3.8+

Git

Ubuntu Linux

Internet connection (for remote chemical API)

Setup instructions
1. Clone the repository
git clone <REPOSITORY_URL>
cd ci2/A10
2. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate
3. Install dependencies
pip install -r requirements.txt
pip install playwright pytest pytest-playwright
 
 python -m playwright install --with-deps

4. Running the web server

Start the Flask application:
python app.py
The server will be available at:
http://localhost:5000
Recording browser interaction

Browser interaction was recorded using Playwright codegen:
python -m playwright codegen http://localhost:5000
The recorded script was then adapted into a robust pytest test using Playwright fixtures and assertions.
5. Running the tests
pytest
Expected output:
tests/test_web.py::test_search_by_smiles PASSED
6. Test description

The automated test performs the following steps:

Opens the web application homepage

Enters a SMILES string into the input field

Submits the form

Verifies that a molecular image is generated and displayed

Assertions are implemented using expect() to ensure test robustness.

