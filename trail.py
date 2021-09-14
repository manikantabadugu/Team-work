import cv2
import matplotlib.pyplot as plt
import numpy as np

image_path = r"C:\Users\User\Documents\GitHub\practice folders\module-6\Team-work\test_images\solidYellowLeft.jpg"
image1 = cv2.imread(image_path)
image= image1.copy()


img_gray= cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
img_blur= cv2.GaussianBlur(img_gray, (7,7),0)

img_edge = cv2.Canny(img_blur,70,140)


def region(image):
    height, width = image.shape
    #isolate the gradients that correspond to the lane lines
    triangle = np.array([
                       [(0, height), (width//2,round(height//1.75)), (width, height)]
                       ])
    #create a black image with the same dimensions as original image
    mask = np.zeros_like(image) 
    #create a mask (triangle that isolates the region of interest in our image)
    mask = cv2.fillPoly(mask, triangle, 255)
    mask = cv2.bitwise_and(image, mask)
    return mask

cv2.imshow('image copy', region(img_edge))
cv2.waitKey()

