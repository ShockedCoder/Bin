#!/bin/python

""" To-Do List """
# DONE: Make it work for multi-char wrappers e.g.: "<!-- -->"


""" Imports """
import re
from sys import argv, exit


""" Variables """
wrapper = ('{', '}')
# teststr = "{Heeheehaahaa{How about two?}}"
# wrapper = ("<!--", "-->")
# teststr = "Html comment tags <!-- Apples, apples everywhere <!-- <!---->  --> -->"


""" Functions """
def wrapperparser(string:str, leftoff:int = 0, returnall:bool = True) -> tuple | bool | list:
    if len(wrapper[0]) == 1 and len(wrapper[1]) == 1:
        ex_op = 0 # Extra Open
        if returnall:
            thung = []
    
        for i, char in enumerate(string[leftoff+1:], leftoff+1):
            if char == wrapper[0]:
                ex_op += 1
                if returnall:
                    thung.append(wrapperparser(string, i))
            elif char == wrapper[1]:
                if ex_op == 0:
                    if returnall:
                        return thung
                    else:
                        return (leftoff, i)
                else:
                    ex_op -= 1
        return False
    else:
        try:
            return re.search(wrapper[0] + r".*" + wrapper[1], string).span()
        except:
            return False
    

""" Main """
if __name__ == "__main__":
    if len(argv) >= 2:
        if type(argv[1]) == str:
            print(wrapperparser(argv[1]))
        else:
            exit(2)
    else:
        exit(2)

