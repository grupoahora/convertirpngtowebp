import os
from tkinter import Tk, Label, Button, filedialog
from PIL import Image

class ConvertidorImagenes:
    def __init__(self, root):
        self.root = root
        self.root.title("Convertidor de Imágenes")
        self.label = Label(root, text="Seleccione la carpeta de imágenes PNG o JPG:")
        self.label.pack()
        self.btn_seleccionar = Button(root, text="Seleccionar Carpeta", command=self.seleccionar_carpeta)
        self.btn_seleccionar.pack()
        self.directorio_png_jpg = ""
        self.directorio_webp = ""

    def seleccionar_carpeta(self):
        self.directorio_png_jpg = filedialog.askdirectory()
        self.label.config(text=f"Ruta de la carpeta seleccionada: {self.directorio_png_jpg}")
        self.btn_convertir = Button(self.root, text="Convertir Imágenes", command=self.convertir_imagenes)
        self.btn_convertir.pack()

    def convertir_imagenes(self):
        self.directorio_webp = filedialog.askdirectory()
        archivos_png_jpg = os.listdir(self.directorio_png_jpg)
        for archivo in archivos_png_jpg:
            ruta_completa_png_jpg = os.path.join(self.directorio_png_jpg, archivo)
            ruta_completa_webp = os.path.join(self.directorio_webp, os.path.splitext(archivo)[0] + ".webp")
            imagen = Image.open(ruta_completa_png_jpg)
            imagen.save(ruta_completa_webp, "WEBP")
        self.label.config(text="La conversión se ha completado. Las imágenes se han guardado en la carpeta especificada.")

root = Tk()
app = ConvertidorImagenes(root)
root.mainloop()
