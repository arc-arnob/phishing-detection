REMLA24-TEAM-11

## Local Development

### Prerequisites
You will need to have `poetry` installed on your machine. If you don't have it installed, you can install it by following the instructions [here](https://python-poetry.org/docs/).
In addition to that, you will need Python 3.11 installed on your machine. You can install it by following the instructions [here](https://www.python.org/downloads/).
To set poetry to use Python 3.11, run the following command `poetry env use 3.11`.

### Setup
1. Clone the repository
2. Run `poetry install --with dev` to install the dependencies
3. Run `poetry shell` to activate the virtual environment

### Lint
To lint the code, run the following command `pre-commit run --all-files`


### Data Setup
To get data you can do one of two things
1. Download from Kaggle and place the train.txt, test.txt and val.txt files in data/raw/
2. Install wget and `cd` to `src` and run following lines of shell commands:

    ```bash
    wget https://drive.usercontent.google.com/download\?id\=1N2vhSR7Zi2qYbtxK4-unO8dvzo8oji7z\&export\=download\&authuser\=0\&confirm\=t -O ./data/raw/train.zip
    
    wget https://drive.google.com/uc\?export=download\&confirm=no_antivirus\&id=1I5RSGrXX7qFAEcFouAIirhICF4S3cLF9 -O ./data/raw/test.zip

    wget https://drive.google.com/uc\?export=download\&confirm=no_antivirus\&id=1-EoxS7YPMXC3iYZF46GPH4BNOeWnZJmf -O ./data/raw/val.zip
    ```

### Execute Pipeline
To run the pipeline simply run `dvc repro` <br>
After running the pipeline we can observe some results: <br>
To see metrics run `dvc metrics show` <br>
To see plots run `dvc plots show`


# Project Structure

The directory structure of your new project looks like this: 

```
├── LICENSE
├── Makefile[X]        <- Makefile with commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external[X]       <- Data from third party sources.
│   ├── interim[X]        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs[X]            <- A default Sphinx project; see sphinx-doc.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks for experiments
│
├── eval               <- Generated metrics and plot data in JSON file
├── reports[X]            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
├── src                <- Source code for use in this project.
│   ├── __init__.py    <- Makes src a Python module
│   │
│   ├── data           <- Scripts to download or generate data
|   |   └── fetch_dataset.py
│   │   └── make_dataset.py
│   │
│   ├── models         <- Scripts to train models and then use trained models to make
│   │   │                 predictions
│   │   ├── evaluation.py
│   │   └── train_model.py
│   │
│   └── visualization[X]  <- Scripts to create exploratory and results oriented visualizations
│       └── visualize.py
│
└── tox.ini[X]            <- tox file with settings for running tox; see tox.readthedocs.io
```
