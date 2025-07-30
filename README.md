# ADS-502-US-Pollution-Analysis

Final project for USD ADS-502: Data mining and classification on the U.S. Pollution dataset (Kaggle).  
- All Python analysis is in `notebooks/analysis.ipynb`
- Helper functions in `scripts/utils.py`
- Figures are saved in `outputs/figures/eda` and `outputs/figures/model_eval`

## Project Structure

ADS-502-US-Pollution-Analysis/
├── data/
├── notebooks/
├── scripts/
├── outputs/
├── requirements.txt
└── README.md


## Setup Instructions

**Before running the analysis, ensure you have the required Python packages installed.**

1. (Optional but recommended) Create a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate        # On macOS/Linux
    venv\Scripts\activate           # On Windows
    ```

2. Install required packages using `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```
   Or, you can install manually:
    ```bash
    pip install pandas numpy matplotlib seaborn scikit-learn
    ```

3. Place the dataset file (`pollution_us_2000_2016.csv`) in the `data/` directory.

4. Open and run `notebooks/analysis.ipynb` in Jupyter or VS Code.

5. All generated results and images will be saved in `outputs/`.

---

## Troubleshooting

- If you see "sklearn cannot be resolved," ensure you have installed `scikit-learn` and are using the correct Python interpreter in VS Code.
- To select the Python interpreter in VS Code:  
    1. Press `Ctrl+Shift+P`  
    2. Type `Python: Select Interpreter`  
    3. Choose the environment where you installed your packages.

---

## Usage

- **Analysis notebook:** `notebooks/analysis.ipynb`
- **Helper functions:** `scripts/utils.py`
- **Figures:** `outputs/figures/eda`, `outputs/figures/model_eval`

---

## Credits

Dataset from [Kaggle: U.S. Pollution Data (2000–2016)](https://www.kaggle.com/datasets/sogun3/uspollution).
