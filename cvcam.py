import cv2
import random
import time

randn = random.randint(1,10)

camera_port = 0
ramp_frames = 30

camera = cv2.VideoCapture(camera_port)

def get_image():
    retval, im = camera.read()
    return im

for i in range(ramp_frames):
    temp = get_image()


print("Taking image...")
for i in range(0, 150):
    time.sleep(0.01)
    camera_capture = get_image()
    file = "D:/WorkArea/GitHub/tensorflow-for-poets-2/tf_files/Humans/Sanjana/" + "_image" + str(i)  + ".jpg"
    cv2.imwrite(file, camera_capture)
del(camera)
