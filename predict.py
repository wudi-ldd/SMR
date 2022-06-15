from keras.layers import Input
from mask_rcnn import MASK_RCNN 
from PIL import Image
import datetime
mask_rcnn = MASK_RCNN()
while True:
    img = input('Input image filename:')
    starttime = datetime.datetime.now()
    try:
        image = Image.open(img)
    except:
        print('Open Error! Try again!')
        continue
    else:
        image = mask_rcnn.detect_image(image)
        image.show()
        endtime = datetime.datetime.now()
        print(endtime - starttime).seconds
mask_rcnn.close_session()
    