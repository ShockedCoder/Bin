#!/bin/python

patternSize = 5

line = "# " * patternSize * 2
line = line.replace(" ", ".")
line2 = ". " * patternSize * 2
line2 = line2.replace(" ", "#")
count = ""

for i in range(patternSize):
    if len(count) < patternSize * patternSize:
        print(line[:patternSize])
        count += line[:patternSize]
        # print(len(count))
        if len(count) < patternSize * patternSize:
            print(line2[:patternSize])
            count += line2[:patternSize]
            # print(len(count))


# print("-----------------------------------")
# print(count)
# print(len(count))

