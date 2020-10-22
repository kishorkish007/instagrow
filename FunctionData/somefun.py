#Importing Modules
import os
import time

#Clear the Console Func...
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

# define the countdown func.
def countdown(counter_time):
    while counter_time:
        mins, secs = divmod(counter_time, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print("\u001b[33;1mDelay Time Counter\u001b[0m\u001b[31;1m",timer, end="\r\u001b[0m")
        time.sleep(1)
        counter_time -= 1