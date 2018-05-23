# Impporting dependecies
import os
import sys
import subprocess
import cv2
import random
import time
import pyttsx

# testimg function is created
def testimg():
	# printing the number of seconds left
	count = reversed(range(1 , 4))
	for i in count:
		print("T-minus", i)
		time.sleep(1)
	# random number is generated
	randn = random.randint(1,100)
	
	#camera settings are configured
	camera_port = 0
	ramp_frames = 30

	camera = cv2.VideoCapture(camera_port)

	def get_image():
	    retval, im = camera.read()
	    return im

	for i in range(ramp_frames):
	    temp = get_image()

	# Take the Photo
	print("Taking image...")
	time.sleep(0.01) # sleep time of 0.01 secs
	camera_capture = get_image()
	img_test = "_image" + str(randn)  + ".jpg" #one photo taken to test 
	# test photos are stored inside Test_img folder
	file = "D:/WorkArea/GitHub/tensorflow-for-poets-2/tf_files/Test_img/" + img_test
	cv2.imwrite(file, camera_capture)
	del(camera) 

	print("Testing..")
	for i in range(1, 100):
		print(i * "*")
		time.sleep(0.001)
	# Classifying
	os.system("python -m scripts.label_image --graph=tf_files/retrained_graph.pb --image=tf_files/Test_img/" + img_test)
	with open('results.txt', 'r') as f:
		first_line = f.readline()
	print(first_line) # printing the first line

	print(type(first_line))
	# speech engine is initialized
	engine = pyttsx.init()
	engine.say("I am pretty sure you are")
	time.sleep(0.05)
	engine.say(first_line)
	engine.runAndWait()
#testimg()