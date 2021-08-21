import cv2
import numpy as np
import imutils
from numpy.lib.shape_base import column_stack

img = cv2.imread('images/test3.jpg')
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
    print('div: ', div)

for cg in green_contours:
    x, y, w, h = cv2.boundingRect(cg)
    paragraph = [x, y, w, h]
    paragraphs.append(paragraph)
    cv2.rectangle(img, (x, y), (x+w, y+h), (225, 225, 0), 2)
    print('paragraph: ', paragraph)

for cr in red_contours:
    x, y, w, h = cv2.boundingRect(cr)
    image = [x, y, w, h]
    images.append(image)
    cv2.rectangle(img, (x, y), (x+w, y+h), (225, 225, 0), 2)
    print('image: ', image)


# convert arrays into np.arrays
divs = np.array(divs)
paragraphs = np.array(paragraphs)
images = np.array(images)

for item in divs:
    print(item)

for item in paragraphs:
    print(item)

for item in images:
    print(item)

#creating div elements string for html file
div_elem = "".join(
    f"""
    <div class="div{index}"></div>
    """ 
    for index, div in enumerate(divs)
)

#creating p elements string for html file
p_elem = "".join(
    f"""
    <p class="p{index}"></p>
    """
    for index, p in enumerate(paragraphs)
)

#creating img elements string for html file
img_elem = "".join(
    f"""
    <img class="img{index}" />
    """
    for index, img in enumerate(images)
)

#creating div style string for css file
div_style = "".join(
    f""".div{index} {{
    position: absolute;
    right: {div[0]}px;
    top: {div[1]}px;
    width: {div[2]}px;
    height: {div[3]}px;
    border: 3px solid blue;
}}\n
"""
    for index, div in enumerate(divs)
)

#creating p style string for css file
p_style = "".join(
    f""".p{index} {{
    position: absolute;
    right: {p[0]}px;
    top: {p[1]}px;
    width: {p[2]}px;
    height: {p[3]}px;
    border: 3px solid green;
}}\n"""
    for index, p in enumerate(paragraphs)
)

#creating img style string for css file
img_style = "".join(
    f""".img{index} {{
    position: absolute;
    right: {img[0]}px;
    top: {img[1]}px;
    width: {img[2]}px;
    height: {img[3]}px;
    border: 3px solid red;
}}\n"""
    for index, img in enumerate(images)
)

css_content = f"""* {{
    margin: 0;
    padding: 0;
}}

{div_style}
{p_style}
{img_style}
"""

#creating div style string for css file
html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Draw2HTML</title>
    <style>
        {css_content}
    </style>
</head>
<body>
    {div_elem}
    {p_elem}
    {img_elem}
</body>
</html>\n
"""

with open("index.html", "w") as html_file:
    html_file.write(html_content)


cv2.imshow("test", img)
cv2.waitKey(0)