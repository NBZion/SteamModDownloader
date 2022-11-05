from scripts.steamcmd import checkAndDownloadSteamCmd
import os
import scripts.config as conf
import scripts.steam as steam
def checkConf():
    if not os.path.exists('./conf.json'):
        with open('conf.json','w') as f:
            f.write('{"inslDir":"","gameId":""}')
            f.close()
    if not os.path.exists(conf.fetchConf('inslDir')):
        inp=input('Please ReInput path here: ')
        conf.setConf("2",inp)
    if conf.fetchConf('gameId') == "":
        inp=input('Please ReInput desired gameId here: ')
        conf.setConf("1",inp)
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
    

    