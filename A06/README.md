# Assignment A06 – Graph Generation in Python

This folder contains the solution for assignment A06.

---

## Files included

- **graph.csv** – input dataset containing x and y values (linear function y = 2x)
- **graph.py** – Python script that loads `graph.csv` and generates `graph.png`
- **graph.png** – output image generated from the script
- **requirements.txt** – list of Python packages required to run the assignment
- **Untitled.ipynb** and other notebooks – development only, not required for execution

---

# Complete instructions to run the assignment

Follow the steps below exactly after cloning the repository.  
All commands must be run inside the **A06** folder.

---

## 1️ Clone the repository

Clone the GitHub repository and navigate to the folder for this assignment:

```bash
git clone https://github.com/ElenaOs2208/ci2.git
## 2️ Create a virtual environment

Create an isolated Python environment so that dependencies do not interfere with the system:

```bash
python3 -m venv venv
 This creates a folder named venv, which will contain a private Python installation.
## 3️ Activate the virtual environment, install packages, and generate the graph

### Activate the virtual environment

Before installing dependencies or running scripts, activate the environment:

```bash
source venv/bin/activate

When activated, the terminal prompt will begin with:

(venv)

If (venv) is not visible, the environment is not active.
Install required Python packages

Inside the activated virtual environment, install all Python modules listed in requirements.txt:

pip install -r requirements.txt

This installs:

    pandas

    numpy

    matplotlib

These packages are used to load the CSV file, perform numerical operations, and generate the graph.
Run the script to generate the graph

Execute the Python script that loads the CSV file and produces the output image:

python3 graph.py graph.csv

After successfully running the script, you should see:

Saved graph to graph.png

This means the output graph image has been generated.
The file graph.png will appear in the same directory.
Verification

To confirm that the assignment works correctly:

    Ensure that the file graph.png exists.

    Open the file and verify that it contains a linear graph corresponding to:

y = 2 * x

If the generated image shows a correct linear function, the assignment is successfully completed.
cd ci2/A06

