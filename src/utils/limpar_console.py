import os
from time import sleep
def limparConsole():
    if os.name == "nt":
        sleep(1)
        os.system("cls")
    else: 
        sleep(1)
        os.system("clear")