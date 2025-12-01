import sys
import pandas as pd
import matplotlib.pyplot as plt

def generate_graph(csv_path, output_path="graph.png"):
    df = pd.read_csv(csv_path)

    x = df["x"]
    y = df["y"]

    plt.plot(x, y)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Linear function: y = 2 * x")
    plt.grid(True)

    plt.savefig(output_path)
    print(f"Saved graph to {output_path}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python graph.py graph.csv")
    else:
        generate_graph(sys.argv[1])
