import os
import time
from colorama import init, Fore

init(autoreset=True)

os.system('cls' if os.name == 'nt' else 'clear')

pares = 0
impares = 0

print(Fore.CYAN + "Digite 5 números inteiros: ")

for i in range (5):
    try:
        numero = int(input(f"Valor {i+1}: ")) 
        if numero % 2 == 0:
             pares += 1
        else:
            impares += 1
    except ValueError:
        print(Fore.RED + "Por favor, digite apenas números inteiro.")    

    print ("\n" + "="*20)
    print(Fore.GREEN + f"Número pares: {pares}")
    print(Fore.YELLOW + f"Número impares: {impares}")
    print("="*20)    
