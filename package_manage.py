import os as os

print('\nFetching Updates...')
os.system('sudo apt-get update')
os.system('sudo apt update')

print('\nUpgrading...')
os.system('sudo apt-get upgrade')
os.system('sudo apt upgrade')

print('\nAutoremoving...')
os.system('sudo apt-get autoremove')
os.system('sudo apt autoremove')

print('\nRemoving Thumbnails and Cleaning...')
os.system('sudo rm -rf ~/.thumbnails')
os.system('sudo apt-get clean')