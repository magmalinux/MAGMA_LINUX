#!/usr/bin/python3
from os import system
from termcolor import colored
from sys import exit

logo = """
  __  __                               _______                   __          
 |  \/  |                             |__   __|                 / _|         
 | \  / | __ _  __ _ _ __ ___   __ _     | |_ __ __ _ _ __  ___| |_ ___ _ __ 
 | |\/| |/ _` |/ _` | '_ ` _ \ / _` |    | | '__/ _` | '_ \/ __|  _/ _ \ '__|
 | |  | | (_| | (_| | | | | | | (_| |    | | | | (_| | | | \__ \ ||  __/ |   
 |_|  |_|\__,_|\__, |_| |_| |_|\__,_|    |_|_|  \__,_|_| |_|___/_| \___|_|   
                __/ |                                                        
               |___/                                                         
"""
print(colored(logo, "green"))
print("Magma Transfer is powered by the Magic Wormhole")
print("https://github.com/warner/magic-wormhole")
file_location = input("Please enter the files location you wish to transfer [filename]: ")
confirm = input("Confirm? [y/n]: ").lower()
if (confirm == 'y' or confirm == 'yes'):
    system('wormhole send ' + str(file_location))
if (confirm == 'n' or confirm == 'no'):
    exit()