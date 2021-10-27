import cv2
import numpy as np



# load and preprocessing
image = cv2.imread('text/holo.jpeg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# blur = cv2.GaussianBlur(gray, (9,9), 0)
thresh = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,11,30)
cv2.imshow("ss", thresh)
cv2.waitKey(0)