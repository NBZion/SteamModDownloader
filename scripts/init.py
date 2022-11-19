from scripts.steamcmd import checkAndDownloadSteamCmd
import os
import scripts.config as conf
import scripts.steam as steam
import sys
def checkConf():
    if not os.path.exists('./conf.json'):
        with open('conf.json','w') as f:
            f.write('{"inslDir":"","gameId":"","anon":"","logName":"","logPass":""}')
            f.close()
    if not os.path.exists(conf.fetchConf('inslDir')):
        inp=input('Please ReInput path here: ')
        conf.setConf("2",inp)
    if conf.fetchConf('gameId') == "":
        inp=input('Please ReInput desired gameId here: ')
        conf.setConf("1",inp)
    if conf.fetchConf('anon') == "":
        print("DISCLAIMER: ALL INFORMATION AREN'T GATHERED AND IS ONLY STORED IN THE LOCAL MACHINE!")
        inp=input("Want to use anonymous?\n[1]True \n[2]False\nInput:")
        if inp=="1":
            conf.setConf("3","true")
        elif inp=="2":
            conf.setConf("3","false")
        else:
            print('Invalid Choice')
            sys.exit()
    if conf.fetchConf("anon") == "false" and conf.fetchConf("logName") == "":
        name, passc = conf.getCreds()
        print(name)
        print(passc)
        conf.setConf("4",name)
        conf.setConf("5",passc)
def workshop():
    workUrl=input("Input Workshop Url: ")
    urlCheck=steam.modCollectCheck(workUrl)
    if  urlCheck == "mod":
        steam.downMod(workUrl)
    elif urlCheck == "collection":
        steam.downCollect(workUrl)
    else:
        print('Invalid URL')
    print('--------------------------------------------------')
    workshop()
def config():
    print("DISCLAIMER: ALL INFORMATION AREN'T GATHERED AND IS ONLY STORED IN THE LOCAL MACHINE!")
    print('Which of these do you want to change? \n[1]Game Id \n[2]Installation Dir(Where mods are placed)\n[3]Use Anonymous?(type true or false exactly)\n[4]Steam Username\n[5]Steam Password')
    inp=input('Input: ')
    print('--------------------------------------------------')
    print('What value do you want to change it to?')
    val=input('Input: ')
    conf.setConf(inp,val)
def start():
    checkConf()
    checkAndDownloadSteamCmd()
    print('Do you want to [1]Install Mods or [2]Configure the Config?')
    inp=input('Input: ')
    if inp=="1":
        workshop()
    elif inp=="2":
        config()
    else:
        print('Invalid Choice')
        start()
    

    