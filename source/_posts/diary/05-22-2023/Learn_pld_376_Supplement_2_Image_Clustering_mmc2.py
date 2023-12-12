# -*- coding: utf-8 -*-
# os.environ["CUDA_VISIBLE_DEVICES"] = "2"


import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import pandas as pd
import os
from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

####################### 1, Fine tune ###################################

import random
import shutil
pathori = "/home/junru/data/mangchun/fine_tune/dataset"  #path for mor than 10
pathvali = "/home/junru/data/mangchun/fine_tune/validation" #path for validate set
pathtrain = "/home/junru/data/mangchun/fine_tune/train" # path for train set

modelSpList = [ 'Closterotomus_norvegicus_M_AMN' , 'Alloeonotus_fulvipes_M_ZISP_EN' , 'Epimecellus_cyllecorides_M_ZISP_EN' , 'Brachycoleus_decolor_M_ZISP_EN' ,   'Mermitelocerus_schmidtii_M_AMN' ,  'Closterotomus_biclavatus_M_ZISP_EN' , 'Odontoplatis_suturalis_M_ZISP_EN' ,  'Closterotomus_fulvomaculatus_M_AMN' , 'Stenotus_binotatus_M_ZISP_EN'  ]

# 从数据集中随机抽3：1的数据构建测试、训练集
for i in modelSpList:
    pathvalinow = os.path.join(pathvali, i) # 遍历物种名称列表，检索某集中是否存在，如不存在创建文件夹
    if not os.path.exists(pathvalinow):
        os.mkdir(pathvalinow)
    pathtrainnow = os.path.join(pathtrain, i)
    if not os.path.exists(pathtrainnow):
        os.mkdir(pathtrainnow)
    pathnow = os.path.join(pathori, i) # 检查最初数据集里是否包含所有物种 
    listtemp = os.listdir(pathnow) # listtemp存储每个物种所有照片名录列表
    random.shuffle(listtemp)    
    length = len(listtemp) # 随机打乱并计算长度
    valiSelect = listtemp[:length // 4] # 选定测试集并移动到测试集目录
    for valiname in valiSelect:
        shutil.copyfile(os.path.join(pathnow, valiname), os.path.join(pathvalinow, valiname))
    trainSelect = listtemp[length // 4:] # 选定训练集并移动到训练集目录
    for trainname in trainSelect:
        shutil.copyfile(os.path.join(pathnow, trainname), os.path.join(pathtrainnow, trainname))

train_dir = "/home/junru/data/mangchun/fine_tune/train" # path for train set
valid_dir = "/home/junru/data/mangchun/fine_tune/validation" # path for train set
# label_file = "/home/junru/data/mangchun/fine_tune/labels.txt" # path for train set
print(os.path.exists(train_dir))
print(os.path.exists(valid_dir))
# print(os.path.exists(label_file))

print(os.listdir(train_dir))
print(os.listdir(valid_dir))

# labels = pd.read_csv(label_file, header = 0)

def plot_learning_curves(history, label, epochs, min_value, max_value):
    data = {}
    data[label] = history.history[label]
    data["val_" + label] = history.history["val_" + label]
    pd.DataFrame(data).plot(figsize = (8,5))
    plt.grid(True)
    plt.axis([0, epochs, min_value, max_value])
    plt.show()


# Resnet50
height = 224
width = 224
channels = 3
batch_size = 24 
num_classes = 9  # 此处应该与类数量保持一致，用lenth获取或许更好
# augmentations are strongly recommended for fine-tuning of models
train_datagen = keras.preprocessing.image.ImageDataGenerator(
    preprocessing_function = keras.applications.resnet50.preprocess_input, 
    rotation_range = 40,
    width_shift_range = 0.2, 
    height_shift_range = 0.2,
    shear_range = 0.2,
    zoom_range = 0.2,
    horizontal_flip = True,
    fill_mode = "nearest", 
)
train_generator = train_datagen.flow_from_directory(
    train_dir, 
    target_size = (height, width),
    batch_size = batch_size, 
    seed = 7,
    shuffle = True,
    class_mode = "categorical") 
valid_datagen = keras.preprocessing.image.ImageDataGenerator(preprocessing_function = keras.applications.resnet50.preprocess_input)
valid_generator = valid_datagen.flow_from_directory(
    valid_dir, 
    target_size = (height, width),
    batch_size = batch_size,
    seed = 7,
    shuffle = False,
    class_mode = "categorical")
train_num = train_generator.samples
valid_num = valid_generator.samples
resnet50 = keras.applications.ResNet50(include_top = False, pooling = "avg", weights = "imagenet")
for layer in resnet50.layers[0:-5]:
    layer.trainable = False
x = resnet50.output
x = keras.layers.Dense(num_classes, activation="softmax")(x)
resnet50_new = keras.models.Model(inputs=resnet50.input, outputs=x)
resnet50_new.compile(loss = "categorical_crossentropy", optimizer = "sgd", metrics = ["accuracy"])
resnet50_new.summary()
epochs = 30
# 注意：此处要求origin，validation，train三个目录下目录数量一直，即类的数量一致
# 同时要注意文件是否存在损坏，可以使用ffmpeg统一转换格式之后再进行该步骤。
history = resnet50_new.fit(train_generator, steps_per_epoch = train_num // batch_size, epochs = epochs,
                           validation_data = valid_generator, validation_steps = valid_num // batch_size)
plot_learning_curves(history, "accuracy", epochs, 0, 1.2)
plot_learning_curves(history, "loss", epochs, 0, 2.5)
resnet50_new.save_weights(os.path.join("/home/junru/data/mangchun/fine_tune", "fine-tune-resnet50NN.h5"))



# InceptionResnetV2

height = 299 
width = 299
channels = 3
batch_size = 24 
num_classes = 9 # same to above 
train_datagen = keras.preprocessing.image.ImageDataGenerator(
    preprocessing_function = keras.applications.inception_resnet_v2.preprocess_input, 
    rotation_range = 40, 
    width_shift_range = 0.2, 
    height_shift_range = 0.2, 
    shear_range = 0.2,
    zoom_range = 0.2,
    horizontal_flip = True, 
    fill_mode = "nearest", 
)
train_generator = train_datagen.flow_from_directory(
    train_dir, 
    target_size = (height, width),
    batch_size = batch_size,
    seed = 7,
    shuffle = True,
    class_mode = "categorical")
valid_datagen = keras.preprocessing.image.ImageDataGenerator(
    preprocessing_function = keras.applications.inception_resnet_v2.preprocess_input)
valid_generator = valid_datagen.flow_from_directory(
    valid_dir, 
    target_size = (height, width),
    batch_size = batch_size,
    seed = 7,
    shuffle = False,
    class_mode = "categorical")
train_num = train_generator.samples
valid_num = valid_generator.samples

inceptionResnetV2 = keras.applications.InceptionResNetV2(include_top = False, pooling = "avg", weights = "imagenet")
for layer in inceptionResnetV2.layers[0:500]: 
    layer.trainable = False

x = inceptionResnetV2.output
x = keras.layers.Dense(num_classes, activation="softmax")(x)
inceptionResnetV2_new = keras.models.Model(
    inputs=inceptionResnetV2.input, outputs=x)
inceptionResnetV2_new.compile(loss = "categorical_crossentropy", 
                              optimizer = "sgd", metrics = ["accuracy"])
inceptionResnetV2_new.summary()
epochs = 30
history = inceptionResnetV2_new.fit(train_generator, steps_per_epoch = train_num // batch_size, epochs = epochs,
                           validation_data = valid_generator, validation_steps = valid_num // batch_size)
inceptionResnetV2_new.save_weights(os.path.join("/home/junru/data/mangchun/fine_tune", "fine-tune-inceptionResnetV2N.h5"))
plot_learning_curves(history, "accuracy", epochs, 0, 1.2)
plot_learning_curves(history, "loss", epochs, 0, 2.5)

################################ 2, image clustering #######################################


# from keras.preprocessing import image
from keras.utils import image_utils as image

from keras.applications.inception_resnet_v2 import InceptionResNetV2, preprocess_input
image.LOAD_TRUNCATED_IMAGES = True
model = InceptionResNetV2(weights='imagenet', pooling='max', include_top=False)
model.load_weights(r"/home/junru/data/mangchun/fine_tune/fine-tune-inceptionResnetV2N.h5",by_name=True)

# from keras.applications.resnet import ResNet50,preprocess_input
# image.LOAD_TRUNCATED_IMAGES = True
# model = ResNet50(weights='imagenet', pooling='max', include_top=False) # include_top=False means full connection layers were not used here
# model.load_weights(r"E:\corybasDistri\Corybas\secondAnalysis\fine_tune\fine-tune-resnet50NN.h5",by_name=True)


import numpy as np
import math
import os
import time
import random
from operator import itemgetter



def get_image_feature(picpath):
    if picpath in picDic:
        featurelist = picDic[picpath]
    else:
        img = image.load_img(picpath, target_size=(299, 299))
        img_data = image.img_to_array(img)
        img_data = np.expand_dims(img_data, axis=0)
        img_data = preprocess_input(img_data)
        features = np.array(model.predict(img_data))
        featurelist = (features.flatten())
        picDic[picpath] = featurelist
    return featurelist

def calculate_distance(x, y):
    distance = 0.0
    for a,b in zip(x, y):
        distance += math.pow(a-b, 2)
    return math.sqrt(distance)



def oneCluster(unClusterList, taxaList, voteTimes):
    oneDistanceMatrix = []
    for i in range(len(unClusterList)):
        for j in range(i+1, len(unClusterList)):
            distance = 0.0
            for _ in range(voteTimes):
                featureX = get_image_feature(random.choice(unClusterList[i]))
                featureY = get_image_feature(random.choice(unClusterList[j]))
                distance += calculate_distance(featureX, featureY)
            x = taxaList[i]
            y = taxaList[j]
            if ":" not in taxaList[i]:
                x = taxaDic[x]
            if ":" not in taxaList[j]:
                y = taxaDic[y]
            oneDistanceMatrix.append([(x,y), distance/voteTimes, (i,j)])
    sort_d = sorted(oneDistanceMatrix, key=itemgetter(1))
    return sort_d[0]

def calculate_resDistance(clade, d):
    dRes = d/2
    if ":" not in clade:
        return dRes
    else:
        k = True
        while k:
            index = clade.rfind(":")
            if clade[index -1] != ")": # 从最右端开始找，如果冒号前面没有右括号，那么就到头了Start from right untill there is no right bracket in front of the colon
                k = False
            dRes = dRes - float(clade[index+1:-1])
            clade = clade[:index]
    return dRes

def mainOperater(taxaList, voteTimes):
    unClusterList = []
    for i in taxaList:
        picList = os.listdir(i)
        inameList = []
        for j in picList:
            inameList.append(i + "/" + j)
        unClusterList.append(inameList)
    while len(unClusterList) > 1:
        # 获得一个簇，并将簇里的图片路径列表合并
        # Get a cluster and merge the image path list in the cluster
        thisCluster = oneCluster(unClusterList, taxaList, voteTimes)
        unClusterList[thisCluster[2][0]].extend(unClusterList[thisCluster[2][1]])
        unClusterList.pop(thisCluster[2][1])
        d1 = calculate_resDistance(taxaList[thisCluster[2][0]],thisCluster[1])
        d2 = calculate_resDistance(taxaList[thisCluster[2][1]],thisCluster[1])
        taxaList[thisCluster[2][0]] = "(" + thisCluster[0][0]+":" + str(d1) + "," + thisCluster[0][1] + ":" + str(d2) + ")"
        taxaList.pop(thisCluster[2][1])
    return taxaList[0]


os.chdir(r"dataset") 
global taxaDic
taxaList = os.listdir()
taxaDic = {}
head = "#NEXUS\n\nBegin taxa;\n\tDimensions ntax=" + str(len(taxaList)) + ";\n\t\tTaxlabels"
for taxa in taxaList:
    head = head + "\n\t\t\t" + taxa.replace(" ", "_")
head = head + "\n\t\t\t;\nEnd;\nBegin trees;\n\tTranslate"
taxaCode = 0
for taxa in taxaList:
    taxaCode += 1
    taxaDic[taxa] = str(taxaCode)
    head = head + "\n\t\t" + " "*(4-len(str(taxaCode))) + str(taxaCode) + " " + taxa.replace(" ", "_") + ","
head = head[:-1] + "\n;"
end = 'End;\n'


outpath = os.path.join(r"/home/junru/data/mangchun/","inceptNoaug-%s-%d.nexus" % (time.strftime("%y%m%d"), len(taxaList)))
# outpath = os.path.join(r"E:\Corybas","resnetNoaug-%s-%d.nexus" % (time.strftime("%y%m%d"), len(taxaList)))
dupTimes = 1000 # Number of trees.
voteTimes = 5 # Repeating time when calculate the distance between images from two taxa.
global picDic
picDic = {} 
thisTime = 1
with open(outpath, "a") as f:
    f.write(head)
    f.write("\n\n")
while thisTime <= dupTimes:
    print("This is the No." + str(thisTime) + " duplication")
    taxaList = os.listdir("/home/junru/data/mangchun/fine_tune/dataset")
    tree = mainOperater(taxaList, voteTimes)
    res = "tree TREE" + str(thisTime) + " =" + tree + ":0.0;\n"
    with open(outpath, "a") as f:
        f.write(res)
    thisTime += 1
with open(outpath, "a") as f:
    f.write(end)
    
    
    
    
################################# 3, construct random trees #################################
# build random trees

# -*- coding: utf-8 -*-

import os
import random


def randomTree(num):
    groupList = [str(i+ 1) for i in range(num)]
    while len(groupList) != 1:
        thisgroupAindex = random.randint(0, len(groupList)-1)
        thisgroupA = groupList[thisgroupAindex]
        groupList.pop(thisgroupAindex)
        thisgroupBindex = random.randint(0, len(groupList)-1)
        thisgroupB = groupList[thisgroupBindex]
        groupList.pop(thisgroupBindex)
        newgroup = "(%s,%s)" % (thisgroupA, thisgroupB)
        groupList.append(newgroup)
    return groupList[0]

treeNum = 1000
# picDir = r"E:\corybasDistri\Corybas\secondAnalysis\allPic"
# picDir = r"E:\corybasDistri\Corybas\secondAnalysis\moreThan5Pic"
picDir = r"/home/junru/data/mangchun/fine_tune/dataset"

taxaList = os.listdir(picDir)
taxaList = [i.replace(" ", "_") for i in taxaList]

# outputPath = r"E:\corybasDistri\Corybas\secondAnalysis\randomTrees78.nexus"
# outputPath = r"E:\corybasDistri\Corybas\secondAnalysis\randomTrees50.nexus"
outputPath = r"/home/junru/data/mangchun/fine_tune/randomTrees38.nexus"

head = '#NEXUS\n\nBegin taxa;\n\tDimensions ntax=%d;\n\t\tTaxlabels\n' % len(taxaList)
for i in taxaList:
    head = head + "\t\t\t" + i + "\n"
head = head + "\t\t\t;\nEnd;\nBegin trees;\n\tTranslate\n"
for i in range(len(taxaList)):
    head = head + "\t\t\t" + str(i+1)+" " + taxaList[i] + ",\n"
head = head + ";\n\n"
    
with open(outputPath, "a", encoding="utf-8") as f:
    f.write(head)
for i in range(treeNum):
    with open(outputPath, "a", encoding="utf-8") as f:
        f.write('tree TREE%d =%s;\n' % (i+1, randomTree(len(taxaList))))

end = 'End;\n'
with open(outputPath, "a", encoding="utf-8") as f:
    f.write(end)