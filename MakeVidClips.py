import cv2
import numpy as np
import glob
import os
 
for name in os.listdir("downloads/"):
	img_array = []
	filenames = glob.glob('downloads/'+name+'/*.jpg')

	for filename in filenames:
		img = cv2.imread(filename)
		#height, width, layers = img.shape
		#size = (width,height)
		img_array.append(img)

	out = cv2.VideoWriter('videos/' + name + 'test.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 1, (1920, 1080))

	for i in range(len(img_array)):
		out.write(img_array[i])

	out.release() 
