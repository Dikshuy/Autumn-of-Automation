import cv2
import numpy as np
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0)

while(cap.isOpened()):
    ret, frame = cap.read()
    edges = cv2.Canny(frame,100,200)

    
    cv2.imshow('sketch',edges)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()

