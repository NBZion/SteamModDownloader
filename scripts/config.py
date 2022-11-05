import json
import sys
import os 
def setConf(choice,val):
    confch=None
    if choice=="1":
        confch="gameId"
    elif choice=="2":
        confch="inslDir"
    else:
        print('Invalid Number')
        sys.exit()
    if choice=="2":
        if not os.path.exists(val) and val!="":
            print('Invalid Path')
            sys.exit()
    js=json.load(open('conf.json'))
    js[confch]=val
    print(js)
    with open('conf.json','w') as f:
        json.dump(js,f,indent=4)
        f.close()

def fetchConf(val):
    js=json.load(open('conf.json'),)
    return js[val]