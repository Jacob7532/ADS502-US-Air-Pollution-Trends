# scripts/utils.py

import os
import matplotlib.pyplot as plt
import seaborn as sns

def make_project_dirs():
    """Create necessary output folders if they do not exist."""
    dirs = [
        "outputs/figures/eda",
        "outputs/figures/model_eval"
    ]
    for d in dirs:
        os.makedirs(d, exist_ok=True)

def save_histplot(series, title, filename):
    """Save a histogram plot for a data series."""
    plt.figure(figsize=(8, 5))
    sns.histplot(series.dropna(), bins=30, kde=True)
    plt.title(title)
    plt.tight_layout()
    plt.savefig(f"outputs/figures/eda/{filename}.png")
    plt.close()

def save_boxplot(series, title, filename):
    """Save a boxplot for a data series."""
    plt.figure(figsize=(8, 5))
    sns.boxplot(x=series.dropna())
    plt.title(title)
    plt.tight_layout()
    plt.savefig(f"outputs/figures/eda/{filename}.png")
    plt.close()

def save_figure(fig, subdir, filename):
    """General-purpose save for matplotlib figures."""
    os.makedirs(f"outputs/figures/{subdir}", exist_ok=True)
    fig.savefig(f"outputs/figures/{subdir}/{filename}.png")
    plt.close(fig)
