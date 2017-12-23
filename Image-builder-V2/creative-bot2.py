from directkeys import *
from PIL import Image
import numpy as np 
import os
import time
import colorsys

W0 = [80,0]
W1 = [35,0]
W2 = [155,0]
W3 = [42,00]
K0 = [35,8]
K1 = [1,0]
K2 = [35,7]
K3 = [173,0]
R0 = [35,6]
R1 = [159,6]
R2 = [35,14]
R3 = [152,0]
G0 = [133,0]
G1 = [35,5]
G2 = [159,5]
G3 = [159,13]
B0 = [174,0]
B1 = [35,3]
B2 = [35,11]
B3 = [22,0]
C0 = [169,0]
C1 = [57,0]
C2 = [168,1]
C3 = [168,0]
M0 = [35,2]
M1 = [159,2]
M2 = [35,10]
M3 = [159,11]
Y0 = [19,0]
Y1 = [41,0]
Y2 = [35,4]
Y3 = [159,4]

O0 = [35,1]
O1 = [35,1]
O2 = [35,1]
O3 = [35,1]

ign = "paulolops"   
 
# region0 = list(range(0,86))
# region1 = list(range(86,171))
# region2 = list(range(171,256))

# regions = [region0, region1, region2]
# colors = [0,1,2] # 0-red, 1-green, blue-2

# blocks = {}

print("start")

# pixel = (124, 112, 222)
# if all(value <= 40 for value in pixel):
# 	print("Black")
# elif all(value >= 214 for value in pixel):
# 	print("White")

# else:
# 	for r in regions:
# 		for c in colors:
# 			if pixel[c] in r:
# 				print(pixel[c], r)



# filename = "miniont.png"
filename = input("Enter filename: ")
mainimage = Image.open(filename)

sizewidth = int(input("Enter sizewidth: "))
# sizewidth = 3
mainWidth, mainHeight = mainimage.size
resized_img = mainimage.resize((sizewidth, int((sizewidth/mainWidth)*mainHeight)))
rotated_img = resized_img.rotate(180)

color_reduced_img = rotated_img.convert('P', palette=Image.ADAPTIVE, colors=2)
gray_img = color_reduced_img.convert("L")

l_pixel_values = np.array([], dtype='int32')
hls_pixel_values = np.array([], dtype='int32')
data_values = np.array([])
final_blocks = np.array([], dtype='int32')
something = np.array([])

width, height = gray_img.size
# for w in range(width):
# 	for h in range(height):
# 		l_pixel = gray_img.getpixel((w,h))
# 		scale_down_value = int(l_pixel*4/255)  # Gives int values from [0-3], which range from white to black
# 		# print(scale_down_value)
# 		l_pixel_values = np.append(l_pixel_values ,scale_down_value)

# ------------------------------------------------------------< 
		
# with open("mc-block-color.txt") as file:
# 	content = file.readlines()


# for line in content:
# 	line = line.strip()
# 	# data_value = [x for x in line.split(" ")]
# 	# # data_values = np.append(data_values, data_value)
# 	# print(data_value)
# 	# data_values.append(data_value)
# 	# # print(data_value[0])
# 	for x in line.split(" "):
# 		something = np.append(something, x)
# 		# print(x)

# print(something)
# ------------------------------------------------------------>

def hls_to_color(hls_value):
	
	if 0.0 <= round(hls_value[0],2) <= 0.1:
		color = "O"
		# print(color, scale_down_value)
		return color

	elif 0.1 <= round(hls_value[0],2) <= 0.2:
		color = "Y"
		
		return color
	elif 0.2 <= round(hls_value[0],2) <= 0.4:
		color = "G"
		# print(color, scale_down_value)
		return color
	elif 0.4 <= round(hls_value[0],2) <= 0.5:
		color = "C"
		# print(color, scale_down_value)
		return color
	elif 0.5 <= round(hls_value[0],2) <= 0.7:
		color = "B"
		# print(color, scale_down_value)
		return color
	elif 0.7 <= round(hls_value[0],2) <= 0.8:
		color = "M"
		# print(color, scale_down_value)
		return color
	elif 0.8 <= round(hls_value[0],2) <= 1.0:
		color = "R"
		# print(color, scale_down_value)
		return color
	else:
		print(" ¯\_(ツ)_/¯ ")
		# return None


