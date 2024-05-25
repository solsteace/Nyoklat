import json
import os

import cv2
import numpy as np
from tensorflow.keras.models import model_from_json as tf_load_model

model = None;

def classify(image):
    global model
    if(model == None):
        with open(os.path.join(".", "assets", "config.json"), 'r') as f:
            model_spec = json.load(f)
            model = tf_load_model(json.dumps(model_spec))
            model.load_weights(os.path.join(".", "assets", "model.weights.h5"))

    prediction = model.predict(image)

    highest_certainty = prediction[0][0]
    for jdx in range(len(prediction[0])):
        node_certainty = prediction[0][jdx]
        if(node_certainty > highest_certainty):
            highest_certainty = jdx

    return [f"Class {x + 1}" for x in range(4)][int(highest_certainty)]