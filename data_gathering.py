import cv2
import os
from tkinter import simpledialog
from tkinter import messagebox


face_detector = cv2.CascadeClassifier('Cascades/haarcascade_frontalface_default.xml')

def main(cam):
	# For each person, enter one numeric face id

	face_id = simpledialog.askstring("Enter face ID", "\n enter inmate id and press <ok> ")
	messagebox.showinfo("[INFO]", "Initializing face capture. Look the camera and wait ...\n (make sure to keep facing the camera)\n Press ESC to stop")

	# Initialize individual sampling face count
	count = 0
	path = "dataset/"

	while(True):

		ret, img = cam.read()
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		faces = face_detector.detectMultiScale(gray, 1.3, 5)

		for (x,y,w,h) in faces:

			cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
			count += 1

			# Save the captured image into the datasets folder
			cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])

			cv2.imshow('image', img)

		k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
		if k == 27:
			break
		elif count >= 30: # Take 30 face sample and stop video
			break

	# Do a bit of cleanup
	print("\n [INFO] Exiting Program and cleaning up stuff")
	cam.release()
	cv2.destroyAllWindows()




