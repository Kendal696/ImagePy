# src/main.py

import tkinter as tk
from tkinter import filedialog, simpledialog
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
import sys
import os

# Añadir el directorio src al sys.path para permitir la importación de módulos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src import image_io, preprocessing, enhancement, transformations

class ImageProcessingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Proyecto Final")

        self.image = None
        self.processed_image = None

        self.create_widgets()

    def create_widgets(self):
        self.canvas = tk.Canvas(self.root, width=600, height=400, bg='black')
        self.canvas.pack()

        self.load_button = tk.Button(self.root, text="Cargar Imagen", command=self.load_image)
        self.load_button.pack()

        self.gray_button = tk.Button(self.root, text="Convertir a Blanco y Negro", command=self.convert_to_grayscale)
        self.gray_button.pack()

        self.negative_button = tk.Button(self.root, text="Generar Negativo", command=self.generate_negative)
        self.negative_button.pack()

        self.brightness_label = tk.Label(self.root, text="Ajustar Brillo")
        self.brightness_label.pack()
        self.brightness_slider = tk.Scale(self.root, from_=0.1, to_=2.0, orient=tk.HORIZONTAL, resolution=0.1, command=self.adjust_brightness)
        self.brightness_slider.set(1.0)
        self.brightness_slider.pack()

        self.contrast_label = tk.Label(self.root, text="Ajustar Contraste")
        self.contrast_label.pack()
        self.contrast_slider = tk.Scale(self.root, from_=0.1, to_=2.0, orient=tk.HORIZONTAL, resolution=0.1, command=self.adjust_contrast)
        self.contrast_slider.set(1.0)
        self.contrast_slider.pack()

        self.scale_button = tk.Button(self.root, text="Escalar Imagen", command=self.scale_image)
        self.scale_button.pack()

        self.rotate_button = tk.Button(self.root, text="Rotar Imagen", command=self.rotate_image)
        self.rotate_button.pack()

        self.translate_button = tk.Button(self.root, text="Trasladar Imagen", command=self.translate_image)
        self.translate_button.pack()

    def load_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image = image_io.load_image(file_path)
            self.processed_image = self.image
            self.show_image(self.image)

    def convert_to_grayscale(self):
        if self.image is not None:
            self.processed_image = preprocessing.convert_to_grayscale(self.image)
            self.show_image(self.processed_image, cmap='gray')

    def generate_negative(self):
        if self.image is not None:
            self.processed_image = preprocessing.generate_negative(self.image)
            self.show_image(self.processed_image)

    def adjust_brightness(self, value):
        if self.image is not None:
            factor = float(value)
            self.processed_image = enhancement.adjust_brightness(self.image, factor)
            self.show_image(self.processed_image)

    def adjust_contrast(self, value):
        if self.image is not None:
            factor = float(value)
            self.processed_image = enhancement.adjust_contrast(self.image, factor)
            self.show_image(self.processed_image)

    def scale_image(self):
        if self.image is not None:
            factor = simpledialog.askfloat("Escalar Imagen", "Ingrese el factor de escala (por ejemplo, 0.5 para reducir a la mitad):")
            if factor:
                self.processed_image = transformations.scale_image(self.image, factor)
                self.show_image(self.processed_image)

    def rotate_image(self):
        if self.image is not None:
            angle = simpledialog.askfloat("Rotar Imagen", "Ingrese el ángulo de rotación (por ejemplo, 45 para 45 grados):")
            if angle:
                self.processed_image = transformations.rotate_image(self.image, angle)
                self.show_image(self.processed_image)

    def translate_image(self):
        if self.image is not None:
            tx = simpledialog.askinteger("Trasladar Imagen", "Ingrese la traslación en x (por ejemplo, 50 para 50 píxeles):")
            ty = simpledialog.askinteger("Trasladar Imagen", "Ingrese la traslación en y (por ejemplo, 50 para 50 píxeles):")
            if tx is not None and ty is not None:
                self.processed_image = transformations.translate_image(self.image, tx, ty)
                self.show_image(self.processed_image)

    def show_image(self, image, cmap=None):
        self.canvas.delete("all")  # Clear the canvas
        if cmap == 'gray':
            image = Image.fromarray(image).convert('L')
        else:
            image = Image.fromarray(image)

        imgtk = ImageTk.PhotoImage(image=image)
        self.canvas.create_image(300, 200, anchor=tk.CENTER, image=imgtk)
        self.canvas.image = imgtk  # Keep a reference to avoid garbage collection

def main():
    root = tk.Tk()
    app = ImageProcessingApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()