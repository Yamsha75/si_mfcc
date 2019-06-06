import os

import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import Dense, Dropout, Flatten
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam


hots = np.eye(8, 8)


def load_data(path):
    files = os.listdir(path)
    data = []
    ans = []
    for file in files:
        _data = np.load(path + file)
        ans_class = int(file[6:8])
        if ans_class == 2 or ans_class == 7:
            continue
        data.append(_data)
        ans.append(hots[ans_class - 1])
    return np.array(data), np.array(ans)


def init_model():
    print('Compiling Model ... ')
    model = Sequential()
    model.add(Flatten(input_shape=(290, 13)))
    model.add(Dense(units=500, input_dim=3770, activation="relu", kernel_initializer="random_uniform", bias_initializer="zeros"))
    model.add(Dropout(0.2))
    model.add(Dense(units=100, activation="relu"))
    model.add(Dropout(0.3))
    model.add(Dense(units=8, activation="softmax"))

    print(model.summary())
    # model.compile(optimizer='adam', loss ='mean_squared_error', metrics=['accuracy'])
    optimizer = Adam(lr=0.0001)
    model.compile(optimizer=optimizer, loss ='categorical_crossentropy', metrics=['accuracy'])

    return model


def train_eval_model(model):
    X, Y = load_data('LEARN\\')
    X_test, Y_test = load_data('TEST\\')
    print(X.shape)
    # learning_label = pd.DataFrame(learning_dataset[["label"]].copy(deep=False)) # Seperate labels (y) from input
    # learning_input = pd.DataFrame(learning_dataset.drop("label", 1, inplace=False))
    model.fit(X, Y, epochs=100, batch_size=24, verbose=1, validation_data=(X_test, Y_test))
    #   (X_train, y_train), (X_test, y_test) = mnist.load_data()


def eval_model(model):
    X_test, Y_test = load_data('TEST\\')
    loss, metrics = model.evaluate(X_test, Y_test)
    print(f'Loss: {loss}, Accuracy: {metrics}')
    

    # model.predict()
    #  X_train = X_train.astype('float32')
    #  X_test = X_test.astype('float32')


model = init_model()
train_eval_model(model)
# eval_model(model)