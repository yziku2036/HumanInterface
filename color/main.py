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

def moji(img):
	fontpath = "ttf/ipag.ttf"     
	fontsize=128
	disp_str="ヒューマンインターフェース"
	font = ImageFont.truetype(fontpath, fontsize)
	img_pil = Image.fromarray(img)
	draw = ImageDraw.Draw(img_pil)
	draw.text((width/2-(fontsize/2)*len(disp_str),height/2-(fontsize/2)), disp_str, font = font, fill = (255,255,255,0))
	img=np.array(img_pil)
	return img

def display(img,wname="frame"):
	while True:
		cv2.imshow(wname,img)
		key=cv2.waitKey(1)
		if key== 27:
			break

def main():
	#輝度の高い順に背景色のカラーコードを用意
	colorcode=[[255,219,205],[255,176,145],[255,133,84],[255,90,25],[220,62,0],[160,45,0],[100,28,0]]
	
	#スコア100の画像表示
	img=gen_image([255,191,165])
	img=display(img,"base")
	cv2.destroyAllWindows()
	#比較対象の画像表示
	for code in colorcode:
		img=gen_image(code)
		img=moji(img)
		display(img)

main()