## Importing Dependencies
import os
import sys
import subprocess
import cv2
import random
import time
import test
import pyttsx

if __name__ == '__main__':
	""" Either Train the model or Test it """
	print("1. Train") # Enter 1 to train
	print("2. Test") # Enter 2 to train
	# Fucntion called
	option = input("")
	if option == "1":
		pass
	elif option == "2":
		test.testimg()
		exit()
	else:
		print("Invalid Option")

# Training class
class Training():

	def __init__(self, human):
		self.human = human
		# To create a Folder with the New User
		file_path = "D:/WorkArea/GitHub/tensorflow-for-poets-2/tf_files/Humans/" + self.human
		# Check if the Folder exists, if not create a new folder
		if not os.path.exists(file_path):
			os.makedirs(file_path)
	
	# Return the name of the person
	def HUMAN(self):
		return(self.human)

	
# Read the name of the person
tellmeyourname = input("Your Name: ")
human_me = Training(tellmeyourname) #Create an object with the name

# Generate a random number
randn = random.randint(1,10)

# settings to capture the photo
camera_port = 0
ramp_frames = 30

camera = cv2.VideoCapture(camera_port)

def get_image():
    retval, im = camera.read()
    return im

for i in range(ramp_frames):
    temp = get_image()


# Take the photo
print("Taking image...")
# capture 150 photos
for i in range(0, 150):
	# Sleep time of 0.01 seconds
    time.sleep(0.01)
    camera_capture = get_image()
    # dir to save the file + file name
    file = "D:/WorkArea/GitHub/tensorflow-for-poets-2/tf_files/Humans/" + str(human_me.HUMAN()) + '/' +"_image" + str(i)  + ".jpg"
    cv2.imwrite(file, camera_capture)
del(camera) # close the object

# print the name of the person
print(human_me.HUMAN())

## IMPORTANT

# training script with training steps set to 100
os.system("python -m scripts.retrain --bottleneck_dir=tf_files/bottlenecks --how_many_training_steps=100 --model_dir=tf_files/models/inception --output_graph=tf_files/retrained_graph.pb --output_labels=tf_files/retrained_labels.txt --image_dir=tf_files/Humans")

# test script is invovked to for a quick test.
test.testimg()