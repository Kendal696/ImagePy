# src/preprocessing.py

import numpy as np

def convert_to_grayscale(image):
    """Convierte una imagen a blanco y negro."""
    if len(image.shape) == 3 and image.shape[2] == 3:
        return np.dot(image[...,:3], [0.2989, 0.5870, 0.1140]).astype(np.uint8)
    else:
        return image

def generate_negative(image):
    """Genera la imagen negativa."""
    return 255 - image
