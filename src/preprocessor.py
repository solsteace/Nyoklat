import numpy as np
import cv2

def preprocess(raw_image: bytes):
    image = cv2.imdecode(
        np.fromstring(raw_image, np.uint8),
        cv2.IMREAD_COLOR
    )

    image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

    return image;
