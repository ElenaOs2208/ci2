# Assignment A06 – Graph Generation in Python

This folder contains the solution for assignment A06.

## Files included

- **graph.csv** – input dataset containing x and y values (linear function y = 2x)
- **graph.py** – Python script that loads graph.csv and generates graph.png
- **graph.png** – output image generated from the script
- **requirements.txt** – list of Python modules required to run the script
- **Untitled.ipynb / other notebooks** – development notebooks (not required for execution)

---

## How to run this assignment after cloning the repository

### 1. Clone the repository

```bash
git clone https://github.com/<YOUR_USERNAME>/<YOUR_REPOSITORY>.git
cd <YOUR_REPOSITORY>/A06
```

Replace `<YOUR_USERNAME>` and `<YOUR_REPOSITORY>` with the actual names.

---

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install all required Python packages

```bash
pip install -r requirements.txt
```

This installs:
- pandas  
- numpy  
- matplotlib  

---

### 4. Run the script to generate the graph

```bash
python3 graph.py graph.csv
```

After running this command, the file **graph.png** will be created in the same folder.

---

## Verification

The output image **graph.png** must contain a linear graph corresponding to the function:

```
y = 2 * x
```

If the graph appears and the file is generated correctly, the assignment is completed.
