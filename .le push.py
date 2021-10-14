import os
import random

with open(".gitcommit_msglist", "r") as f:
    lsit = [i.replace("\n", "") for i in list(f)]

os.system("git add .")
os.system(f"git commit -m \"{lsit[random.randint(0, len(lsit)-1)]}\"")
os.system("git push")
os.system("zenity --info --no-wrap --ellipsize --text=\"the pushing has been done\"")