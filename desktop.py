#!/bin/python
import pyautogui as p
import cv2 as c
import numpy as n

img = p.screenshot()
img = c.cvtColor(n.array(img), c.COLOR_RGB2BGR)
img = img[0:1080, 0:1920]

c.imwrite("desktop.png", img)
