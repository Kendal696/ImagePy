# src/transformations.py

import numpy as np
from PIL import Image

def scale_image(image, factor):
    """Escala una imagen por el factor dado."""
    img = Image.fromarray(image)
    new_size = (int(img.width * factor), int(img.height * factor))
    return np.array(img.resize(new_size, Image.ANTIALIAS))

def rotate_image(image, angle):
    """Rota una imagen por el ángulo dado."""
    img = Image.fromarray(image)
    return np.array(img.rotate(angle, expand=True))

def translate_image(image, tx, ty):
    """Traduce una imagen por los valores tx y ty dados."""
    img = Image.fromarray(image)
    translated_image = Image.new("RGB", img.size)
    translated_image.paste(img, (tx, ty))
    return np.array(translated_image)
