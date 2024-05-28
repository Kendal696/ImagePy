# src/enhancement.py

import numpy as np

def adjust_brightness(image, factor):
    """Ajusta el brillo de una imagen multiplicando los valores de los píxeles por el factor dado."""
    return np.clip(image * factor, 0, 255).astype(np.uint8)

def adjust_contrast(image, factor):
    """Ajusta el contraste de una imagen usando el factor dado."""
    mean = np.mean(image, axis=(0, 1), keepdims=True)
    return np.clip((image - mean) * factor + mean, 0, 255).astype(np.uint8)
