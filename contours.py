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
output_root_path += '/20190622_9'
if not os.path.exists(output_root_path):os.mkdir(output_root_path)
output_root_path += '/'

input_original_data = './text_detection/data/raw/kiseki.jpg'  #kiseki_oosaka.jpg'

img = cv2.imread(input_original_data)
cv2.imshow("img",img)

h, s, gray = cv2.split(cv2.cvtColor(img, cv2.COLOR_BGR2HSV))
size = (3, 3)
blur = cv2.GaussianBlur(gray, size, 0)
cv2.imwrite(output_root_path + '1_blur.jpg', blur)

lap = cv2.Laplacian(blur, cv2.CV_8UC1)
cv2.imwrite(output_root_path + '2_laplacian.jpg', lap)

# Otsu's thresholding
ret2, th2 = cv2.threshold(lap, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU) #lap
cv2.imwrite(output_root_path + '3_th2.jpg', th2)

kernel = np.ones((3, 8), np.uint8)  #(3, 20)
closing = cv2.morphologyEx(th2, cv2.MORPH_CLOSE, kernel)
cv2.imwrite(output_root_path + '4_closing.jpg', closing)

kernel = np.ones((3, 3), np.uint8)
dilation = cv2.dilate(closing, kernel, iterations = 1) #closing
cv2.imwrite(output_root_path + '5_dilation.jpg', dilation)
erosion = cv2.erode(dilation, kernel, iterations = 1)
cv2.imwrite(output_root_path + '6_erosion.jpg', erosion)

lap2 = cv2.Laplacian(erosion, cv2.CV_8UC1)
cv2.imwrite(output_root_path + '7_laplacian_2.jpg', lap2)

contours, hierarchy = cv2.findContours(lap2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #CV_RETR_TREE
min_area = 30 #img.shape[0] * img.shape[1] * 1e-3  #-4
max_area = 2500 #img.shape[0] * img.shape[1] * 1e-3  #-4
tmp = img.copy()
tmp2 = img.copy()

rect=[]
for i, contour in enumerate(contours):
    re = cv2.boundingRect(contour)
    print(re)
    rect.append(re)
#rect=np.array(rect)
#print(rect)
rect=sorted(rect, key=itemgetter(0))
#rect=sorted(rect, key=itemgetter(1))
#print("rect",rect)
#print(rect[0][0],rect[0][1],rect[0][2],rect[0][3])
with open(output_root_path +'./rect.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    #if len(contours) > 0:
    for i in range(len(rect)):
        print(rect[i][0],rect[i][1],rect[i][2],rect[i][3])
        #rect = cv2.boundingRect(contour)
        if rect[i][2] < 5 or rect[i][3] < 5:  #rect[2] < 10 or rect[3] < 10:  rect[i][2] < 5 or rect[i][3] < 5
            continue
        area = (rect[i][3])*(rect[i][2])  #cv2.contourArea(contour)
        if area < min_area or area > max_area:
            continue
        roi = tmp[rect[i][1]:rect[i][1]+rect[i][3], rect[i][0]:rect[i][0]+rect[i][2]]
        roi=cv2.resize(roi,(5*rect[i][2],5*rect[i][3]),interpolation=cv2.INTER_CUBIC)
        cv2.imshow("roi",roi)
        img_dst=cv2.rectangle(tmp, (rect[i][0], rect[i][1]), (rect[i][0]+rect[i][2], rect[i][1]+rect[i][3]), (0, 255, 0), 2)
        #print(rect[i])
        cv2.imshow("IMAGE",img_dst)
        #print(roi.shape)
        writer.writerow(map(lambda x: x, rect[i]))
        plt.imshow(tmp)
        plt.pause(1)

cv2.imwrite(output_root_path + '8_1_findContours.jpg', tmp)
cv2.imwrite(output_root_path + '8_2_findContours.jpg', tmp2)