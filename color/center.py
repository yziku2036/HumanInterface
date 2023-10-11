#!/usr/bin/env python

import numpy as np
import cv2

from PIL import ImageFont, ImageDraw, Image
from time import sleep

# create blank image - y, x
img = np.zeros((600, 1000, 3), np.uint8)
fontpath = "ttf/ipag.ttf"     

font = ImageFont.truetype(fontpath, 32)
img_pil = Image.fromarray(img)
draw = ImageDraw.Draw(img_pil)
draw.text((50, 100),  "いっつにほんご！", font = font)
img = np.array(img_pil)

# setup text
font = cv2.FONT_HERSHEY_SIMPLEX
text = "Hello Joseph!ああああ"

# get boundary of this text
textsize = cv2.getTextSize(text, font, 1, 2)[0]

# get coords based on boundary
textX = int((img.shape[1] - textsize[0]) / 2)
textY = int((img.shape[0] + textsize[1]) / 2)

# add text centered on image
cv2.putText(img, text, (textX, textY ), font, 1, (255, 255, 255), 2)

# display image
while True:
	cv2.imshow('image', img)
	key=cv2.waitKey(1)
	if key==27:
		break

# cleanup
cv2.destroyAllWindows()
