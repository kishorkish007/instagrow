#Color and Codes
COLORS = {\
"black":"\u001b[30;1m",
"red": "\u001b[31;1m",
"green":"\u001b[32m",
"yellow":"\u001b[33;1m",
"blue":"\u001b[34;1m",
"magenta":"\u001b[35m",
"cyan": "\u001b[36m",
"white":"\u001b[37m",
"yellow-background":"\u001b[43m",
"black-background":"\u001b[40m",
"cyan-background":"\u001b[46;1m",
"red-background": "\u001b[41m",
"reset":"\u001b[0m",
}

def colorText(text):
    for color in COLORS:
        text = text.replace("[[" + color + "]]", COLORS[color])
    return text

#KMF LOGO OR ASSCCI HEADER
def KMFHEADER():
    f = open('./MokupData/' "KMFHeader.txt","r")
    KMFHEADER = "".join(f.readlines())
    print(colorText(KMFHEADER))

# BOT LOGIN PAGE
def BOTLOGIN():
    f = open('./MokupData/' "BOTLOGIN.txt","r")
    BOTLOGIN = "".join(f.readlines())
    print(colorText(BOTLOGIN))


#Options ASSCCI HEADER
def OPTIONLIST():
    f = open('./MokupData/' "OPTIONLIST.txt","r")
    OPTIONLIST = "".join(f.readlines())
    print(colorText(OPTIONLIST))

#TEAMHUNTER
def TEAMHUNTER():
    f = open('./MokupData/' "TEAMHUNTER.txt","r")
    TEAMHUNTER = "".join(f.readlines())
    print(colorText(TEAMHUNTER))

#NONFOLLOWERS
def NONFOLLOWERS():
    f = open('./MokupData/' "NONFOLLOWERS.txt","r")
    NONFOLLOWERS = "".join(f.readlines())
    print(colorText(NONFOLLOWERS))

#NONFOLLOWERS
def INSTRUCTIONS():
    f = open('./MokupData/' "INSTRUCTIONS.txt","r")
    INSTRUCTIONS = "".join(f.readlines())
    print(colorText(INSTRUCTIONS))

#REHASHTAG
def REHASHTAG():
    f = open('./MokupData/' "REHASHTAG.txt","r")
    REHASHTAG = "".join(f.readlines())
    print(colorText(REHASHTAG))

#MASSLOOKER
def MASSLOOKER():
    f = open('./MokupData/' "MASSLOOKER.txt","r")
    MASSLOOKER = "".join(f.readlines())
    print(colorText(MASSLOOKER))

#PROFILE_SCRAPER
def PROFILE_SCRAPER():
    f = open('./MokupData/' "PROFILE_SCRAPER.txt","r")
    PROFILE_SCRAPER = "".join(f.readlines())
    print(colorText(PROFILE_SCRAPER))

#OFFLINE
def OFFLINE():
    f = open('./MokupData/' "OFFLINE.txt","r")
    OFFLINE = "".join(f.readlines())
    print(colorText(OFFLINE))

#DONATE
def DONATE():
    f = open('./MokupData/' "DONATE.txt","r")
    DONATE = "".join(f.readlines())
    print(colorText(DONATE))

#INSHACKLE
def INSHACKLE():
    f = open('./MokupData/' "INSHACKLE.txt","r")
    INSHACKLE = "".join(f.readlines())
    print(colorText(INSHACKLE))


#FEEDLIKER
def FEEDLIKER():
    f = open('./MokupData/' "FEEDLIKER.txt","r")
    FEEDLIKER = "".join(f.readlines())
    print(colorText(FEEDLIKER))

#LOGOUT
def LOGOUT():
    f = open('./MokupData/' "LOGOUT.txt","r")
    LOGOUT = "".join(f.readlines())
    print(colorText(LOGOUT))


#DIRECTMESSAGE
def DIRECTMESSAGE():
    f = open('./MokupData/' "DIRECTMESSAGE.txt","r")
    DIRECTMESSAGE = "".join(f.readlines())
    print(colorText(DIRECTMESSAGE))