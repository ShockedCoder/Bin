#!/bin/python

import os
# import zipfile
import shutil
import platform
from datetime import datetime
from rich import console

maxLength = 35
Zeroed = ["", " ", None]

if platform.system() == "Windows":
    Windows = True
else:
    Windows = False
    
def clear():
    if Windows:
        os.system("cls")
    else:
        os.system("clear")
clear()


while os.path.isfile("WORLD") == False:
    WORLDfiles = input(f"Please input a new directory ({maxLength} max): ")
    if os.path.isfile(WORLDfiles) == False:
        clear()
        console.print("Please input an existing directory.")

cusWORLD = open("WORLD","w+")
cusWORLD.write(WORLDfiles)
cusWORLD.close()

cusWORLD = open("WORLD","r")
WORLDfiles = cusWORLD.read()
cusWORLD.close()

WORLDfiles = WORLDfiles.replace(".","")
WORLDfiles = WORLDfiles.replace(",","")
WORLDfiles = WORLDfiles.replace("'","")
WORLDfiles = WORLDfiles.replace("\"","")
WORLDfiles = WORLDfiles.replace("/","")
WORLDfiles = WORLDfiles.replace("\\","")
WORLDfiles = WORLDfiles.replace("*","")
WORLDfiles = WORLDfiles.replace("+","")
WORLDfiles = WORLDfiles.replace("´","")
WORLDfiles = WORLDfiles.replace("<","")
WORLDfiles = WORLDfiles.replace(">","")
WORLDfiles = WORLDfiles.replace(":","")
WORLDfiles = WORLDfiles.replace(";","")
WORLDfiles = WORLDfiles.replace("~","")
WORLDfiles = WORLDfiles.replace("^","")
WORLDfiles = WORLDfiles.replace("|","")
WORLDfiles = WORLDfiles.replace("§","")
WORLDfiles = WORLDfiles.replace("½","")
WORLDfiles = WORLDfiles.replace("?","")
WORLDfiles = WORLDfiles.replace("!","")
WORLDfiles = WORLDfiles.replace("=","")
WORLDfiles = WORLDfiles.replace("]","")
WORLDfiles = WORLDfiles.replace("[","")
WORLDfiles = WORLDfiles.replace("}","")
WORLDfiles = WORLDfiles.replace("{","")
WORLDfiles = WORLDfiles.replace("(","")
WORLDfiles = WORLDfiles.replace(")","")
WORLDfiles = WORLDfiles.replace("&","")
WORLDfiles = WORLDfiles.replace("%","")
WORLDfiles = WORLDfiles.replace("€","")
WORLDfiles = WORLDfiles.replace("£","")
WORLDfiles = WORLDfiles.replace("$","")
WORLDfiles = WORLDfiles.replace("#","")
WORLDfiles = WORLDfiles.replace("@","")
WORLDfiles = WORLDfiles.replace("¤","")
WORLDfiles = WORLDfiles.replace("`","")
WORLDfiles = WORLDfiles.replace("'","")
WORLDfiles = WORLDfiles.replace(" ","")

while len(WORLDfiles) > maxLength:
    lengthClarification = input(f"{WORLDfiles}({len(WORLDfiles)}) is too long of a name ({maxLength} max)\nIt will be shortened to {WORLDfiles[:maxLength]}.\nAccept? (Y/n): ")
    if lengthClarification.lower() == "y" or None or "" or " ":
        if Windows:
            os.system("copy WORLD WORLD.old")
        else:
            os.system("cp WORLD WORLD.old")
        WORLDfiles = WORLDfiles[:maxLength]
        cusWORLD = open("WORLD", "w+")
        cusWORLD.write(WORLDfiles)
        cusWORLD.close()

if os.path.isfile("Yesth") == False:
    clarification = input(f"Is {WORLDfiles} the correct directory? (Y/n): ")
    if clarification.lower() == "y" or None or "" or " ":
        if Windows:
            os.system("type nul > Yesth")
        else:
            os.system("touch Yesth")
    elif clarification.lower() == "n":
        console.print("null")


if WORLDfiles in Zeroed:
    console.print("You're hopeless at this point.")
    exit()
else:
    DateAndTime = f"{(str(datetime.now().day).zfill(2))}-{(str(datetime.now().month).zfill(2))}-{(str(datetime.now().year).zfill(2))}_{(str(datetime.now().hour).zfill(2))}-{(str(datetime.now().minute).zfill(2))}-{(str(datetime.now().second).zfill(2))}"
    shutil.make_archive(f"{WORLDfiles}.{DateAndTime}", "zip", f"{WORLDfiles}")

## zipfile is files only and doesn't support entire folders, as far as I know
# with zipfile.ZipFile(f"{WORLDfiles}.{DateAndTime}.zip", "w", compression=zipfile.ZIP_DEFLATED) as backup:
#     backup.write(f"{WORLDfiles}")
