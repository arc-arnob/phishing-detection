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
