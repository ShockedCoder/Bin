# The "encrypted" result is just the unicode num version with zfill(7) 
# Don't change anything, I've barely made it work.
# Surprisinly, this is usable as a library

import sys

leadingZeros = 7


def encrypt(*args):
    usrin = ""
    encrypted = ""
    if len(args) == 1:
        usrin = args[0]
    else:
        usrin = input("To Encrypt >> ")
    ordlist = []
    
    for i in usrin:
        ordlist.append(str(ord(i)).zfill(leadingZeros))
    ordlist.append("0")
    
    for i in ordlist:
        encrypted += str(i)
    return encrypted


def decrypt(*args):
    usrin = ""
    decrypted = ""
    if len(args) == 1:
        usrin = args[0]
    else:
        usrin = input("To Decrypt >> ")
    ordlist = []
    chrlist = []
    limit = 0
    result = ""

    for i in range(len(usrin)):
        if limit == leadingZeros:
            ordlist.append(int(result))
            limit = 0
            result = ""
        result += str(usrin[i])
        limit += 1

    for i in ordlist:
        chrlist.append(chr(i))

    for i in chrlist:
        decrypted += str(i)
    return decrypted



if __name__ == "__main__":
    choice = ""
    encryption = decryption = False

    try:
        if sys.argv[1] == "-e":
            if len(sys.argv) < 3:
                print(encrypt())
            else:
                print(encrypt(sys.argv[2]))
        elif sys.argv[1] == "-d":
            if len(sys.argv) < 3:
                print(decrypt())
            else:
                print(decrypt(sys.argv[2]))
    except:
        while True:
            choice = input("Encrypt or Decrypt(e/d): ")
            if choice.lower() == "e":
                encryption = True
                break
            elif choice.lower() == "d":
                decryption = True
                break

        if encryption:
            print(encrypt())
        elif decryption:
            print(decrypt())