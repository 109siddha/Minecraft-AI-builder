import time
from directkeys import *
from PIL import Image
import numpy as np
import os

# white|red|green|blue|cyan|magenta|yellow|gray|black
#   1  | 2 |  3  | 4  | 5  |   6   |   7  | 8  |  9  



# To get each pixel values in numpy array
def getPixels(image):

	values = np.array([], dtype='int32')
	width, height = image.size 

	for i in range(width):
		for j in range(height):
			pixel = image.getpixel((i, j))

        
			if pixel[1] in range((pixel[0]-15), (pixel[0]+15)) and pixel[1] in range(70, 220):
				if pixel[1] in range(pixel[2]-15, pixel[2]+15):
					values = np.append(values, 8)
					print("GRAY")
					
				else:
					if pixel[0] <= 125:

						if pixel[1] <= 125:
							if pixel[2] <= 125:
								values = np.append(values, 9)
								print("BLACK")								
							else:
								values = np.append(values, 4)
								print("BLUE")

						elif pixel[2] <= 125:
							values = np.append(values, 3)
							print("GREEN")


						else:
							values = np.append(values, 5)
							print("CYAN")

					
					elif pixel[1] <= 125:
						if pixel[2] <= 125:
							values = np.append(values, 2)
							print("RED")

						else:
							values = np.append(values, 6)
							print("MAGENTA")

					elif pixel[2] <= 125:
						values = np.append(values, 7)
						print("YELLOW")

					else:
						values = np.append(values, 1)
						print("WHITE")

				
			else:
				if pixel[0] <= 125:

					if pixel[1] <= 125:
						if pixel[2] <= 125:
							values = np.append(values, 9)
							print("BLACK")								
						else:
							values = np.append(values, 4)
							print("BLUE")

					elif pixel[2] <= 125:
						values = np.append(values, 3)
						print("GREEN")


					else:
						values = np.append(values, 5)
						print("CYAN")

				
				elif pixel[1] <= 125:
					if pixel[2] <= 125:
						values = np.append(values, 2)
						print("RED")

					else:
						values = np.append(values, 6)
						print("MAGENTA")

				elif pixel[2] <= 125:
					values = np.append(values, 7)
					print("YELLOW")

				else:
					values = np.append(values, 1)
					print("WHITE")
	
	print("Ready to start")				
	return values



def builder(final_img):

	f_values = getPixels(final_img)
	total_blocks = f_values.size
	
	width, height = final_img.size
	column_block_n = 0
	total_block_number = 0

	for block in f_values:

		loop = True
		while loop == True:
			CAPSLOCK = CAPSLOCK_STATE()
			if ((CAPSLOCK) & 0xffff) != 0:
				loop = False 
			else:
				loop = True



		column_block_n += 1
		total_block_number += 1
		print(column_block_n, round((total_block_number/total_blocks)*100, 2), "% Completed")
		if column_block_n > height:
			PressKey(D)	
			time.sleep(0.5)
			ReleaseKey(D)
			PressKey(A)
			time.sleep(1)
			ReleaseKey(A)
			time.sleep(3)

			column_block_n = 1
			PressKey(eval('n' + str(block)))
			time.sleep(0.1)
			ReleaseKey(eval('n'+str(block)))

			PressKey(space)
			time.sleep(0.2)

			rightclick()
			ReleaseKey(space)
			
			time.sleep(0.1)
			rightrelease()

			time.sleep(0.2)			

		else:			
			PressKey(eval('n' + str(block)))
			time.sleep(0.01)
			ReleaseKey(eval('n'+str(block)))

			PressKey(space)
			time.sleep(0.2)

			rightclick()
			ReleaseKey(space)
			
			time.sleep(0.1)
			rightrelease()

			time.sleep(0.2)	





img_file = input("Enter the file name - ")
size_width = int(input("Enter width - "))

mainImage = Image.open(img_file)
mainWidth, mainHeight = mainImage.size
resized_img = mainImage.resize((size_width, int((size_width/mainWidth)*mainHeight)))
final_img = resized_img.rotate(180)

pixel = final_img.getpixel((10, 10))
print(pixel)

stime = time.time()
builder(final_img)
etime = time.time()
print(etime-stime,"taken to complete")
