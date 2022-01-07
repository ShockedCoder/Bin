#!/bin/python

from lang import *

while True:
    try:
        prompt = input("Shell ¶þ ")
        if prompt.lower() == "exit":
            exit(0)
        result, error = run(prompt)

        if error:
            print(error.as_string())
        else:
            print(result)

    except KeyboardInterrupt:
        print()
        exit(0)