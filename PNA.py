# coding=utf-8
import PIL.Image as Image
import os

PHOTO_FILE = r'512'

def fixed_size(file, width=512, height=512):
    """按照固定尺寸处理图片"""
    im = Image.open(file)
    out = im.resize((width, height),Image.ANTIALIAS)
    out.save(file)

def executeCompressImage():      #  执行图片的缩放

    for r, d, f in os.walk(PHOTO_FILE):
        for file in f:
           path = os.path.join(r, file)
           print(path)
           fixed_size(path)     #   默认修改为高=800像素，宽=600像素

while True:
    print("ok")
    executeCompressImage()