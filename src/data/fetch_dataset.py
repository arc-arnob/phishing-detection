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

# Download and extract testing data
# test_zip_path, _ = urllib.request.urlretrieve(test_URL)
extract_files(test_zip_path, EXTRACT_DIR)

# Download and extract training data
# train_zip_path, _ = urllib.request.urlretrieve(train_URL)
extract_files(train_zip_path, EXTRACT_DIR)


# Download and extract validation data
# val_zip_path, _ = urllib.request.urlretrieve(val_URL)
extract_files(val_zip_path, EXTRACT_DIR)