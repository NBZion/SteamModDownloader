from math import modf
import os
from re import sub
import wget
import subprocess
import shutil
import time
# Variables
steamCmdUrl="https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz"
steamCmdPath="./scripts/steamcmd/"
workDirectory=os.getcwd()+'/scripts/steamcmd/workshop'
conDir=workDirectory+'/steamapps/workshop/content/'
tarFile=None

def checkAndDownloadSteamCmd():
    if len(os.listdir(steamCmdPath)) == 0:
        print("SteamCMD not present, Downloading...")
        wget.download(steamCmdUrl,steamCmdPath)
        subprocess.call(['tar','-xvf', steamCmdPath+'steamcmd_linux.tar.gz','-C',steamCmdPath])
        os.remove(steamCmdPath+'steamcmd_linux.tar.gz')
        os.mkdir('./scripts/steamcmd/workshop')
    else:
        return 
def download(id,gameId,name,insDir):
    print('Downloading '+ name+'('+id+')')
    print('--------------------------------------------------')
    subprocess.call([steamCmdPath+'steamcmd.sh','+force_install_dir '+workDirectory,'+login anonymous',f'+workshop_download_item {gameId} {id}','+exit'])
    print('\n--------------------------------------------------')
    print('Moving and Renaming ' +name+'('+id+')')
    modFol=conDir+gameId+'/'+id+'/'
    outPathName=insDir+'/'+name
    if os.path.exists(outPathName): print('Updating File(Existing File)')
    shutil.copytree(modFol,outPathName,dirs_exist_ok=True)
    shutil.rmtree(modFol)
    