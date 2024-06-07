import cv2

def gaussian_filter(image, kernel_size=(5, 5), sigma=1):
    """Aplica un filtro Gaussiano a una imagen."""
    return cv2.GaussianBlur(image, kernel_size, sigma)

def canny_edge_detection(image, threshold1, threshold2):
    """Aplica detección de bordes con el algoritmo de Canny."""
    return cv2.Canny(image, threshold1, threshold2)
