# -*- coding: utf-8 -*-

# Computer Vision Course (CSE 40535/60535)
# University of Notre Dame, Fall 2024
# ________________________________________________________________
# Adam Czajka, Andrey Kuehlkamp, September 2017 - 2024

# Here are your tasks:
#
# Task 2a:
# - Select one object that you want to track and set the RGB
#   channels to the selected ranges (found by colorSelection.py).
# - Check if HSV color space works better. Can you ignore one or two
#   channels when working in HSV color space? Why?
# ANSWER: I found that HSV works better. I would assume this is because it tracks intensity better which can better detct
# object in bad lighting. Ignoring the V channel helps in dynamic lighting conditions
# - Try to track candies of different colors (blue, yellow, green).
# ANSWER: when presenting two objects of the same color, the program only recognizes the one that has moved most recently
# It will hop back and forth between the two if they are moving around. When putting up 2 different colors, it ignores the
# color I was not trying to track
# Task 2b:
# - Adapt your code to track multiple objects of *the same* color simultaneously, 
#   and show them as separate objects in the camera stream.
#
# Task 2c:
# - Adapt your code to track multiple objects of *different* colors simultaneously,
#   and show them as separate objects in the camera stream. Make your code elegant 
#   and requiring minimum changes when the number of different objects to be detected increases.
#


import cv2
import numpy as np
cam = cv2.VideoCapture(0)

while (True):
    retval, img = cam.read()

    res_scale = 0.5 # rescale the input image if it's too large
    img = cv2.resize(img, (0,0), fx = res_scale, fy = res_scale)


    #######################################################
    # Use hsvSelection.py to find good color ranges for your object(s):

    # Uncomment this if you want to use HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    colorRanges = {
        "green": ([40, 50, 0], [90, 200, 255], (0, 255, 0)),
        "red": ([170, 150, 0], [180, 180, 255], (0, 0, 255)),
        "blue": ([90, 140, 0], [110, 175, 255], (255, 0, 0)),
        "yellow": ([0, 90, 0], [25, 150, 255], (0, 255,255)),

    }

    # Resulting binary image may have large number of small objects.
    # You may check different morphological operations to remove these unnecessary
    # elements. You may need to check your ROI defined in step 1 to
    # determine how many pixels your object may have.
    kernel = np.ones((5,5), np.uint8)
    for color_name, (lower, upper, brgColor) in colorRanges.items():
        # Create binary mask for the current color
        lower_bound = np.array(lower, dtype=np.uint8)
        upper_bound = np.array(upper, dtype=np.uint8)
        mask = cv2.inRange(hsv, lower_bound, upper_bound)

        # Apply operations to clean  mask
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, kernel)

        # Find contours
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2:]

        # We are using [-2:] to select the last two return values from the above function to make the code work with
        # both opencv3 and opencv4. This is because opencv3 provides 3 return values but opencv4 discards the first.

        # Ignore bounding boxes smaller than "minObjectSize"
        minObjectSize = 20

        #######################################################
        # TIP: think if the "if" statement
        # can be replaced with a "for" loop

        for contour in contours:
            # Use just the first contour to draw a rectangle
            x, y, w, h = cv2.boundingRect(contour)

            # Do not show very small objects
            if w > minObjectSize or h > minObjectSize:
                cv2.rectangle(img, (x, y), (x+w, y+h), brgColor, 3)
                cv2.putText(img,            # image
                color_name,        # text
                (x, y-10),                  # start position
                cv2.FONT_HERSHEY_SIMPLEX,   # font
                0.7,                        # size
                brgColor,                # BGR color
                1,                          # thickness
                cv2.LINE_AA)                # type of line
        cv2.imshow(f"{color_name} mask", mask)
    cv2.imshow("Live WebCam", img)

    action = cv2.waitKey(1)
    if action & 0xFF == 27:
        break

cam.release()
cv2.destroyAllWindows()


























