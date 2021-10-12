import os
import shutil
from datetime import datetime
from platform import system

if not os.path.isfile("WORLD"): # Creates the WORLD file that contains the dir name
    with open("WORLD", "x") as d:
        d.write("world")

with open("WORLD", "r") as w:
    WARUDO = w.read() # Reads the file and stores it as a variable 
    WARUDO = WARUDO.replace("\n","") # Removes new lines, since you cannot contain any in a dir

if WARUDO.replace(" ","") == "" or os.path.isdir(WARUDO) == False: # Checks if replacing the spaces with nothing will result in nothing

    while WARUDO.replace(" ","") == "" or os.path.isdir(WARUDO) == False: # While WARUDO is null and the dir mentioned doesn't exist it will loop until both are true
        WARUDO = input("Your world is unreachable, please input your world's name: ")
        WARUDO = WARUDO.replace("\n","")

    with open("WORLD", "w") as s:
        s.write(WARUDO) # Writes the variable in the file for future use

DateAndTime = f"{(str(datetime.now().year).zfill(2))}-{(str(datetime.now().month).zfill(2))}-{(str(datetime.now().day).zfill(2))}_{(str(datetime.now().hour).zfill(2))}-{(str(datetime.now().minute).zfill(2))}-{(str(datetime.now().second).zfill(2))}"
shutil.make_archive(f"{WARUDO}.{DateAndTime}", "zip", WARUDO) # Gets the current date and time and makes it into a zip file