# A09 – Chemistry Web Server

This project implements a chemistry web server using **Flask**.  
The application allows the user to enter a chemical structure in **SMILES** format, retrieves compound information from a **remote chemistry web service (ChEMBL)**, generates a **3D molecule image** using **Open Babel** and **POV-Ray**, and displays the results dynamically on a single web page.

The application is implemented as a **single-page application (SPA)** – the page content is updated using JavaScript without reloading the page.

---

## Features

- Single web page interface
- Input of chemical structure in SMILES format
- Retrieval of compound information from the remote **ChEMBL** database (EBI)
- Generation of a 3D molecular structure using **Open Babel**
- Rendering of the molecule image using **POV-Ray**
- Dynamic update of page content using JavaScript and JSON communication

---

## Requirements

### System requirements

- Linux or Windows (WSL)
- Python 3
- Git
- Internet connection

### System packages

- Open Babel
- POV-Ray

### Python packages

- Flask
- Requests

---

## Installation

### 1. Clone the repository

```bash
git clone <REPOSITORY_URL>
cd ci2/A09
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 4. Install system dependencies (Ubuntu / WSL)

```bash
sudo apt update
sudo apt install openbabel povray
```

---

## Running the application

Start the Flask development server:

```bash
python app.py
```

Open a web browser and go to:

```
http://127.0.0.1:5000
```

---

## Usage

1. Enter a SMILES string (e.g. `CCO`) into the input field.
2. Click the **Search** button.
3. The application will:
   - retrieve compound information from the remote **ChEMBL** database,
   - generate a 3D molecule image using **Open Babel** and **POV-Ray**,
   - display the compound information and the generated image on the page.

The page is not reloaded; all content is updated dynamically using JavaScript.

---

## Implementation notes

- The backend is implemented using **Flask** and communicates with the frontend via JSON.
- The remote chemistry web service used is **ChEMBL (EBI)**.
- Open Babel is used to generate 3D molecular structures from SMILES.
- POV-Ray is used to render the final 3D molecule image.
- Generated images are stored in the `static/` directory.

---


