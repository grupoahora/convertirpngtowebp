import os
from PIL import Image

# Pedir la ruta de la carpeta de entrada (imágenes PNG o JPG)
directorio_png_jpg = input("Ingrese la ruta de la carpeta de imágenes PNG o JPG: ")

# Pedir la ruta de la carpeta de salida (imágenes WebP)
directorio_webp = input("Ingrese la ruta de la carpeta de salida para las imágenes WebP: ")

# Lista todos los archivos en el directorio PNG/JPG
archivos_png_jpg = os.listdir(directorio_png_jpg)

# Itera sobre los archivos PNG/JPG y conviértelos a WebP
for archivo in archivos_png_jpg:
    ruta_completa_png_jpg = os.path.join(directorio_png_jpg, archivo)
    ruta_completa_webp = os.path.join(directorio_webp, os.path.splitext(archivo)[0] + ".webp")

    # Abre el archivo PNG/JPG y guarda como WebP
    imagen = Image.open(ruta_completa_png_jpg)
    imagen.save(ruta_completa_webp, "WEBP")

print("La conversión se ha completado. Las imágenes se han guardado en la carpeta especificada.")
