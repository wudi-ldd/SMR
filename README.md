## Research on Image Identification Method of Rock Thin Slices in Tight Oil Reservoirs Based on Mask R-CNN

---

### Catalogue
1. [Environment](#Environment)
2. [Explain](#Explain)
3. [How2train](#How2train)
4. [Result](#Result)

### Environment
Python 3.6

tensorflow-gpu 1.15.0

### Explain
config.py This file contains the default configuration,allows you to subclass it and modify the properties you need to change.

dataset.py This file provides a consistent way to process any data set.It allows you to train with new datasets without changing the code of the model.It also supports loading multiple datasets at the same time, which is very useful if the objects you want to detect are not all available in one dataset.

PNA.py To support multiple images for each batch of training, we adjusted all images to 512*512.

NLMWGC.py Removing original image noise using nonlocal mean filtering.

augment.py The training image is augmented with labels, mainly including rotation, noise, salt and pepper, brightness adjustment and other operations.

labelme2COCO.py Convert JSON file to coco format training image.

train.py Run train.py for training.

predict.py Run predict.py to predict after training

### How2train
#### 1、Prepare dataset
a、Label the dataset with labelme. Note that the same class should use different serial numbers when labeling,For example, there are **two quartz in the picture. One is quartz1 and the other is quartz2.**    
b、After annotation, put the JPG file and JSON file in before under the root directory.  
c、Then run JSON_ to_ dataset. Py to generate a train_ Dataset folder.

#### 2、Modify training parameters
a、dataset.py Modify the classes you want to classify, which are load_ Shapes function and load_ The contents related to classes in the mask function, that is, the original circle, square, etc. are modified into their own classes.   
b、Modify the contents of shapesconfig (config) under the train folder, num_ Class is equal to the number of classes you want to divide +1.  
c、IMAGE_MAX_DIM、IMAGE_MIN_DIM、BATCH_SIZE和IMAGES_PER_GPU modify according to your own video memory。RPN_ ANCHOR_ Scales according to image_ MAX_ Dim and image_ MIN_ Dim.  
d、STEPS_ PER_ Epoch represents how many times each generation trains.  

#### 3、Train

Run train.py for training

#### 4、predict
Run predict.py for prediction

### Identification results
![1655291063095](C:\Users\DMIS-ldd\AppData\Roaming\Typora\typora-user-images\1655291063095.png)

​                                                                                            Original drawing

![1655291091552](C:\Users\DMIS-ldd\AppData\Roaming\Typora\typora-user-images\1655291091552.png)

​                                                                                       Identification results
For convenience of observation, we modified visualize.py, remove the identification box, modify the font size of the identification label, and center it.
