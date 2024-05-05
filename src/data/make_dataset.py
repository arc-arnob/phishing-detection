"""
make_dataset.py

This module contains functions to process raw data and create a final dataset ready for analysis.
"""
# -*- coding: utf-8 -*-
import logging
from pathlib import Path
import os
import pickle
import click
from dotenv import find_dotenv, load_dotenv
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.preprocessing.text import Tokenizer
import numpy as np
from keras.preprocessing.sequence import pad_sequences



@click.command()
@click.argument('input_filepath', type=click.Path(exists=True))
@click.argument('output_filepath', type=click.Path())
def main():
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')
    # TO_DO: Add a data processing stage.

    # File Paths
    train_file = os.path.join(input_filepath, 'train.txt')
    test_file = os.path.join(input_filepath, 'test.txt')
    val_file = os.path.join(input_filepath, 'val.txt')

    with open(train_file, "r", encoding="utf-8") as f:
        train_lines = f.readlines()[1:]

    train = [line.strip() for line in train_lines]
    raw_x_train = [line.split("\t")[1] for line in train]
    raw_y_train = [line.split("\t")[0] for line in train]

    with open(test_file, "r", encoding="utf-8") as f:
        test_lines = f.readlines()
    test = [line.strip() for line in test_lines]
    raw_x_test = [line.split("\t")[1] for line in test]
    raw_y_test = [line.split("\t")[0] for line in test]

    with open(val_file, "r", encoding="utf-8") as f:
        val_lines = f.readlines()
    val=[line.strip() for line in val_lines]
    raw_x_val=[line.split("\t")[1] for line in val]
    raw_y_val=[line.split("\t")[0] for line in val]

    tokenizer = Tokenizer(lower=True, char_level=True, oov_token='-n-')
    tokenizer.fit_on_texts(raw_x_train + raw_x_val + raw_x_test)
    char_index = tokenizer.word_index
    with open('models/char_index.pkl', 'wb') as f:
        pickle.dump(char_index, f)
    sequence_length=200
    x_train = pad_sequences(tokenizer.texts_to_sequences(raw_x_train), maxlen=sequence_length)
    x_val = pad_sequences(tokenizer.texts_to_sequences(raw_x_val), maxlen=sequence_length)
    x_test = pad_sequences(tokenizer.texts_to_sequences(raw_x_test), maxlen=sequence_length)

    encoder = LabelEncoder()

    y_train = encoder.fit_transform(raw_y_train)
    y_val = encoder.transform(raw_y_val)
    y_test = encoder.transform(raw_y_test)

    # Save processed data
    os.makedirs(output_filepath, exist_ok=True)
    np.save(os.path.join(output_filepath, 'x_train.npy'), x_train)
    np.save(os.path.join(output_filepath, 'x_val.npy'), x_val)
    np.save(os.path.join(output_filepath, 'x_test.npy'), x_test)
    np.save(os.path.join(output_filepath, 'y_train.npy'), y_train)
    np.save(os.path.join(output_filepath, 'y_val.npy'), y_val)
    np.save(os.path.join(output_filepath, 'y_test.npy'), y_test)


if __name__ == '__main__':
    LOG_FMT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=LOG_FMT)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
