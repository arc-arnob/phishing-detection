
# Test Link: https://drive.google.com/uc?export=download&id=1I5RSGrXX7qFAEcFouAIirhICF4S3cLF9
# Train Link: https://drive.google.com/uc?export=download&id=1N2vhSR7Zi2qYbtxK4-unO8dvzo8oji7z
# Val Link: https://drive.google.com/file/d/1-EoxS7YPMXC3iYZF46GPH4BNOeWnZJmf/view?usp=drive_link


import urllib.request
import zipfile
import os

# TODO: Fix Train download, too big for autoscan. Swap link and you'll see things getting downloaded
train_URL = 'https://drive.google.com/uc?export=download&confirm=no_antivirus&id=1N2vhSR7Zi2qYbtxK4-unO8dvzo8oji7z'
test_URL = 'https://drive.google.com/uc?export=download&confirm=no_antivirus&id=1I5RSGrXX7qFAEcFouAIirhICF4S3cLF9'
val_URL = 'https://drive.google.com/uc?export=download&confirm=no_antivirus&id=1-EoxS7YPMXC3iYZF46GPH4BNOeWnZJmf'

EXTRACT_DIR = "./data/raw/"

# Create the directory if it doesn't exist
if not os.path.exists(EXTRACT_DIR):
    os.makedirs(EXTRACT_DIR)

def extract_files(zip_file, extract_to):
    with zipfile.ZipFile(zip_file, "r") as f:
        f.extractall(extract_to)

# Download and extract testing data
test_zip_path, _ = urllib.request.urlretrieve(test_URL)
extract_files(test_zip_path, EXTRACT_DIR)

# Download and extract training data
train_zip_path, _ = urllib.request.urlretrieve(train_URL)
extract_files(train_zip_path, EXTRACT_DIR)


# Download and extract validation data
val_zip_path, _ = urllib.request.urlretrieve(val_URL)
extract_files(val_zip_path, EXTRACT_DIR)