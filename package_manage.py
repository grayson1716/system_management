import os as os

print('\nUpdating Package Repository...')
os.system('sudo apt update')

print('\nUpgrading Packages and Removing Unnecessary Dependencies...')
os.system('sudo apt full-upgrade')

print('\nRemoving Thumbnails...')
os.system('sudo rm -rf ~/.thumbnails')

print('\nCleaning APT cache...')
os.system('sudo apt-get autoclean')
os.system('sudo apt-get clean')
