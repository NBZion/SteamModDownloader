import json
import sys
import os 
from getpass import getpass

def setConf(choice,val):
    confch=None
    if choice=="1":
        confch="gameId"
    elif choice=="2":
        confch="inslDir"
    elif choice=="3":
        confch="anon"
    elif choice=="4":
        confch="logName"
    elif choice=="5":
        confch="logPass"
    else:
        print('Invalid Number')
        sys.exit()
    if choice=="2":
        if not os.path.exists(val) and val!="":
            print('Invalid Path')
            sys.exit()
    js=json.load(open('conf.json'))
    js[confch]=val
    with open('conf.json','w') as f:
        json.dump(js,f,indent=4)
        f.close()
def getCreds():
    nameInp=input("What is your Steam Name?: ")
    passInp=getpass("What is your Steam Password?: ")
    confirmInp=getpass("Re-Enter To Confirm: ")
    if passInp==confirmInp:
        return nameInp, passInp
    else:
        print("Invalid Password, Please Relaunch")
        sys.exit()
def fetchConf(val):
    js=json.load(open('conf.json'))
    return js[val]