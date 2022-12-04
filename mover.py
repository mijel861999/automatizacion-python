from PIL import Image # python3 -m pip install Pillow

import os

downloadsFolder = "/home/mijel/Descargas/"
imagesFolder = "/home/mijel/Imágenes/"
musicFolder = "/home/mijel/Música/"
documentsFolder = "/home/mijel/Documentos/"
excelFolder = "excels/"

if __name__ == "__main__":
    for filename in os.listdir(downloadsFolder):
        name, extension = os.path.splitext(downloadsFolder + filename)

        if extension in [".jpg", ".jpeg", ".png"]:
            picture = Image.open(downloadsFolder + filename)
            picture.save(imagesFolder + "compressed_"+filename, optimize=True, quality=60)
            os.remove(downloadsFolder + filename)
            print(name + ": " + extension)

        if extension in [".mp3"]:
            os.rename(downloadsFolder + filename, musicFolder + filename)

        if extension in [".xlsx", ".xlsm", ".xlsb", ".xltx"]:
            os.rename(downloadsFolder + filename, documentsFolder + excelFolder + filename)
            
        if extension in [".docx", ".docm", ".dotx", ".dotm", ".pdf"]:
            os.rename(downloadsFolder + filename, documentsFolder + filename)
            


