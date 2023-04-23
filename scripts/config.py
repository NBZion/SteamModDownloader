import json
import os
import sys
from getpass import getpass

def configureSetting(setting, val):
    with open("conf.json", "r+") as f:
        js = json.load(f)
        js[setting] = val
        f.seek(0)
        json.dump(js, f, indent=4)
        f.truncate()

def getCredentials():
    name = input("What is your steam name?\n> ")
    while not name:
        name = input("Please enter a valid steam name.\n> ")

    pass_ = getpass("What is your steam password?\n> ")
    while not pass_:
        pass_ = getpass("Please enter a valid steam password.\n> ")

    confirm = getpass("Re-enter your password to confirm.\n> ")
    while pass_ != confirm:
        print("Passwords do not match, please try again.")
        pass_ = getpass("What is your steam password?\n> ")
        while not pass_:
            pass_ = input("Please enter a valid steam password.\n> ")
        confirm = getpass("Re-enter your password to confirm.\n> ")

    return name, pass_

def fetchConfiguration(val):
    with open("conf.json", "r") as f:
        js = json.load(f)
    return js[val]
