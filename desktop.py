#!/bin/python

# one line:
# __import__("cv2").imwrite("desktop.png", __import__("cv2").cvtColor(__import__("numpy").array(__import__("pyautogui").screenshot()), __import__("cv2").COLOR_RGB2BGR)[x:1080, x:1920])

import pyautogui
import numpy
import cv2

x, y = 0, 0
w, h = 1920, 1080

img = pyautogui.screenshot()
img = numpy.array(img)
img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
img = img[x:h, y:w]

cv2.imwrite("desktop.png", img)