def color_scale(hls_value):
	if 0.0 <= round(hls_value[1],2) <= 0.15:
		color = "K"
		# print(color, scale_down_value)
		return color

	elif 0.15 <= round(hls_value[1],2) <= 0.85:
		# print("Color")
		color = hls_to_color(hls_value)
		return color

	elif 0.85 <= round(hls_value[1],2) <= 15:
		color = "W"
		# print(color, scale_down_value)
		return color
	else:
		print(" ¯\_(ツ)_/¯ ")
		# return None

def char2keyin(char):
	time.sleep(0.01)
	PressKey(eval(char))
	time.sleep(0.01)
	ReleaseKey(eval(char))
	


def cmdin(block):

	print(block)
	a = block[0]
	b = block[1]
	block = str(a)+":"+str(b)

	cmd = "give "+ign+" "+ block +" 1"
	print(cmd.upper())
	return cmd.upper()


for w in range(width):
	for h in range(height):
		l_pixel = gray_img.getpixel((w,h))
		scale_down_value = int(l_pixel*3/255)  # Gives int values from [0-3], which range from white to black
		# print(scale_down_value)
		l_pixel_values = np.append(l_pixel_values ,scale_down_value)

		pixel = resized_img.getpixel((w,h))
		
		hls_value = colorsys.rgb_to_hls(*[x/255.0 for x in resized_img.getpixel((w,h))])

		# print(hls_value,"--",pixel)
		hls_pixel_values = np.append(hls_pixel_values, hls_value)

		# hue_value = hls_pixel_values[0]
		# print(hue_value)

		color_1 = color_scale(hls_value)
		color_info = color_1 + str(scale_down_value)
		data_values = np.append(data_values,color_info)

def entercmd(command):

	time.sleep(0.2)
	# print(command)
	char2keyin("fslash")
	time.sleep(0.2)
	for char in command:
		
		if char == " ":
			char2keyin("space")
			
		elif char == ":":
			PressKey(lshift)
			char2keyin("semicolon")
			ReleaseKey(lshift)
		elif char.isdigit():
			char2keyin("n"+char)
		else:
			# print(char)
			# aa = eval(char)
			char2keyin(char)
				
	char2keyin("enter")


width, height = resized_img.size
column_block_n = 0
total_block_number = 0

for coco in data_values:
	coco = eval(coco)
	command = cmdin(coco)
	entercmd(command)
	time.sleep(0.1)
	# ---------------------------------

	# f_values = getPixels(final_img)
	# total_blocks = f_values.size

	width, height = resized_img.size
	column_block_n = 0
	total_block_number = 0

	loop = True
	while loop == True:
		CAPSLOCK = CAPSLOCK_STATE()
		if ((CAPSLOCK) & 0xffff) != 0:
			loop = False 
		else:
			loop = True


	column_block_n += 1
	total_block_number += 1
	# print(column_block_n, round((total_block_number/total_blocks)*100, 2), "% Completed")

	if column_block_n > height:
		print("next_column")
		PressKey(D)	
		time.sleep(0.5)
		ReleaseKey(D)
		PressKey(A)
		time.sleep(1)
		ReleaseKey(A)
		time.sleep(3)

		column_block_n = 1
		PressKey(space)
		time.sleep(0.2)
		rightclick()
		ReleaseKey(space)			
		time.sleep(0.1)
		rightrelease()
		time.sleep(0.2)		

	else:
		PressKey(space)
		time.sleep(0.2)

		rightclick()
		ReleaseKey(space)
		
		time.sleep(0.1)
		rightrelease()

		time.sleep(0.2)	

print("Complete")
	

		
	# ------------------------------------



# def builder():

# 	for p in range(1,10):

# 		PressKey(eval('n'+str(p)))
# 		time.sleep(0.05)
# 		ReleaseKey(eval('n'+str(p)))
# 		print(eval('n'+str(p)))


# builder()




	

	