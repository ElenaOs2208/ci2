# A09 – Chemistry Web Server

This assignment implements a simple chemistry web server using Flask.
The application allows the user to enter a SMILES string, retrieves
chemical data from an external chemistry web service, generates a 3D
molecule image using Open Babel, and displays the results dynamically
on a single web page.

## Requirements

- Linux OS
- Python 3
- Git
- Open Babel
- POV-Ray (optional)
- Internet connection

## Installation

Clone the repository:

```bash
git clone <REPOSITORY_URL>
cd ci2/A09
## Create and activate virtual environment:
python3 -m venv venv
source venv/bin/activate
## Install Python dependencies:
pip install -r requirements.txt
## Install system dependencies:
sudo apt install openbabel povray
## Running the application

Start the Flask server:
python app.py 
## Open a web browser and go to:
http://127.0.0.1:5000
## Usage

Enter a SMILES string (e.g. CCO)

Click Search

The page displays:

Molecular formula

Molecular weight

3D molecule image

The page is not reloaded; all content is updated dynamically using JavaScript.

Assignment notes

The application uses a single HTML page (SPA)

Communication between frontend and backend is done via JSON

External chemistry web services are used

Open Babel is used to generate 3D molecule images
