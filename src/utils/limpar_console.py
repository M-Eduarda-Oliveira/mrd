import os
from time import sleep
def limparConsole(tempo):
    if os.name == "nt":
        sleep(tempo)
        os.system("cls")
    else: 
        sleep(tempo)
        os.system("clear")