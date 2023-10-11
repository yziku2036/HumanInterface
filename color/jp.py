import numpy as np
from PIL import ImageFont, ImageDraw, Image
import cv2
import time


def main():
	## Make canvas and set the color
	img = np.zeros((200,400,3),np.uint8)
	b,g,r,a = 0,255,0,0

	## Use cv2.FONT_HERSHEY_XXX to write English.
	text = time.strftime("%Y/%m/%d %H:%M:%S %Z", time.localtime()) 
	cv2.putText(img,  text, (50,50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (b,g,r), 1, cv2.LINE_AA)

	## Use simsum.ttc to write Chinese.
	fontpath = "ttf/ipag.ttf"     
	font = ImageFont.truetype(fontpath, 32)
	img_pil = Image.fromarray(img)
	draw = ImageDraw.Draw(img_pil)
	draw.text((50, 100),  "ほげほｇへS乐!", font = font, fill = (b, g, r, a))
	img = np.array(img_pil)

	return img


import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

width=1920
height=1080

def gen_image(colorcode):
	img=np.zeros((height,width, 3), np.uint8)
	tmp=np.zeros((height,width), np.uint8)
	r=colorcode[2]
	g=colorcode[1]
	b=colorcode[0]
	img[:,:,0]=r
	img[:,:,1]=g
	img[:,:,2]=b
	return img

def puttext(img):
	fontpath = "ttf/ipag.ttf"     
	font = ImageFont.truetype(fontpath, 32)
	img = cv2.putText(img, 'ヒューマンインターフェース', [int(width/2),int(height/2)], font,  
                   12, [0,0,0], 4, cv2.LINE_AA) 
	return img

def display(img,wname="frame"):
	while True:
		cv2.imshow(wname,img)
		key=cv2.waitKey(1)
		if key== 27:
			break

def main():
	#輝度の高い順
	colorcode=[[255,219,205],[255,176,145],[255,133,84],[255,90,25],[220,62,0],[160,45,0],[100,28,0]]
	
	img=gen_image([255,191,165])
	img=display(img,"base")
	cv2.destroyAllWindows()
	for code in colorcode:
		img=gen_image(code)
		display(img)


main()