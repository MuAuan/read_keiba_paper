from PIL import Image
import sys

import pyocr
import pyocr.builders
import csv
import cv2
import matplotlib.pyplot as plt

tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)

tool = tools[0]
# そのOCRツールで使用できる言語を確認
langs = tool.get_available_languages()
print(langs) 
# 言語に日本語と今回の学習済みデータを指定
lang_setting = langs[3]  #langs[1]+"+"+langs[2]+"+"+langs[3]
print(lang_setting)
print("Will use tool '%s'" % (tool.get_name()))
with open('rect_line.txt', 'w', newline='\n', encoding="utf-8") as f:
    for i in range(1,84,1):
        txt = tool.image_to_string(
            Image.open("./data/8_1_roi_"+str(i)+".jpg"),
            lang=lang_setting,  # "jpn1",
            builder=pyocr.builders.LineBoxBuilder(tesseract_layout=6) #6 LineBoxBuilder #TextBuilder
        )
        # 認識範囲を描画
        out = cv2.imread("./data/8_1_roi_"+str(i)+".jpg")
        for d in txt:
            #print(d.content)
            print(d.position)
            cv2.rectangle(out, d.position[0], d.position[1], (0, 0, 255), 2)  # 赤い枠を描画
            plt.imshow(out)
            plt.pause(1)
            plt.close()
            txt=d.content
            print( txt )
            f.write(txt+'\n')
        
#C:\Users\user\ObjectiveNuro\text_detection\data\takaraduka\data