import requests
from bs4 import BeautifulSoup
from scripts.steamcmd import download
from scripts.config import fetchConfiguration

def processURL(url):
    result = url.split('id=')[1]
    if 'searchtext' in url:
        result = result.split('&searchtext')[0]
    return result

def checkType(url):
    if not "https" in url:
        return None
    res=requests.get(url)
    doc=BeautifulSoup(res.text,"html.parser")
    cItems = doc.find_all(class_="collectionItemDetails")
    if cItems:
        return "collection"
    else:
        return "mod"

def downloadMod(url):
    dwn = fetchConfiguration('downloadDir')
    gameid = fetchConfiguration('gameID')
    res = requests.get(url)
    doc = BeautifulSoup(res.text, "html.parser")
    title = doc.head.title.text.split("::")[1]
    id = processURL(url)
    download(id, gameid, title, dwn)

def downloadCollection(url):
    res = requests.get(url)
    doc = BeautifulSoup(res.text,"html.parser")
    itemList = doc.find_all(class_="collectionItemDetails")
    for item in itemList:
        downloadMod(item.find("a", href=True)['href'])

