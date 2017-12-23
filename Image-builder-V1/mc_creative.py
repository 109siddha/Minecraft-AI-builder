import time
from directkeys import *
from PIL import Image
import numpy as np 
import os

# white|red|green|blue|cyan|magenta|yellow|gray|black
#   1  | 2 |  3  | 4  | 5  |   6   |   7  | 8  |  9  


def open_image(path):
	newImage = Image.open(path)
	return newImage

def img_resize(img, size_x, size_y):

 	resized = img.resize((size_x, size_y))
 	return resized

def save_image(image, path):
    image.save(path, 'png')

def get_pixel(image, i, j):
    width, height = image.size
    if i > width or j > height:
        return None

    # Get Pixel
    else:
        pixel = image.getpixel((i,j))
        return pixel



img = open_image('miniont.png')
# result = img.convert('P', palette=Image.ADAPTIVE, colors=5)
# result.show()
rotate_img = img.rotate(180)
rs_img = img_resize(rotate_img, 10, 10)


def get_color(img):

	values = np.array([], dtype='int32')
	width, height = img.size 

	for i in range(width):
		for j in range(height):

			print(i, j)
			pixel = get_pixel(img, i, j)
			print(pixel)
			# values = np.append(values, pixel)

			if pixel[1] in range((pixel[0]-15), (pixel[0]+15)) and pixel[1] in range(70, 220):
				if pixel[1] in range(pixel[2]-15, pixel[2]+15):
					print("GRAY")
					values = np.append(values, 8)
					# print(values)
				else:
								
					if pixel[0] < 125:
						if pixel[1] < 125:
							if pixel[2] < 125:
								print("BLACK")
								values = np.append(values, 9)
							else:
								print("BLUE")
								values = np.append(values, 4)
								# return 4 

						elif pixel[2] < 125:
							print("GREEN")
							values = np.append(values, 3)
							# return 3

						else:
							print("CYAN")
							values = np.append(values, 5)
							# return 5

					
					elif pixel[1] < 125:
						if pixel[2] < 125:
							print("RED")
							values = np.append(values, 2)
							# return 2
						else:
							print("MAGENTA")
							values = np.append(values, 6)
							# return 6

					elif pixel[2] < 125:
						print("YELLOW")
						values = np.append(values, 7)
						# return 7
					else:
						print("WHITE")
						values = np.append(values, 1)
						# return 1
				
######
			else:
				if pixel[0] < 125:
					if pixel[1] < 125:
						if pixel[2] < 125:
							print("BLACK")
							values = np.append(values, 9)
						else:
							print("BLUE")
							values = np.append(values, 4)
							# return 4 

					elif pixel[2] < 125:
						print("GREEN")
						values = np.append(values, 3)
						# return 3

					else:
						print("CYAN")
						values = np.append(values, 5)
						# return 5

				
				elif pixel[1] < 125:
					if pixel[2] < 125:
						print("RED")
						values = np.append(values, 2)
						# return 2
					else:
						print("MAGENTA")
						values = np.append(values, 6)
						# return 6

				elif pixel[2] < 125:
					print("YELLOW")
					values = np.append(values, 7)
					# return 7
				else:
					print("WHITE")
					values = np.append(values, 1)
					# return 1

	return values


f_values = get_color(rs_img)
# print(f_values)
# print(f_values.shape)
# print(f_values.size)

def builder(array, split_size=10):
	a = 0
	number = 0
	for block in array:
		a = a+1
		number = number + 1
		print(a, number)
		if a > split_size:
			PressKey(D)	
			time.sleep(0.5)
			ReleaseKey(D)
			PressKey(A)
			time.sleep(1)
			ReleaseKey(A)
			time.sleep(3)
			a = 1
			PressKey(eval('n'+str(block)))
			time.sleep(0.1)
			ReleaseKey(eval('n'+str(block)))
			PressKey(space)
			time.sleep(0.1)
			PressKey(P)
			ReleaseKey(space)
			PressKey(P)
			time.sleep(0.5)
			ReleaseKey(P)
			time.sleep(0.4)		

		else:			
			PressKey(eval('n' + str(block)))
			time.sleep(0.1)
			ReleaseKey(eval('n'+str(block)))
			PressKey(space)
			time.sleep(0.1)
			PressKey(P)
			ReleaseKey(space)
			PressKey(P)
			time.sleep(0.4)
			ReleaseKey(P)
			time.sleep(0.3)

  


builder(f_values)




