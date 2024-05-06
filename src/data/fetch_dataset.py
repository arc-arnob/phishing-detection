import zipfile
import os

train_zip_path = './data/raw/train.zip'
test_zip_path = './data/raw/test.zip'
val_zip_path = './data/raw/val.zip'


EXTRACT_DIR = "./data/raw/"

# Create the directory if it doesn't exist
if not os.path.exists(EXTRACT_DIR):
    os.makedirs(EXTRACT_DIR)

def extract_files(zip_file, extract_to):
    with zipfile.ZipFile(zip_file, "r") as f:
        f.extractall(extract_to)

extract_files(test_zip_path, EXTRACT_DIR)
extract_files(train_zip_path, EXTRACT_DIR)
extract_files(val_zip_path, EXTRACT_DIR)