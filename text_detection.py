# original C++ source code
# http://nikoyuwono.com/2015/10/05/receipt-scanner/
import os, shutil, time, cv2, math
import numpy as np
import cv2
import csv
import matplotlib.pyplot as plt

output_root_path = './text_detection/data'
if not os.path.exists(output_root_path):os.mkdir(output_root_path)
output_root_path += '/takaraduka'
if not os.path.exists(output_root_path):os.mkdir(output_root_path)
output_root_path += '/20190622'
if not os.path.exists(output_root_path):os.mkdir(output_root_path)
output_root_path += '/'

input_original_data = './text_detection/data/raw/kiseki.jpg'

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

contours, hierarchy = cv2.findContours(lap2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
min_area = img.shape[0] * img.shape[1] * 1e-5  #-4
tmp = img.copy()
tmp2 = img.copy()
with open(output_root_path +'./rect.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    if len(contours) > 0:
        for i, contour in enumerate(contours):
            rect = cv2.boundingRect(contour)
            if rect[2] < 3 or rect[3] < 5:  #rect[2] < 10 or rect[3] < 10:
                continue
            area = cv2.contourArea(contour)
            if area < min_area:
                continue
            roi = tmp[rect[1]:rect[1]+rect[3], rect[0]:rect[0]+rect[2]]
            roi=cv2.resize(roi,(5*rect[2],5*rect[3]),interpolation=cv2.INTER_CUBIC)
            cv2.imshow("roi",roi)
            img_dst=cv2.rectangle(tmp, (rect[0], rect[1]), (rect[0]+rect[2], rect[1]+rect[3]), (0, 255, 0), 2)
            print(rect)
            cv2.imshow("IMAGE",img_dst)
            print(roi.shape)
            writer.writerow(map(lambda x: x, rect))
            writer.writerow(map(lambda x: x, roi.shape))
            writer.writerow(map(lambda x: x, roi))  
            # 回転を考慮した外接矩形
            rect = cv2.minAreaRect(contour)
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            tmp2 = cv2.drawContours(tmp2, [box], 0, (255, 255, 0), 2)
            plt.imshow(tmp)
            plt.pause(1)


cv2.imwrite(output_root_path + '8_1_findContours.jpg', tmp)
cv2.imwrite(output_root_path + '8_2_findContours.jpg', tmp2)