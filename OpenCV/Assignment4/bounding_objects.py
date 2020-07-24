import imutils
import cv2

class ShapeDetector:
	def __init__(self):
		pass
	def detect(self, c):
		shape = "unidentified"
		peri = cv2.arcLength(c, True)
		approx = cv2.approxPolyDP(c, 0.04 * peri, True)

		if len(approx) == 3:
			shape = "triangle"
		
		elif len(approx) == 4:
			(x, y, w, h) = cv2.boundingRect(approx)
			aspect_ratio = w / float(h)
			if aspect_ratio >= 0.95 and aspect_ratio <= 1.05:    #this is because approxPolyDP has a variance of 1-5%
				shape = "square"
			elif aspect_ratio >= 0.712 and aspect_ratio <= 0.814:
				shape = "rhombus"
			else:
				shape = "rectangle"  
		
		else:
			(x,y),radius = cv2.minEnclosingCircle(approx)
			center = (int(x),int(y))
			radius = int(radius)
			if len(approx) == 8:
				shape = "circle"
			else:
				shape = "oval"
		
		return shape

image = cv2.imread("img.jpg")
resized = imutils.resize(image, width=300)
ratio = image.shape[0] / float(resized.shape[0])

gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(blurred, 150, 255, cv2.THRESH_BINARY)[1]

cnts = cv2.findContours(thresh.copy(), cv2.RETR_LIST , cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
sd = ShapeDetector()

for c in cnts:
	M = cv2.moments(c)
	
	cX = int((M["m10"] / M["m00"]) * ratio)
	cY = int((M["m01"] / M["m00"]) * ratio)
	
	shape = sd.detect(c)
 	
	c = c.astype("float")
	c *= ratio
	c = c.astype("int")
	cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
	cv2.putText(image, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)


cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()