import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

width=1920
height=1080


def gen_image(colorcode):
	img=np.zeros((400, 600, 3), np.uint8)
	tmp=np.zeros((400, 600), np.uint8)
	r=colorcode[0]
	g=colorcode[1]
	b=colorcode[2]
	img[:,:,0]=r
	img[:,:,1]=g
	img[:,:,2]=b
	img=cv2.cvtColor(img,cv2.COLOR_BGR2HLS)
	
	img[:,:,1]=tmp
	img[:,:,1]=img[:,:,2]
	img[:,:,2]=tmp
	
	return img


def main():
	fontpath = "ttf/ipag.ttf"     
	font = ImageFont.truetype(fontpath, 32)
	
	img=gen_image([255,191,165])
	
	#img_pil = Image.fromarray(img)
	#draw = ImageDraw.Draw(img_pil)

	#img.text((50, 100),  "いっつにほんご！", font = font)
	ima = cv2.putText(img, 'ヒューマンインターフェース', (width/2,height/2), font,  
                   12, [0,0,0], 4, cv2.LINE_AA) 

	while True:
		cv2.imshow("frame",img)
		key=cv2.waitKey(1)
		if key==27:
			break

main()