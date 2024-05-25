import numpy as np
import cv2

def preprocess(raw_image: bytes):
    image = cv2.imdecode(
        np.fromstring(raw_image, np.uint8),
        cv2.IMREAD_COLOR
    )

    image = cv2.resize( image, (224, 224))

    # cv2.imwrite("./res.png", image)
    image = np.expand_dims(image, axis=0);
    return image
