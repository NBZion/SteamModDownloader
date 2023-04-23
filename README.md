# SteamModDownloader
A Steam Workshop Downloader CLI-tool for linux,

Developed by NBZion.

## Installation
Download `smd` from releases tab, and run the following commands:
```bash
chmod +x ./smd # Allow execution
./smd install # Execute script
```
If you want to replace your already existing installation completely:
```bash
./smd reinstall
```

## Usage
To start SMD (assuming it has been installed properly), run this command:
```
./smd launch
```
Here's a list of all the settings and what they are:
```js
'downloadDir': the directory mods will be downloaded to.
'anonymousMode': whether or not to use a real account.
'steamAccountName': account username if not using anonymous mode.
'steamPassword': account password if not using anonymous mode.
'gameID': ID of the game you want the workshop mods for.
```
These are configured at startup once, and can be changed in settings.
To download your mods, simply select the "Download Mods" option and
paste your workshop url/link. It will be downloaded to `downloadDir`.

## Features
- Collection Support
 
## Currently Known Issues
- Downloading a mod may not work until you delete the steamcmd folder and try to re-download it.

## Some Things To Note...
- This project is currently only built for the linux python version.
- Some mods may not download as they require an actual account.
- My code is messy, so feel free to pull-request any changes!
- This project is still being updated, it's just that I'm either busy or don't have a feature to add, so please suggest potential features or report bugs in the issues page.

## TODO
- Windows Support
-  ✅ Wrapper Scripts 

