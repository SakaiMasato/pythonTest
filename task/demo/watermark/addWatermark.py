import os
from PIL import Image

global watermarkIm
files = os.listdir(os.path.abspath('img'))
for fileName in files:
    try:
        if fileName.index('.jpg'):
            url = os.path.join(os.path.abspath('img'), fileName)
            img = Image.open(url)
            width, height = img.size
            img.paste(watermarkIm, (width-50,height-50),watermarkIm)
            img.save(os.path.join(os.path.abspath('img'),'withlogo.jpg'))
    except ValueError as e:
        if fileName.index('.png'):
            url = os.path.join(os.path.abspath('img'),fileName)
            img = Image.open(url)
            watermarkIm = img.resize((50,50))