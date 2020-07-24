import numpy as np
import cv2
from time import sleep
i = 0
cap = cv2.VideoCapture("messi.mp4")
while True:
	ret,im = cap.read()
	imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
	ret,thresh = cv2.threshold(imgray,200,255,cv2.THRESH_BINARY)
	contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)	
	for cnt in contours:
		area = cv2.contourArea(cnt)
		if area > 10**3:
			episolon = 0.005*cv2.arcLength(cnt,True)
			poly = cv2.approxPolyDP(cnt,episolon,True)

			if len(poly) > 10:
				im = cv2.drawContours(im, [poly],0, (0,255,0), 3)
				M = cv2.moments(cnt)
				x = int(M['m10']/M['m00'])
				y = int(M['m01']/M['m00'])
				x1 = poly.ravel()[0]
				y1 = poly.ravel()[1]
				x2 = poly.ravel()[2]
				y2 = poly.ravel()[3]
				d1 = ((x1-x)**2+(y1-y)**2)**0.5
				d2 = ((x2-x)**2+(y2-y)**2)**0.5
				if(abs(d1-d2) <1 ):
					cv2.imshow("test",im)
					cv2.putText(im,"Circle",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0))
				else:
					cv2.putText(im,"Oval",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0))



		
		if cv2.waitKey(20) & 0xFF == ord('q'):
			break 