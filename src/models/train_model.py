"""
model_training.py

This module contains functions for building, training, and saving a cnn model for text classification.
"""
import pickle
import numpy as np
from keras._tf_keras.keras.models import Sequential
from keras._tf_keras.keras.layers import Embedding, Conv1D, MaxPooling1D, Flatten, Dense, Dropout


def build_model(voc_size, categories):
    """
    Build a convolutional neural network model.
    """
    model = Sequential()
    model.add(Embedding(voc_size + 1, 50))
    model.add(Conv1D(128, 3, activation='tanh'))
    model.add(MaxPooling1D(3))
    model.add(Dropout(0.2))

    model.add(Conv1D(128, 7, activation='tanh', padding='same'))
    model.add(Dropout(0.2))

    model.add(Conv1D(128, 5, activation='tanh', padding='same'))
    model.add(Dropout(0.2))

    model.add(Conv1D(128, 3, activation='tanh', padding='same'))
    model.add(MaxPooling1D(3))
    model.add(Dropout(0.2))

    model.add(Conv1D(128, 5, activation='tanh', padding='same'))
    model.add(Dropout(0.2))

    model.add(Conv1D(128, 3, activation='tanh', padding='same'))
    model.add(MaxPooling1D(3))
    model.add(Dropout(0.2))

    model.add(Conv1D(128, 3, activation='tanh', padding='same'))
    model.add(MaxPooling1D(3))
    model.add(Dropout(0.2))

    model.add(Flatten())
    model.add(Dense(len(categories) - 1, activation='sigmoid'))

    return model


def train_model(model, x_train, y_train, x_val, y_val, batch_size, epochs, loss_function, optimizer):
    """
    Trains model with x_train and y_train.
    """
    model.compile(loss=loss_function, optimizer=optimizer, metrics=['accuracy'])
    hist = model.fit(x_train, y_train,
                     batch_size=batch_size,
                     epochs=epochs,
                     shuffle=True,
                     validation_data=(x_val, y_val))
    return hist


def save_model(model, filepath):
    """
    Saves model.
    """
    model.save(filepath)


if __name__ == '__main__':
    # Dependency
    with open('models/char_index.pkl', 'rb') as f:
        char_index = pickle.load(f)
    params = {'loss_function': 'binary_crossentropy',
              'optimizer': 'adam',
              'sequence_length': 200,
              'batch_train': 5000,
              'batch_test': 5000,
              'categories': ['phishing', 'legitimate'],
              'char_index': char_index,
              'epoch': 1,
              'embedding_dimension': 50,
              'dataset_dir': "../data/raw"}

    # Assuming char_index is defined elsewhere
    voc_size = len(params['char_index'].keys())

    model = build_model(voc_size, params['categories'])
    # Dependency
    x_train = np.load('data/processed/x_train.npy')
    y_train = np.load('data/processed/y_train.npy')

    x_val = np.load('data/processed/x_val.npy')
    y_val = np.load('data/processed/y_val.npy')

    hist = train_model(model, x_train, y_train, x_val, y_val,
                       params['batch_train'], params['epoch'],
                       params['loss_function'], params['optimizer'])

    # Save the trained model
    MODEL_OUTPUT_FILEPATH = 'models/model.keras'
    save_model(model, MODEL_OUTPUT_FILEPATH)
