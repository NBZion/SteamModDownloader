from scripts.steamcmd import checkAndDownloadSteamCmd
import os
import scripts.config as conf
import scripts.steam as steam
def checkPath():
    if not os.path.exists(conf.fetchConf('inslDir')):
        inp=input('Please Reinput path here: ')
        conf.setConf("2",inp)
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
    print('Which of these do you want to change? \n [1]Game Id \n [2]Installation Dir(Where mods are placed)')
    inp=input('Input: ')
    print('--------------------------------------------------')
    print('What value do you want to change it to?')
    val=input('Input: ')
    conf.setConf(inp,val)
def start():
    checkPath()
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
    

    