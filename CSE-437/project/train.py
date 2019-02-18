#author: Md Mahedi Hasan
#date: 13/02/2019
#description: design and train a model for MNIST dataset recognition

import numpy as np
from keras.models import Sequential
from keras.layers import Conv2D, Dense, Dropout, Flatten, MaxPooling2D

import data_preprocess
import os

# constans variables and paths
model_name = "miu_cnn.json"
weight_name = "miu_cnn.h5"

model_dir = "../model"

model_path = os.path.join(model_dir, model_name)
weight_path = os.path.join(model_dir, weight_name)


# network parameter
nb_epochs = 1
img_rows = 28
img_cols = 28
img_shape = (img_rows, img_cols, 1)
nb_classes = 10

# loading data
X_train, y_train = data_preprocess.process_train_data()
X_train = X_train.reshape(X_train.shape[0], img_rows, img_cols, 1)


# building model 
model = Sequential()
model.add(Conv2D(32, kernel_size=(3,3), activation="relu", input_shape = img_shape))
model.add(Conv2D(64, (3,3), activation="relu"))
model.add(MaxPooling2D(pool_size = (2,2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(128))
model.add(Dropout(0.5))
model.add(Dense(nb_classes, activation="softmax"))

model.summary()


objective = "categorical_crossentropy"
optimizer = "adam"
metrics = ["accuracy"]

model.compile(optimizer = optimizer,
              loss = objective,
              metrics = metrics)

print("Training")

model.fit(X_train, y_train,
          batch_size = 64,
          epochs = nb_epochs,
          verbose = 2,
          validation_split = 0.15)

# saving model
print("Saving model")
json_string = model.to_json()
open(model_path, "w").write(json_string)

# saving weights
model.save_weights(weight_path)