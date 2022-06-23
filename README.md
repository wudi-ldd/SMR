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

PNA.py 为了支持每批训练多个图像，我们将所有图像调整为![img](file:///C:/Users/DMIS-ldd/AppData/Local/Temp/msohtmlclip1/01/clip_image002.gif)大小。

NLMWGC.py 使用非局部均值滤波去除原始图像噪声。

augment.py 实现训练图像带标签的增广，主要包括旋转、噪声、椒盐、亮度调整等操作。

labelme2COCO.py 将json文件转换为COCO格式的训练图像

train.py 运行train.py进行训练

predict.py 训练完成后运行predict进行预测

### 训练步骤
#### 1、准备数据集
a、利用labelme标注数据集，注意标注的时候同一个类要用不同的序号，比如画面中存在**两个苹果那么一个苹果的label就是apple1另一个是apple2。**    
b、标注完成后将jpg文件和json文件放在根目录下的before里面。  
c、之后运行json_to_dataset.py就可以生成train_dataset文件夹了。  

#### 2、修改训练参数
a、dataset.py内修改自己要分的类，分别是load_shapes函数和load_mask函数内和类有关的内容，即将原有的circle、square等修改成自己要分的类。    
b、在train文件夹下面修改ShapesConfig(Config)的内容，NUM_CLASS等于自己要分的类的数量+1。  
c、IMAGE_MAX_DIM、IMAGE_MIN_DIM、BATCH_SIZE和IMAGES_PER_GPU根据自己的显存情况修改。RPN_ANCHOR_SCALES根据IMAGE_MAX_DIM和IMAGE_MIN_DIM进行修改。  
d、STEPS_PER_EPOCH代表每个世代训练多少次。   

#### 3、训练

运行train.py进行训练

#### 4、预测
训练完成后运行predict.py进行预测  

### 识别结果

![1655291063095](C:\Users\DMIS-ldd\AppData\Roaming\Typora\typora-user-images\1655291063095.png)

​                                                                                            原图

![1655291091552](C:\Users\DMIS-ldd\AppData\Roaming\Typora\typora-user-images\1655291091552.png)

​                                                                                        识别结果

  为方便观察，我们修改了visualize.py的检测方式，去除识别框，修改识别标签字体的大小，并使其居中。
