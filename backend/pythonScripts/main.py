import cv2
import numpy as np
import imutils
import os
import sys
from html_generator import *


img = cv2.imread('./images/' + sys.argv[1])
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# blue range
lower_blue = np.array([90, 60, 0])
upper_blue = np.array([121, 225, 255])

# green range
lower_green = np.array([36, 25, 25])
upper_green = np.array([70, 255, 255])

# red range
lower_red = np.array([170, 70, 50])
upper_red = np.array([180, 255, 255])

mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
mask_green = cv2.inRange(hsv, lower_green, upper_green)
mask_red = cv2.inRange(hsv, lower_red, upper_red)

blue_contours = cv2.findContours(
    mask_blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
blue_contours = imutils.grab_contours(blue_contours)

green_contours = cv2.findContours(
    mask_green, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
green_contours = imutils.grab_contours(green_contours)

red_contours = cv2.findContours(
    mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
red_contours = imutils.grab_contours(red_contours)

# empty arrays
divs = []
paragraphs = []
images = []

for cb in blue_contours:
    x, y, w, h = cv2.boundingRect(cb)
    div = [x, y, w, h]
    divs.append(div)
    cv2.rectangle(img, (x, y), (x+w, y+h), (225, 255, 0), 2)
    # print('div: ', div)

for cg in green_contours:
    x, y, w, h = cv2.boundingRect(cg)
    paragraph = [x, y, w, h]
    paragraphs.append(paragraph)
    cv2.rectangle(img, (x, y), (x+w, y+h), (225, 225, 0), 2)
    # print('paragraph: ', paragraph)

for cr in red_contours:
    x, y, w, h = cv2.boundingRect(cr)
    image = [x, y, w, h]
    images.append(image)
    cv2.rectangle(img, (x, y), (x+w, y+h), (225, 225, 0), 2)
    # print('image: ', image)


# convert arrays into np.arrays
divs = np.array(divs)
paragraphs = np.array(paragraphs)
images = np.array(images)

# for item in divs:
#     print(item)

# for item in paragraphs:
#     print(item)

# for item in images:
#     print(item)


html_string = generate_html_string(divs, paragraphs, images)

# print(html_string)

save_path = './htmlGen'
file_name = 'index.html'
complete_name = os.path.join(save_path, file_name)

with open(complete_name, "w") as html_file:
    html_file.write(html_string)

# cv2.imshow("test", img)
# cv2.waitKey(0)
