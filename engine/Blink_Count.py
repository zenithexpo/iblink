from scipy.spatial import distance
from imutils import face_utils
import imutils
import dlib
import cv2,json
import time,os
import datetime

thresh = 0.18

detect = dlib.get_frontal_face_detector()
predict = dlib.shape_predictor("engine/shape_predictor_68_face_landmarks.dat")# Dat file is the crux of the code

def read_config():
	# print(os.getcwd())
	# sys.stdout.flush()
	with open('config.js') as data_file:
		data_item = json.load(data_file)
	start = bool(data_item['status'])
	set_time = int( data_item['interval'])*60
	return(start,set_time)

def eye_aspect_ratio(eye):
	A = distance.euclidean(eye[1], eye[5])
	B = distance.euclidean(eye[2], eye[4])
	C = distance.euclidean(eye[0], eye[3])
	ear = (A + B) / (2.0 * C)
	return ear

def CountingArray(array):
	# array = [110101101]
	return array.count("01")
	# return finalCount

def CountBlink():
	number_of_blinks = 0
	(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS["left_eye"]
	(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS["right_eye"]
	cap = cv2.VideoCapture(0)
	blink_array = ""
	# 60
	end_time = time.time() + 60
	i = 0
	while time.time() < end_time:
		i += 1
		if i%5==0:
			start, set_time = read_config()
			if start==False:
				cv2.destroyAllWindows()
				cap.release()
				return -1

		# if len(blink_array)>0 and blink_array[-1]=="1":
		# 	print(blink_array)
		ret, frame=cap.read()
		frame = imutils.resize(frame, width=450)
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		subjects = detect(gray, 0)
		for subject in subjects:
			shape = predict(gray, subject)
			shape = face_utils.shape_to_np(shape)#converting to NumPy Array
			leftEye = shape[lStart:lEnd]
			rightEye = shape[rStart:rEnd]
			leftEAR = eye_aspect_ratio(leftEye)
			rightEAR = eye_aspect_ratio(rightEye)
			ear = (leftEAR + rightEAR) / 2.0
			leftEyeHull = cv2.convexHull(leftEye)
			rightEyeHull = cv2.convexHull(rightEye)

			if ear < thresh:
				blink_array += "1"
			else:
				blink_array += "0"

		key = cv2.waitKey(1) & 0xFF

	cv2.destroyAllWindows()
	cap.release()
	return CountingArray(blink_array)
