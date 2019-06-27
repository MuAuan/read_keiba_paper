import numpy as np
import cv2
import matplotlib.pyplot as plt
import os, shutil, time, cv2, math
import csv
from operator import attrgetter
from operator import itemgetter
    
output_root_path = './text_detection/data'
if not os.path.exists(output_root_path):os.mkdir(output_root_path)
output_root_path += '/takaraduka'
if not os.path.exists(output_root_path):os.mkdir(output_root_path)
output_root_path += '/20190622_11'
if not os.path.exists(output_root_path):os.mkdir(output_root_path)
output_root_path += '/'

input_original_data = './text_detection/data/raw/kiseki.jpg'  #kiseki_oosaka.jpg'

img = cv2.imread(input_original_data)
cv2.imshow("img",img)

min_area = 30 
max_area = 2500
tmp = img.copy()
tmp2 = img.copy()

rect2=[]
with open(output_root_path+'rect.csv', newline='') as f:
    rect1 = csv.reader(f, delimiter=' ', quotechar=' ')
    for r in rect1:
        r1=', '.join(r)
        print(r1)
        rect2.append(r1)

rect=[]
for i in range(len(rect2)):
    str = rect2[i]
    a=str.split(",")
    rect3=[]
    for j in range(4):
        rect1=int(a[j])
        print(type(rect1),a[j]) 
        rect3.append(rect1)
    rect.append(rect3)    
print("rect ",rect)

p=0
for i in range(len(rect)):
    print(rect[i])
    if rect[i][2] < 5 or rect[i][3] < 5:
        continue
    area = (rect[i][3])*(rect[i][2])
    if area < min_area or area > max_area:
        continue
    roi = tmp[rect[i][1]:rect[i][1]+rect[i][3], rect[i][0]:rect[i][0]+rect[i][2]]
    roi=cv2.resize(roi,(5*rect[i][2],5*rect[i][3]),interpolation=cv2.INTER_CUBIC)
    cv2.imshow("roi",roi)
    #cv2.imwrite(output_root_path + '8_1_roi_{}.jpg'.format(p), roi)
    img_dst=cv2.rectangle(tmp, (rect[i][0], rect[i][1]), (rect[i][0]+rect[i][2], rect[i][1]+rect[i][3]), (0, 255, 0), 2)
    cv2.imshow("IMAGE",img_dst)
    cv2.imwrite(output_root_path + '8_1_findContours_{}.jpg'.format(p), img_dst)
    plt.imshow(tmp)
    plt.pause(0.11)
    p += 1

cv2.imwrite(output_root_path + '8_1_findContours.jpg', tmp)
cv2.imwrite(output_root_path + '8_2_findContours.jpg', tmp2)
plt.close()