# HW12-Lantuejoul’s skeletonization method
'''
    using the structuring element
    (1) square structuring
    (2) cross structuring
'''

import cv2
import numpy as np

# Load the image in grayscale
img = cv2.imread('nice_work.png', 0)
img2 = img
size = np.size(img)

# Threshold the image with threshold value 127
_, img = cv2.threshold(img, 127, 255, 0)
_, img2 = cv2.threshold(img2, 127, 255, 0)

# Using Structure element : square structure & cross structure
# square structure(MORPH_RECT)
square_element = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
done = False   # Not until zeros
suqare_skeleton = np.zeros(img.shape, np.uint8)

# cross structure(MORPH_CROSS)
cross_element = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
done2 = False  # Not until zeros
cross_skeleton = np.zeros(img2.shape, np.uint8)

# Lantuejoul’s Algorithm (Using square structure)
while( not done):
    # opening : erode followed by dilate
    eroded = cv2.erode(img, square_element)
    temp = cv2.dilate(eroded, square_element)
    # Set differences
    temp = cv2.subtract(img, temp)
    # Union differences
    suqare_skeleton = cv2.bitwise_or(suqare_skeleton, temp)
    img = eroded.copy()

    zeros = size - cv2.countNonZero(img)
    if zeros == size:
        done = True  # until zero and stop the function.

cv2.imshow("square_skeleton", suqare_skeleton)

# Lantuejoul’s Algorithm (Using cross structure)
while( not done2):
    # opening : erode followed by dilate
    eroded = cv2.erode(img2, cross_element)
    temp = cv2.dilate(eroded, cross_element)
    # Set differences
    temp = cv2.subtract(img2, temp)
    # Union differences
    cross_skeleton = cv2.bitwise_or(cross_skeleton, temp)
    img2 = eroded.copy()

    zeros = size - cv2.countNonZero(img2)
    if zeros == size:
        done2 = True  # until zero and stop the function.

cv2.imshow("cross_skeleton", cross_skeleton)

cv2.waitKey(0)
cv2.destroyAllWindows()