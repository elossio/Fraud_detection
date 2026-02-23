# Machine Learning applied to Fraud Detection

![Fraud Detection Infographic][def]

This project explores various machine learning techniques to detect fraudulent transactions in a highly imbalanced dataset. It includes data preprocessing, exploratory data analysis, and the implementation of several classification models (Logistic Regression, Decision Trees, XGBoost, etc.) with a focus on handling class imbalance using techniques like Random Under-Sampling (RUS).

## Project Organization

```
├── .gitignore         <- Files and directories to be ignored by Git
├── environment.yml    <- The requirements file for reproducing the analysis environment
├── LICENSE            <- Open source license if one is chosen
├── README.md          <- The top-level README for developers using this project.
│
├── data               <- Data files for the project.
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention: owner initials and short description, e.g., `01-fb-eda`.
│
│   └──src             <- Source code for use in this project.
│      │
│      ├── __init__.py  <- Makes it a Python module
│      ├── config.py    <- Basic project configurations
│      ├── graphics.py  <- Scripts for creating exploratory and results-oriented visualizations
│      ├── helpers.py   <- Scripts for processing data and other tasks
│      ├── models.py    <- Model training and evaluation logic
│      └── models_rus.py <- Model training logic using Random Under-Sampling
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis in HTML, PDF, LaTeX, etc.
│   └── images         <- Generated graphics and figures to be used in reports
```

## Environment Setup

1. Clone the repository:

    ```bash
    git clone REPOSITORY_ADDRESS
    ```

2. Create a virtual environment for your project using your preferred environment manager.

    a. If using `conda`, export the environment dependencies to the `environment.yml` file:

      ```bash
      conda env export > environment.yml
      ```

    b. If using another environment manager, export the dependencies to a `requirements.txt` file or another format of your choice. Add the file to version control, removing the `environment.yml` file.

3. Check the `notebooks/01-el-eda.ipynb` file for usage examples.
4. Rename `notebooks/01-el-eda.ipynb` to a name more appropriate for your project, and follow the naming convention for other notebooks.
5. Check the `notebooks/src/config.py` file for basic project configurations. Modify as necessary, adding or removing file and directory paths.
6. Update the `references/01_data_dictionary.md` file with your project's data dictionary.

[def]: reports/images/fraud_detection_infographic.png