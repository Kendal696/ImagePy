# src/image_io.py

from PIL import Image
import numpy as np

def load_image(image_path):
    """Carga una imagen desde el archivo especificado."""
    image = Image.open(image_path)
    return np.array(image)

def save_image(image, save_path):
    """Guarda la imagen en el archivo especificado."""
    im = Image.fromarray(image)
    im.save(save_path)
