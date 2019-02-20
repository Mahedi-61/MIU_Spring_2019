#Author: Md Mahedi Hasan
#Date: 13/02/2019
#Description: file for testing our model in MNIST dataset


import numpy as np
import pandas as pd
import os

import data_preprocess
from keras.models import model_from_json 

batch_size = 64
img_rows = 28
img_cols = 28

nb_test_images = 28000

def submit_result(result, value):
    submit_df = pd.DataFrame({"ImageId" : range(1 , value+1), "Lable": result})
    submit_df.to_csv(output_path, header = True, index = False)


# constans variables and paths
model_name = "miu_cnn.json"
weight_name = "miu_cnn.h5"
output_file = "submission1.csv"

model_dir = "../model"
output_dir = "../submission/"

model_path = os.path.join(model_dir, model_name)
weight_path = os.path.join(model_dir, weight_name)
output_path = os.path.join(output_dir, output_file)

# load test data
X_test = data_preprocess.preprocess_test_data()
X_test = X_test.reshape(X_test.shape[0], img_rows, img_cols, 1)

# model build
json_string = open(model_path).read()
model = model_from_json(json_string)
model.load_weights(weight_path)


# prediction
predictions = model.predict(X_test,
                            batch_size = 64,
                            verbose = 2)

result = np.argmax(predictions, axis = 1)

# make the csv file to upload in Kaggle
submit_result(result, nb_test_images)