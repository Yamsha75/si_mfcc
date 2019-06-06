import os

import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout




def init_model():
    print('Compiling Model ... ')
    model = keras.Sequential()
    model.add(keras.layers.Flatten())
    model.add(keras.layers.Dense(units=1000, input_dim=3770, activation="relu", kernel_initializer="random_uniform", bias_initializer="zeros"))
    model.add(Dropout(0.4))
    model.add(Dense(units=500, activation="relu"))
    model.add(Dropout(0.3))
    model.add(Dense(units=250, activation="relu"))
    model.add(Dropout(0.2))
    model.add(Dense(units=6, activation="softmax"))

    print(model.summary())
    model.compile(optimizer='adam', loss ='mean_squared_error', metrics=['accuracy']) #optimizer="RMSprop"
    learning_label = pd.DataFrame(learning_dataset[["label"]].copy(deep=False)) # Seperate labels (y) from input
    learning_input = pd.DataFrame(learning_dataset.drop("label", 1, inplace=False))
    model.fit(learning_input.as_matrix(), learning_label, epochs=4, batch_size=64)
 #   (X_train, y_train), (X_test, y_test) = mnist.load_data()
    val_loss , val_acc = model.evaluate(x_testing_dataset,y_test)
    
    model.predict()
  #  X_train = X_train.astype('float32')
  #  X_test = X_test.astype('float32')
