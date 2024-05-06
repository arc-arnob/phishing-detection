"""
make_dataset.py

This module contains functions to process raw data and create a final dataset ready for analysis.
"""
# -*- coding: utf-8 -*-
import os
import pickle
import sys
import numpy as np
from sklearn.preprocessing import LabelEncoder
from keras._tf_keras.keras.preprocessing.text import Tokenizer
from keras._tf_keras.keras.preprocessing.sequence import pad_sequences


def read_data(data_file):
    """
    Processes raw data and creates a final dataset ready for analysis.
    """
    with open(data_file, "r", encoding="utf-8") as f:
        data_lines = f.readlines()[1:]

    data = [line.strip() for line in data_lines]
    raw_x_data = [line.split("\t")[1] for line in data]
    raw_y_data = [line.split("\t")[0] for line in data]

    return raw_x_data, raw_y_data


def tokenize_data(raw_x_train, raw_x_val, raw_x_test, raw_y_train, raw_y_val, raw_y_test):
    """
    Tokenizes the data using the given tokenizer.
    """
    tokenizer = Tokenizer(lower=True, char_level=True, oov_token='-n-')
    tokenizer.fit_on_texts(raw_x_train + raw_x_val + raw_x_test)
    char_index = tokenizer.word_index
    with open('models/char_index.pkl', 'wb') as f:
        pickle.dump(char_index, f)

    sequence_length = 200
    x_train = pad_sequences(tokenizer.texts_to_sequences(raw_x_train), maxlen=sequence_length)
    x_val = pad_sequences(tokenizer.texts_to_sequences(raw_x_val), maxlen=sequence_length)
    x_test = pad_sequences(tokenizer.texts_to_sequences(raw_x_test), maxlen=sequence_length)

    encoder = LabelEncoder()
    y_train = encoder.fit_transform(raw_y_train)
    y_val = encoder.transform(raw_y_val)
    y_test = encoder.transform(raw_y_test)

    return x_train, x_val, x_test, y_train, y_val, y_test


def process(input_filepath, output_filepath):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    raw_x_train, raw_y_train = read_data(os.path.join(input_filepath, 'train.txt'))
    raw_x_val, raw_y_val = read_data(os.path.join(input_filepath, 'val.txt'))
    raw_x_test, raw_y_test = read_data(os.path.join(input_filepath, 'test.txt'))

    x_train, x_val, x_test, y_train, y_val, y_test = tokenize_data(raw_x_train, raw_x_val, raw_x_test,
                                                                   raw_y_train, raw_y_val, raw_y_test)

    # Save processed data
    os.makedirs(output_filepath, exist_ok=True)
    np.save(os.path.join(output_filepath, 'x_train.npy'), x_train)
    np.save(os.path.join(output_filepath, 'x_val.npy'), x_val)
    np.save(os.path.join(output_filepath, 'x_test.npy'), x_test)
    np.save(os.path.join(output_filepath, 'y_train.npy'), y_train)
    np.save(os.path.join(output_filepath, 'y_val.npy'), y_val)
    np.save(os.path.join(output_filepath, 'y_test.npy'), y_test)


if __name__ == '__main__':
    process(sys.argv[1], sys.argv[2])
