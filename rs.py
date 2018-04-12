from termcolor import colored
from os import system
from sys import exit

cs = input("Do you want this computer to serve as the client or the server? [client/server]: ").lower()
if cs == 'client':
    system("python3 rs/client.py")
if cs == 'server':
    system("python3 rs/server.py")
else: 
    exit()