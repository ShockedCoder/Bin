#!/bin/python

patternSize = 4

string_1 = ""
string_2 = ""

string_1_finished = False
string_2_finished = False

for a in range(patternSize):

    if (a % 2 == 0):
        while (not string_1_finished):
            if (len(string_1) < patternSize):
                string_1 = string_1 + "#"
                if (len(string_1) < patternSize):
                    string_1 = string_1 + "."
                else:
                    string_1_finished = True
                    break

    else:
        while (not string_2_finished):
            try:
                string_2 = string_2 + "."
            except:
                string_2 = "."

            if (len(string_2) < patternSize):
                string_2 = string_2 + "#"
            else:
                string_2_finished = True
                break


if (string_1_finished and string_2_finished):
    for amount in range(patternSize):
        if (amount % 2 == 0):
            print(string_1)
        else:
            print(string_2)
