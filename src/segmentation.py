import numpy as np
import cv2

def kmeans_segmentation(image, K=2):
    """Segmenta una imagen utilizando K-means clustering."""
    Z = image.reshape((-1, 3))
    Z = np.float32(Z)

    # Definir criterios, número de clusters(K) y aplicar K-means
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    ret, label, center = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    # Convertir de nuevo a uint8, y hacer la imagen resultante
    center = np.uint8(center)
    res = center[label.flatten()]
    return res.reshape((image.shape))
