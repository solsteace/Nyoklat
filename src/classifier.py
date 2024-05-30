import json
import os

import cv2
import numpy as np
from tensorflow.keras.models import model_from_json as tf_load_model

model = None;

def init_model():
    global model
    if(model == None):
        with open(os.path.join(".", "assets", "config.json"), 'r') as f:
            model_spec = json.load(f)
            model = tf_load_model(json.dumps(model_spec))
            model.load_weights(os.path.join(".", "assets", "model.weights.h5"))

def classify(image):
    init_model()
    prediction = model.predict(image)
    prediction = np.argmax(prediction[0])

    return ( 
        f"Class {prediction + 1}: Stage {prediction + 1} ({prediction*2}-{(prediction + 1)*2} months)" if prediction != 3
        else "Class 4: harvest stage (>6 months)"
    )