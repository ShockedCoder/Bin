import os
import getpass
usrname = os.getlogin()
runner = getpass.getuser()

print("Hello!\n")
if runner == "root":
    print("I won't ask why you'd run this as root, but you're pretty dumb for doing it")
elif runner == usrname:
    print("Running this normally I see you're not that dumb.")
# usrname = input("What's your name?: ")
usrname = usrname.title()
print(f"\nIt's nice to meet you, {usrname}!")
print(f"Did you know that your name is {len(usrname)} letters long?")
usrage = input("\nHow old are you?: ")
if int(usrage) >= 80:
    print("You're funny.")
else:
    print(f"That means you'll be {str(int(usrage) + 1)} in a year or less.")