#!/bin/python

# New method (Doesn't work)
""" 
changeableWhitelist = (7, "4") # Add your values here
rangelimit = 10000 # The limit for the numbers


# Do not touch anything under this line
# -------------------------------------------------------#
numlist = []
whitelist = []


for num in changeableWhitelist:
    try:
        whitelist.append(str(int(num))) # Tries to add nums into a whitelist, whilst conveting them into ints
    except ValueError:
        print("The values must be ints") # If the values aren't ints, it will raise this error
        exit()

def Solution():
    for i in range(1,rangelimit+1):
        string = str(i)
        for num in whitelist:
            if num in string:
                try:
                    for char in string:
                        try:
                            for num in whitelist:
                                if char != num:
                                    raise ValueError
                        except ValueError:
                            pass
                except ValueError:
                    pass
                else:
                    numlist.append(i)

    for num in numlist:
        comparelist=[]
        for int in whitelist:
            if int in str(num):
                comparelist.append(int)
                if len(comparelist) == len(whitelist):
                    print(num)

if len(whitelist) != 0:
    try:
        for num in whitelist:
            if len(num) != 1:
                print("The values in the whilelist must be single-digit ints")
                raise ValueError
    except ValueError:
        pass
    else:
        Solution()
else:
    print("The whitelist cannot be empty.")
"""

#-----------------------------------------------------------------------------------------#
#----------------  _____ _                           _     _ _       _    ----------------#
#---------------- |_   _( )                         (_)   | (_)     | |   ----------------#
#----------------   | | |/ _ __ ___     __ _ _ __    _  __| |_  ___ | |_  ----------------#
#----------------   | |   | '_ ` _ \   / _` | '_ \  | |/ _` | |/ _ \| __| ----------------#
#----------------  _| |_  | | | | | | | (_| | | | | | | (_| | | (_) | |_  ----------------#
#---------------- |_____| |_| |_| |_|  \__,_|_| |_| |_|\__,_|_|\___/ \__| ----------------#
#-----------------------------------------------------------------------------------------#


# Old method
unsortedlist = []

for i in range(1,10001):
    string = str(i)
 
    if "7" in string or "4" in string:
        try:
            for a in string:
                if a != "7" and a != "4":
                    raise Exception
        except:
            pass
        else:
            unsortedlist.append(i)
        
        
sortedlist = sorted(unsortedlist)


for num in sortedlist:
    print(num)
        