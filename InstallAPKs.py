#!/bin/python

import os
#import re

# https://code.activestate.com/recipes/577252-lreplace-and-rreplace-replace-the-beginning-and-en/

"""Either this doesn't work or I'm using it wrong"""
# def lreplace(pattern, sub, string):
#     """
#     Replaces 'pattern' in 'string' with 'sub' if 'pattern' starts 'string'.
#     """
#     #return re.sub('^%s' % pattern, sub, string)
#     return string[:len(pattern)] + sub if string.startswith(pattern) else string

# def rreplace(pattern, sub, string):
#     """
#     Replaces 'pattern' in 'string' with 'sub' if 'pattern' ends 'string'.
#     """
#     #return re.sub('%s$' % pattern, sub, string)
#     return string[-len(pattern):] + sub if string.endswith(pattern) else string

# os.system("rm tmp.log")

APKlist = os.listdir()

for item in APKlist:
    if not item.endswith(".apk"):
        APKlist.remove(item)
APKlist.remove(__file__[len(os.path.dirname(os.path.realpath(__file__)) + "/"):])

for package in APKlist:
   os.system(f"adb install -r {package}") # | tee -a tmp.log")

# with open("tmp.log", "r") as f:
#     apple = [word.replace(" ", "") for word in f.read().split("\n")]
# while "" in apple:
#     apple.remove("")
# #apple = [apple.remove(word) if len(word) == 0 else word for word in apple]

# if len(APKlist) != apple.count("Success"):
#     print("Something went wrong")
