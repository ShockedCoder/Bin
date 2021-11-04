from random import randint
import os

words = [["että", "att"],
         ["kun", "när"],
         ["vaikka", "fast"],
         ["koska", "eftersom"],
         ["jos", "om"]]

correct = 0
incorrect = 0
usrin = ""

def clear():
    os.system("clear")
clear()

while True:

    print(f"Times Correct:   {correct}")
    print(f"Times Incorrect: {incorrect}")

    if randint(0,1) == 0:
        num = randint(0, len(words)-1)
        usrin = input(f"What is the swedish equvilant of \"{words[num][0]}\"?: ")
        if usrin.lower().replace(" ", "") == words[num][1]:
            clear()
            print("CORRECT!")
            correct += 1
        elif usrin.lower().replace(" ", "") == "q":
            break
        else:
            clear()
            print("INCORRECT!")
            incorrect += 1
    
    else:
        num = randint(0, len(words)-1)
        usrin = input(f"What is the finnish equvilant of \"{words[num][1]}\"?: ")
        if usrin.lower().replace(" ", "") == words[num][0]:
            clear()
            print("CORRECT!")
            correct += 1
        elif usrin.lower().replace(" ", "") == "q":
            break
        else:
            clear()
            print("INCORRECT!")
            incorrect += 1