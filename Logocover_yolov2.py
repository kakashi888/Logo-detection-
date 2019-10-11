# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 23:04:35 2019

@author: Rohit Soni
"""
import os 
from os import listdir
from os.path import isfile, join
import cv2
import numpy as np
import matplotlib


mypath = "D:\PR\Coca\Frames"

import cv2
import numpy as np
import matplotlib.pyplot as plt
net = cv2.dnn.readNet("YOLOv2_logo_detection_10000th_iteration.weights", "yolov2_logo_detection.cfg")
classes = []
with open("obj.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]
layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
colors = np.random.uniform(0, 255, size=(len(classes), 3))
i = 0
for f in listdir(mypath):
    if f.endswith(".jpg"):
        img = cv2.imread(f)
    else:
        continue
    #img = cv2.cv
    #img = cv2.resize(img, (416, 416))
    height, width, channels = img.shape
    #plt.imshow(img)
    blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    
    net.setInput(blob)
    outs = net.forward(output_layers)
    class_ids = []
    confidences = []
    boxes = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
        
            class_id = np.argmax(scores)
        
            confidence = scores[class_id]
            if confidence > 0.1:
                # Object detected
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                # Rectangle coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)
    
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.1, 0.3)
    
    
    font = cv2.FONT_HERSHEY_PLAIN
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            print(x, y, w, h)
            label = str(classes[class_ids[i]])
            color = colors[i]
            cv2.rectangle(img, (x, y), (x + w, y + h), color, -1)
            #cv2.putText(img, label, (x, y + 30), font, 3, color, 2)
    #cv2.imshow("Image", img)
    cv2.imwrite("Out" +f+".jpg",img)
    i+=1
    #cv2.waitKey(0)

cv2.destroyAllWindows()