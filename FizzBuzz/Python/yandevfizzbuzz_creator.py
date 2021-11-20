#!/bin/python

amount = 100

file = open("yandevfizzbuzz.py", "w")
file.write("#!/bin/python\n\n")
file.write(f"for num in range(1, {amount+1}):\n")

for num in range(1, amount+1):
    if num % 3 == 0 and num % 5 == 0:
        file.write(f"\tif num == {num}:\n\t\tprint(\"FizzBuzz\")  #FizzBuzz\n")
    elif num % 3 == 0:
        file.write(f"\tif num == {num}:\n\t\tprint(\"Fizz\")  #Fizz\n")
    elif num % 5 == 0:
        file.write(f"\tif num == {num}:\n\t\tprint(\"Buzz\")  #Buzz\n")
    else:
        file.write(f"\tif num == {num}:\n\t\tprint(\"{num}\")\n")

file.close()
