import os
import time
from colorama import init, Fore

init(autoreset=True)


os.system('cls' if os.name == 'nt' else 'clear')

while True:
    idade = int(input("Digite sua idade: "))
    if idade >= 18:
        print("Acesso Negado!")
        print("Tente novamente... \n")
    else:
        print("Acesso permitido.")
        break

print("Fim.")
