import numpy as np
import matplotlib.pyplot as plt
import cv2

def plot_histogram(image):
    """Muestra el histograma de una imagen."""
    if len(image.shape) == 3 and image.shape[2] == 3:
        color = ('r', 'g', 'b')
        for i, col in enumerate(color):
            histr = cv2.calcHist([image], [i], None, [256], [0, 256])
            plt.plot(histr, color=col)
            plt.xlim([0, 256])
    else:
        plt.hist(image.ravel(), 256, [0, 256])
    plt.show()

def equalize_histogram(image):
    """Ecualiza el histograma de una imagen."""
    if len(image.shape) == 2:
        return cv2.equalizeHist(image)
    elif len(image.shape) == 3 and image.shape[2] == 3:
        img_yuv = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
        img_yuv[:, :, 0] = cv2.equalizeHist(img_yuv[:, :, 0])
        return cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)
    return image
