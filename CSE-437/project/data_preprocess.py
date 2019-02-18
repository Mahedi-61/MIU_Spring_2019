#author: Md Mahedi Hasan
#date: 12/02/2019
#description: data preprocess for MNIST dataset

import numpy as np 
import pandas as pd 
import cv2 
import matplotlib.pyplot as plt 
import keras
from keras.utils  import np_utils

data_dir = "../data/"
submission_dir = "../submission/"

train_file = "train.csv"
test_file = "test.csv"
output_file = "sumission_1.csv"

num_train_data = 42000
num_test_data = 28000
nb_classes = 10


# loading train data
def load_train_data():
    train_data = pd.read_csv(data_dir + train_file)
    
    X_train = train_data.ix[:, 1:].values
    y_train = train_data.ix[:, 0].values

    del train_data
    X_train.astype(np.float32)
    y_train.astype(np.int32)

    return X_train, y_train


# loading test data
def preprocess_test_data():
    test_data = pd.read_csv(data_dir + test_file)
    X_test = test_data.values
    X_test.astype(np.float32)

    del test_data
    return normalization(X_test)
    

# normalizing data
def normalization(X):
    scale = np.max(X)
    X = X /scale
    return X


# processing train data
def process_train_data():
    X_train, y_train = load_train_data()
    X_train = normalization(X_train)

    # one hot encoding
    y_train = np_utils.to_categorical(y_train, nb_classes)

    return X_train, y_train


# display the image
def show_image(img):
    cv2.imshow("image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()