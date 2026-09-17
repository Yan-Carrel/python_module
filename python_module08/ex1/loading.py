#!/usr/bin/python3
import importlib.util
from importlib.metadata import version
import importlib
import sys


def check_dependencies() -> bool:
    missing = False
    dependencies = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready",
        "matplotlib": "Visualization ready"
        }

    for dependency in list(dependencies.keys()):
        if importlib.util.find_spec(dependency):
            comment = dependencies[dependency]
            print(f"[OK] {dependency} ({version(dependency)}) - {comment}")
        else:
            missing = True
            print(f"[Missing]: {dependency}")

    return missing


if __name__ == "__main__":
    print("LOADING STATUS: Loading programs...")

    print("\nChecking dependencies:")

    if check_dependencies():
        print("!Warning, some dependencies are missing")

        print("\nRun the following command to install dependencies using pip:")
        if sys.prefix == sys.base_prefix:
            print("python3 -m venv .venv")
            print("source .venv/bin/activate")
        print("pip install -r requirements.txt")

        print("\nRun the following command ")
        print("to install dependencies using poetry:")
        print("poetry install")
    else:
        np = importlib.import_module("numpy")
        pd = importlib.import_module("pandas")
        plt = importlib.import_module("matplotlib.pyplot")

        rng = np.random.default_rng()
        num_points = 1000
        print("\nAnalyzing Matrix data...")
        print(f"Processing {num_points} data points...")

        df = pd.DataFrame({
            'x': rng.integers(low=0, high=100, size=num_points),
            'y': rng.integers(low=0, high=100, size=num_points),
        })

        print("\nGenerating visualization...")
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.scatter(df['x'], df['y'], s=5, color='green', alpha=0.5)
        ax.set_title("Matrix Data")
        ax.set_xlabel("X")
        ax.set_ylabel("Y")

        output_file = "matrix_analysis.png"
        plt.savefig(output_file, bbox_inches='tight')
        plt.close()

        print(f"\nAnalysis complete! Results saved to: {output_file}")
