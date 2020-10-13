#Importing Modules
import os

#Clear the Console Func...
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")