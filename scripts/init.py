from scripts.steamcmd import checkAndDownloadSteamCmd
import os, sys
import json
import scripts.config as conf
import scripts.steam as steam
from tkinter import Tk
from tkinter.filedialog import askdirectory
from sys import exit
from bs4 import BeautifulSoup
import requests


def checkVersion():
    currentVersion = open('version.txt','r').readline()
    listedVersion = requests.get("https://raw.githubusercontent.com/NBZion/SteamModDownloader/master/version.txt").text

    if currentVersion != listedVersion:
        print("[WARNING] Please update SMD with smd update!")
        print("Client Version: " + currentVersion)
        print("Listed Version: " + listedVersion)
        print("--------------------------------------------------")

    
def checkConfig():
    # Make configuration file if missing
    if not os.path.exists('./conf.json'):
        with open('conf.json', 'w') as f:
            f.write('{"downloadDir":"","anonymousMode":"","steamAccountName":"","steamPassword":"","gameID":"","os":""}')

    # Reconfigure download directory setting if invalid
    if not os.path.exists(conf.fetchConfiguration('downloadDir')):  
        print('Non-existent mod download directory, please enter a new one => ')
        prompt=None
        if sys.stdout.isatty():
            prompt=input()
        else:
            try:
                Tk().withdraw()
                prompt = askdirectory() 
            except ImportError:
                print('(ERROR) TKInter not installed, resulting to default(Type mod download directory manually).')
                prompt=input()
        
        conf.configureSetting('downloadDir', prompt)

    # Reconfigure gameID if empty
    if conf.fetchConfiguration('gameID') == "":
        prompt = input('gameID setting empty, please enter a new one => ')
        conf.configureSetting('gameID', prompt)

    # Reconfigure anonymous mode if empty
    if conf.fetchConfiguration('anonymousMode') == "":
        print("(DISCLAIMER) Information isn't gathered, and is only stored locally.")
        anonymous = input("Use anonymous mode? [Y\\N]\n> ").lower()
        if anonymous == "y":
            conf.configureSetting('anonymousMode', "true")
        elif anonymous == "n":
            conf.configureSetting('anonymousMode', "false")
        else:
            print('(ERROR) Invalid input passed, exiting.')
            exit()

    # Check if anonymous mode is off and ask for credentials
    if conf.fetchConfiguration("anonymousMode") == "false" and conf.fetchConfiguration("steamAccountName") == "":
        username, password = conf.getCredentials()
        conf.configureSetting('steamAccountName', username)
        conf.configureSetting('steamPassword', password)

    # Set OS if empty
    if conf.fetchConfiguration("os") == "":
        conf.configureSetting('os', sys.platform)

def downloadMods():
    while True:
        workshopURL = input("Mod/Collection Workshop URL: ")
        workshopURLType = steam.checkType(workshopURL)
        if workshopURLType == "mod":
            print('(PROCESS) Downloading mod...')
            steam.downloadMod(workshopURL)
            break
        elif workshopURLType == "collection":
            print('(PROCESS) Downloading collection...')
            steam.downloadCollection(workshopURL)
            break
        else:
            print('(ERROR) Invalid URL, awaiting new.')
    #print('--------------------------------------------------')

def listMods():
    print("--------------------------------------------------")
    print("MODS IN '"+conf.fetchConfiguration("downloadDir")+"'...\n")
    for dir in os.listdir(conf.fetchConfiguration('downloadDir')):
        smbDir=os.path.join(conf.fetchConfiguration('downloadDir'),os.path.join(dir, 'smbinfo.json'))
        if os.path.exists(smbDir):
            jsonData=json.load(open(smbDir, 'r'))
            print(jsonData['name'])
        else:
            # Very Slow, Might Fix Soon
            url="https://steamcommunity.com/sharedfiles/filedetails/?id="+dir
            try:
                res = requests.get(url)
                doc = BeautifulSoup(res.text, "html.parser")
                title = doc.head.title.text.split("::")[1]
                print(title, "(MODID: "+dir+")")
            except:
                print("(ERROR) Invalid URL, awaiting new.")
    print("--------------------------------------------------")

def configure():
    print("(DISCLAIMER) Information isn't gathered, and is only stored locally.")
    print(
        'Setting List:\n'
        '[1] Game ID \n'
        '[2] Download Directory\n'
        '[3] Anonymous Mode\n'
        '[4] Steam Username\n'
        '[5] Steam Password'
    )
    prompt = input('> ')
    #print('--------------------------------------------------')
    print('What value do you want to change it to?')
    if prompt == '2' and not sys.stdout.isatty():
        Tk().withdraw()
        value = askdirectory()
    else:
        value = input('> ')
    match prompt:
        case '1':
            setting='gameID'
        case '2':
            setting='downloadDir'
        case '3':
            setting='anonymousMode'
        case '4':
            setting='steamAccountName'
        case '5':
            setting='steamPassword'
        case _:
            print('(ERROR) Invalid setting id, exiting.')
            exit()
    conf.configureSetting(setting, value)
    start()

def start():
    checkVersion()
    checkConfig()
    checkAndDownloadSteamCmd()
    while True:
        print('Welcome to SWD!')
        print('[1] => Download Mods\n[2] => List Mods\n[3] => Open Settings\n[4] => Exit')
        prompt = input('> ')
        if prompt == '1':
            downloadMods()
            break
        elif prompt == '2':
            listMods()
        elif prompt == '3':
            configure()
            break
        elif prompt == '4':
            exit()
        else:
            print('(ERROR) Invalid option passed, exiting.')
            exit()
start()
