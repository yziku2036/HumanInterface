import cv2
import numpy as np
import random
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

def moji(img,colorcode,disp_str="ヒューマンインターフェース"):
	fontpath = "ttf/ipag.ttf"     
	fontsize=128
	cnt=-50
	#disp_str="ヒューマンインターフェース"
	font = ImageFont.truetype(fontpath, fontsize)
	img_pil = Image.fromarray(img)
	draw = ImageDraw.Draw(img_pil)
	draw.text((width/2-(fontsize/2)*len(disp_str),height/2-(fontsize/2)), disp_str, font = font, fill = (255,255,255,0))
	#for code_num in colorcode:
		#print(cnt)
		#draw.text(((width/2-(fontsize/2)+cnt)*len(disp_str),height/2-(fontsize/2+150)),str(1234) , font = font, fill = (255,255,255,0))
		#cnt+=50
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
	kijun_colorcode=[255,191,165]

	#スコア100の画像表示
	img_kijun=gen_image(kijun_colorcode)
	img_kijun=moji(img_kijun,kijun_colorcode,"基準カラー")
	img_kijun=display(img_kijun,"base")
	
	cv2.destroyAllWindows()
	#比較対象の画像表示
	colorcode_shuffled=random.sample(colorcode,len(colorcode))
	for code in colorcode_shuffled:
		img=gen_image(code)
		img=moji(img,code)
		display(img)

main()