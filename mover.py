from PIL import Image # python3 -m pip install Pillow

import os

downloadsFolder = "/home/mijel/Descargas/"
homeFolder = "/home/mijel/"
imagesFolder = "/home/mijel/Imágenes/"
musicFolder = "/home/mijel/Música/"
documentsFolder = "/home/mijel/Documentos/"
videoFolder = "/home/mijel/Vídeos/"
excelFolder = "excels/"

mp4Extensions = [".mp4", ".avi", ".mov", ".wmv"]

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

        if extension in mp4Extensions:
            os.rename(downloadsFolder + filename, videoFolder + filename)
            
    for filename in os.listdir(homeFolder):
        name, extension = os.path.splitext(homeFolder + filename)

        if extension in [".jpg", ".jpeg", ".png"]:
            picture = Image.open(homeFolder + filename)
            picture.save(imagesFolder + "compressed_"+filename, optimize=True, quality=60)
            os.remove(homeFolder + filename)
            print(name + ": " + extension)

        if extension in [".mp3"]:
            os.rename(homeFolder + filename, musicFolder + filename)

        if extension in [".xlsx", ".xlsm", ".xlsb", ".xltx"]:
            os.rename(homeFolder + filename, documentsFolder + excelFolder + filename)
            
        if extension in [".docx", ".docm", ".dotx", ".dotm", ".pdf"]:
            os.rename(homeFolder + filename, documentsFolder + filename)
        
        if extension in mp4Extensions:
            os.rename(homeFolder + filename, videoFolder + filename)
      


