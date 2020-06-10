import cv2
import os 
import glob 

for img in glob.glob("mask" + "/*.png"):
    image = cv2.imread(img)
    image = cv2.resize(image, (0,0), fx=2, fy=2) 
    cv2.imwrite("mass/"+img[5:], image)
    print(img[5:])
