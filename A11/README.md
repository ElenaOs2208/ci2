# A11 – Django Chemistry Web Application

This project is a Django-based web application that provides three chemistry-related functionalities:

## Pages

### A) Home
The home page introduces the application and provides navigation links to all available features.

### B) ChEMBL
- Users can enter a SMILES string.
- The server queries the ChEMBL web service for information about the molecule.
- Each submitted SMILES string is stored in the database together with a timestamp.
- Key molecular properties are displayed in a structured table.
- Full raw ChEMBL data are available for inspection.

### C) PovRay
- Users can enter a SMILES string.
- The server converts the SMILES to a 3D molecular structure using OpenBabel.
- PovRay is used to render a 3D image of the molecule.
- The generated image is displayed on the webpage as a static file.

---

## Setup Instructions

### 1. Clone the repository
```bash
git clone <YOUR_REPOSITORY_URL>
cd A11
2. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate
3. Install Python dependencies
pip install -r requirements.txt

4. Install external tools
The following tools must be installed on the system:

OpenBabel

PovRay

On Ubuntu: 
sudo apt install openbabel povray
5. Apply database migrations
python manage.py migrate
6. Run the development server
python manage.py runserver



Open your browser at:
http://127.0.0.1:8000/
