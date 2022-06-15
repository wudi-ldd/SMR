from PIL import Image

im = Image.open("181.jpg")
print(im.getbands())

