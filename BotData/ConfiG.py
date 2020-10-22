from MokupData.mokupfun import *
from FunctionData.somefun import *

# After Login Displaying Options
def Option():
    KMFHEADER()
    OPTIONLIST()
    while True:
        try:
            usrInp = input("\u001b[32m[+]\u001b[0m Enter Input:-")
            # If statment for option selection
            if usrInp == "1":
                clear()
                from BotData.MainBot import ig_teamhunter
                ig_teamhunter()

            if usrInp == "2":
                clear()
                from BotData.MainBot import ig_masslooker
                ig_masslooker()

            if usrInp == "3":
                clear()
                from BotData.MainBot import ig_rehashtag
                ig_rehashtag()

            if usrInp == "4":
                clear()
                from BotData.MainBot import ig_feedliker
                ig_feedliker()

            if usrInp == "5":
                clear()
                from BotData.MainBot import ig_inshackle
                ig_inshackle()

            if usrInp == "6":
                clear()
                from BotData.MainBot import ig_directmessage
                ig_directmessage()

            if usrInp == "7":
                clear()
                from BotData.MainBot import ig_nonfollowers
                ig_nonfollowers()

            if usrInp == "8":
                clear()
                from BotData.MainBot import ig_ProfileScraper
                ig_ProfileScraper()

            if usrInp == "9":
                clear()
                KMFHEADER()
                INSTRUCTIONS()
                DONATE()
                BackInp = input("\u001b[32m[+]\u001b[0m Enter Key to Main Menu ")
                if BackInp == "":
                    clear()
                    Option()
                else:
                    clear()
                    Option()

            if usrInp == "10":
                clear()
                KMFHEADER()
                LOGOUT()
                from BotData.MainBot import LogOut
                LogOut()

            else:
                from BotData.MainBot import ELSE_BOT
                ELSE_BOT()
        except KeyboardInterrupt:
            break
            clear()
            Option()
    clear()
    Option()