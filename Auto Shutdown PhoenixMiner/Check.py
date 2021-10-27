#!/bin/python

import os

log = open("./PhoenixMiner.log")

while True:
    logcontent = log.read()
    if "GPU1 is stopped" in logcontent:
        #os.system("shutdown now")
        os.system("killall PhoenixMiner")
        print("It works")
        exit()