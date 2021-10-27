#!/bin/python

# The "encrypted" result is just the unicode num version with zfill(7) 
# Don't change anything, I've barely made it work.
# Surprisinly, this is usable as a library
# I've stopped trying to make it not choke if you try to encrypt "-c", so fuck you
#
# P.S. I'm sure I can make it way more optimized, but looking at the amount of work, I'm honestly not arsed
# P.P.S. I might add file support if it seems fun. 

global clipboard

import sys
import warnings; warnings.filterwarnings("ignore"); warnings.simplefilter("ignore")
try: 
    import pyperclip as pc
    clipboard = True
except:
    clipboard = False


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
        if args[0][-1:] != "0" or args[0][:1] != "0":
            return "INVALID INPUT"
        elif args[0] == "0":
            return ""
        else:
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
    cryparg = ""
    usrout = ""
    prompt = False
    confirmation = False

    if len(sys.argv) >= 2:
    
        if "-e" in sys.argv:
            cryparg = "-e"
            
            if len(sys.argv) >= 2 and sys.argv.index(cryparg) != len(sys.argv)-1:

                if sys.argv[sys.argv.index(cryparg)+1] != "-c":
                
                    usrout = encrypt(sys.argv[sys.argv.index(cryparg)+1])
                    print(usrout)
                    confirmation = True
                
                else:

                    usrout = encrypt()
                    print(usrout)
                    confirmation = True
            
            else:

                usrout = encrypt()
                print(usrout)
                prompt = True
    

        elif "-d" in sys.argv:
            cryparg = "-d"
            
            if len(sys.argv) >= 3:

                if sys.argv[sys.argv.index(cryparg)+1] != "-c":
                
                    usrout = decrypt(sys.argv[sys.argv.index(cryparg)+1])
                    print(usrout)
                    confirmation = True

                else:

                    usrout = decrypt()
                    print(usrout)
                    confirmation = True
          
            else:

                usrout = decrypt()
                print(usrout)
                prompt = True


        if "-c" in sys.argv and clipboard and confirmation: # and ("-c" == sys.argv[sys.argv.index(cryparg)-1] or "-c" == sys.argv[sys.argv.index(cryparg)+2])
         
            pc.copy(usrout)
       
        elif "-c" in sys.argv and not clipboard:
        
            print("Install {pyperclip} for the output to be copied to the clipboard")
        
        elif clipboard and prompt:
         
            tocopy = input("Copy output?(Y/n): ").replace(" ", "")
         
            if tocopy not in ("N", "n"):
              
                pc.copy(usrout)

    
    
    else:
        
        choice = input("Encrypt or Decrypt(E/d): ").replace(" ", "")
       
        if choice in ("D", "d"):
            
            usrout = decrypt()
            print(usrout)
    
        else:
            
            usrout = encrypt()
            print(usrout)

       
        if "-c" in sys.argv and clipboard:
         
            try:
           
                pc.copy(usrout)
            
            except:
            
                print("Install {pyperclip} for the output to be copied to the clipboard")
    
        elif not "-c" in sys.argv and clipboard:
            
            tocopy = input("Copy output?(Y/n): ").replace(" ", "")
            
            if tocopy not in ("N", "n"):
              
                pc.copy(usrout)
