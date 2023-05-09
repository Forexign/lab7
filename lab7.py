import cv2
import numpy as np

image = cv2.imread('colourful.jpeg')
b, g, r = cv2.split(image)

cv2.imshow('Blue Image', b)
cv2.resizeWindow('Blue Image', 600, 300)
cv2.imshow('Green Image', g)
cv2.resizeWindow('Green Image', 600, 300)
cv2.imshow('Red Image', r)
cv2.resizeWindow('Red Image', 600, 300)

redBlueImage = cv2.merge([b, np.zeros_like(g), r])
cv2.imshow('Red-Blue Image', redBlueImage)
cv2.resizeWindow('Red-Blue Image', 1800, 300)

originalImage = cv2.merge([b, g, r])
cv2.imshow('Combined Image', originalImage)
cv2.resizeWindow('Combined Image', 1800, 300)

cv2.waitKey(0)
cv2.destroyAllWindows()
