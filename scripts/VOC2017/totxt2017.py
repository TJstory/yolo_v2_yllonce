#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 22:49:33 2017

@author: tramsys
"""

import os
import random

#trainval_percent = 0.66
train_percent = 1
xmlfilepath = '/home/tramsys/Desktop/darknet/scripts/VOCdevkit/VOC2017/Annotations'#home/tramsys/Desktop/darknet/scripts/VOCdevkit/VOC2007/
txtsavepath = '/home/tramsys/Desktop/darknet/scripts/VOCdevkit/VOC2017/ImageSets/Main'
total_xml = os.listdir(xmlfilepath)

num=len(total_xml)
list=range(num)
#tv=int(num*trainval_percent)
tr=int(num*train_percent)
#trainval= random.sample(list,tv)
train=random.sample(list,tr)

#ftrainval = open('/home/tramsys/Desktop/darknet/scripts/VOCdevkit/VOC2007/ImageSets/Main/trainval.txt', 'w')
#ftest = open('/home/tramsys/Desktop/darknet/scripts/VOCdevkit/VOC2007/ImageSets/Main/test.txt', 'w')
ftrain = open('/home/tramsys/Desktop/darknet/scripts/VOCdevkit/VOC2017/ImageSets/Main/train.txt', 'w')
#fval = open('/home/tramsys/Desktop/darknet/scripts/VOCdevkit/VOC2007/ImageSets/Main/val.txt', 'w')

for i  in list:
    name=total_xml[i][:-4]+'\n'
    #if i in trainval:
        #ftrainval.write(name)
    if i in train:
         ftrain.write(name)
        #else:
            #fval.write(name)
    #else:
        #ftest.write(name)

#ftrainval.close()
ftrain.close()
#fval.close()
#ftest .close()
