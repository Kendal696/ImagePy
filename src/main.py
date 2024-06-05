import tkinter as tk
from tkinter import ttk, filedialog, simpledialog
from PIL import Image, ImageTk
import sys
import os

# Añadir el directorio src al sys.path para permitir la importación de módulos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src import image_io, preprocessing, enhancement, transformations, histogram, segmentation, filters

class ImageProcessingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Proyecto Final")

        self.image = None
        self.processed_image = None

        self.style = ttk.Style()
        self.style.configure('TButton', font=('Helvetica', 12))

        self.load_icons()
        self.create_widgets()

        # Bind the configure event to handle window resizing
        self.root.bind('<Configure>', self.on_resize)

    def load_icons(self):
        self.load_icon = self.resize_icon('icons/load_icon.png')
        self.gray_icon = self.resize_icon('icons/gray_icon.png')
        self.negative_icon = self.resize_icon('icons/negative_icon.png')
        self.brightness_icon = self.resize_icon('icons/brightness_icon.png')
        self.contrast_icon = self.resize_icon('icons/contrast_icon.png')
        self.scale_icon = self.resize_icon('icons/scale_icon.png')
        self.rotate_icon = self.resize_icon('icons/rotate_icon.png')
        self.translate_icon = self.resize_icon('icons/translate_icon.png')
        self.refresh_icon = self.resize_icon('icons/refresh_icon.png')

    def resize_icon(self, path, size=(24, 24)):
        icon = Image.open(path)
        icon = icon.resize(size, Image.LANCZOS)
        return ImageTk.PhotoImage(icon)

    def create_widgets(self):
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.canvas_frame = ttk.Frame(self.main_frame)
        self.canvas_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(self.canvas_frame, bg='black')
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.button_frame = ttk.Frame(self.main_frame)
        self.button_frame.pack(side=tk.RIGHT, fill=tk.Y)

        self.load_button = ttk.Button(self.button_frame, text="Cargar Imagen", command=self.load_image, image=self.load_icon, compound=tk.LEFT)
        self.load_button.pack(pady=5)

        self.gray_button = ttk.Button(self.button_frame, text="Convertir a Blanco y Negro", command=self.convert_to_grayscale, image=self.gray_icon, compound=tk.LEFT)
        self.gray_button.pack(pady=5)

        self.negative_button = ttk.Button(self.button_frame, text="Generar Negativo", command=self.generate_negative, image=self.negative_icon, compound=tk.LEFT)
        self.negative_button.pack(pady=5)

        self.histogram_button = ttk.Button(self.button_frame, text="Mostrar Histograma", command=self.plot_histogram)
        self.histogram_button.pack(pady=5)

        self.equalize_button = ttk.Button(self.button_frame, text="Ecualizar Histograma", command=self.equalize_histogram)
        self.equalize_button.pack(pady=5)

        self.kmeans_button = ttk.Button(self.button_frame, text="Segmentar con K-means", command=self.kmeans_segmentation)
        self.kmeans_button.pack(pady=5)

        self.gaussian_button = ttk.Button(self.button_frame, text="Filtro Gaussiano", command=self.gaussian_filter)
        self.gaussian_button.pack(pady=5)

        self.canny_button = ttk.Button(self.button_frame, text="Detección de Bordes (Canny)", command=self.canny_edge_detection)
        self.canny_button.pack(pady=5)

        self.brightness_label = ttk.Label(self.button_frame, text="Ajustar Brillo", image=self.brightness_icon, compound=tk.LEFT)
        self.brightness_label.pack(pady=5)
        self.brightness_slider = ttk.Scale(self.button_frame, from_=0.1, to_=2.0, orient=tk.HORIZONTAL, command=self.adjust_brightness)
        self.brightness_slider.set(1.0)
        self.brightness_slider.pack(pady=5)

        self.contrast_label = ttk.Label(self.button_frame, text="Ajustar Contraste", image=self.contrast_icon, compound=tk.LEFT)
        self.contrast_label.pack(pady=5)
        self.contrast_slider = ttk.Scale(self.button_frame, from_=0.1, to_=2.0, orient=tk.HORIZONTAL, command=self.adjust_contrast)
        self.contrast_slider.set(1.0)
        self.contrast_slider.pack(pady=5)

        self.scale_button = ttk.Button(self.button_frame, text="Escalar Imagen", command=self.scale_image, image=self.scale_icon, compound=tk.LEFT)
        self.scale_button.pack(pady=5)

        self.rotate_button = ttk.Button(self.button_frame, text="Rotar Imagen", command=self.rotate_image, image=self.rotate_icon, compound=tk.LEFT)
        self.rotate_button.pack(pady=5)

        self.translate_button = ttk.Button(self.button_frame, text="Trasladar Imagen", command=self.translate_image, image=self.translate_icon, compound=tk.LEFT)
        self.translate_button.pack(pady=5)

        self.refresh_button = ttk.Button(self.button_frame, text="Refrescar Imagen", command=self.refresh_image, image=self.refresh_icon, compound=tk.LEFT)
        self.refresh_button.pack(pady=5)

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

    def refresh_image(self):
        if self.image is not None:
            self.processed_image = self.image
            self.show_image(self.image)

    def plot_histogram(self):
        if self.image is not None:
            histogram.plot_histogram(self.image)

    def equalize_histogram(self):
        if self.image is not None:
            self.processed_image = histogram.equalize_histogram(self.image)
            self.show_image(self.processed_image)

    def kmeans_segmentation(self):
        if self.image is not None:
            self.processed_image = segmentation.kmeans_segmentation(self.image)
            self.show_image(self.processed_image)

    def gaussian_filter(self):
        if self.image is not None:
            self.processed_image = filters.gaussian_filter(self.image)
            self.show_image(self.processed_image)

    def canny_edge_detection(self):
        if self.image is not None:
            self.processed_image = filters.canny_edge_detection(self.image, 100, 200)
            self.show_image(self.processed_image)

    def show_image(self, image, cmap=None):
        self.canvas.delete("all")  # Clear the canvas
        if cmap == 'gray':
            image = Image.fromarray(image).convert('L')
        else:
            image = Image.fromarray(image)

        # Resize the image to fit the canvas while keeping aspect ratio
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        image.thumbnail((canvas_width, canvas_height), Image.LANCZOS)

        imgtk = ImageTk.PhotoImage(image=image)
        self.canvas.create_image(canvas_width // 2, canvas_height // 2, anchor=tk.CENTER, image=imgtk)
        self.canvas.image = imgtk  # Keep a reference to avoid garbage collection

    def on_resize(self, event):
        if self.processed_image is not None:
            self.show_image(self.processed_image)

def main():
    root = tk.Tk()
    root.state('zoomed')  # Set window to maximized state
    app = ImageProcessingApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
