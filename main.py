#Importing Modules
import requests

#Importing Mi Func...
from FunctionData.somefun import clear
from MokupData.mokupfun import *
from BotData.MainBot import MainBot

#Status
KMFstatus = ("online")
KMFstatuschecker = requests.get('https://docs.google.com/spreadsheets/d/1pzEXH9XhRenwWh0wMokkbJtw8-Uvm_6rVsvXhuw6qKw/edit?usp=sharing')

#Program Started
clear()
KMFHEADER()
if KMFstatus in KMFstatuschecker.text:
    MainBot()
    
else:
    OFFLINE()
    DONATE()