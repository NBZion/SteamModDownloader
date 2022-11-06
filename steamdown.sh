#!/bin/bash

if [ "$1" == "install" ]; then
    git clone https://github.com/NBZion/SteamModDownloader.git temp
    mv -v ./temp/* .
    rmdir temp
    rm -rf .git
    pip install -r requirements.txt
fi

python __main__.py