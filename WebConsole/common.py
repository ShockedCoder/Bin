#!/bin/python

import os
import requests

_pathdir = os.path.dirname(os.path.realpath(__file__)) + "/"

""" INVALID (unless old console is used) """
# def getcommand(command):
#     output = requests.get(f"http://localhost:5001/api/command/{command}").content
#     string = str(output)
#     cropped = string[2:][:-3].replace("\\n", "\n")
#     formatted = cropped.replace("\\\\", "\\")
#     moreformat = formatted.replace("\\\\", "\\")
#     evenmoreformat = moreformat.replace("\\\n", "\\n")
#     return evenmoreformat
#     # return str(requests.get(f"http://localhost:5001/api/command/{command}").content)[2:][:-3].replace("\\n", "\n").replace("\\\\", "\\").replace("\\\\", "\\").replace("\\\n", "\\n")

def getcommand(command):
        return requests.post(url="http://localhost:5001/api", data=command).content.decode()[:-1]

def jason(): # TODO: Create this function.
    return