# The "encrypted" result is just the unicode num version with zfill(7) 
# Don't change anything, I've barely made it work.
# Surprisinly, this is usable as a library

import sys
import warnings
warnings.filterwarnings("ignore")
warnings.simplefilter("ignore")
global clipboard
try: 
    import pyperclip
    clipboard = True
    
except ImportError:
    clipboard = False
    print("Install {pyperclip} for the output to be copied to the clipboard")


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
    cryparg = ""
    usrout = ""

    try:
        if "-e" in sys.argv:
            cryparg = "-e"
            if sys.argv[sys.argv.index("-e")+1]:
                usrout = encrypt(sys.argv[sys.argv.index("-e")+1])
                print(usrout)
            else:
                print(encrypt())
        elif "-d" in sys.argv:
            cryparg = "-d"
            if sys.argv[sys.argv.index("-d")+1]:
                usrout = decrypt(sys.argv[sys.argv.index("-d")+1])
                print(usrout)
            else:
                usrout = decrypt()
                print(usrout)
        
        if clipboard:
            if "-c" in sys.argv and "-c" != sys.argv[sys.argv.index(cryparg)+1]:
                pyperclip.copy(usrout)
    except Exception as e:
        while True:
            choice = input("Encrypt or Decrypt(e/d): ")
            if choice.lower() == "e":
                encryption = True
                break
            elif choice.lower() == "d":
                decryption = True
                break
            
            
        if encryption:
            usrout = encrypt()
            print(usrout)
        elif decryption:
            usrout = decrypt()
            print(usrout)

        if clipboard:
            if "-c" in sys.argv:
                pyperclip.copy(usrout)