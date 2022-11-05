import scripts.steamcmd as steamcmd
from scripts.config import fetchConf
import requests
from bs4 import BeautifulSoup


def processUrl(inp):
    strspl=inp.split('id=')
    fresult=strspl[1]
    if 'searchtext' in inp:
        fresult=fresult.split('&searchtext')[0]
    return fresult
def modCollectCheck(inp):
    if not "https" in inp:  return
    res=requests.get(inp)
    doc=BeautifulSoup(res.text,"html.parser")
    cItems=doc.find_all(class_="collectionItemDetails")
    if cItems != []:
        return "collection"
    else:
        return "mod"
def downMod(url):
    insDir=fetchConf('inslDir')
    gameId=fetchConf('gameId')
    res=requests.get(url)
    doc=BeautifulSoup(res.text,"html.parser")
    title=doc.head.title.text.split("::")[1]
    id=processUrl(url)
    steamcmd.download(id,gameId,title,insDir)
def downCollect(url):
    res=requests.get(url)
    doc=BeautifulSoup(res.text,"html.parser")
    itemList=doc.find_all(class_="collectionItemDetails")
    for item in itemList:
        downMod(item.find("a", href=True)['href'])
        
    