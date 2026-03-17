import os
import time
from colorama import init, Fore

init(autoreset=True)


os.system('cls' if os.name == 'nt' else 'clear')

# Laço de repetição usado quando sabhemos
# Quantas vezes queremos repetir algo.

soma = 0

print(Fore.CYAN + "--- Somador de 5 Números ---")

for i in range(1, 6):
    try:
        numero = int(input(f"Digite o {i}º número inteiro: "))
        soma += numero
    except ValueError:
        print(Fore.RED + "Isso não é um número inteiro! Tente novamente.")

print(Fore.YELLOW + "\nCalculando...")
time.sleep(4) 

print(Fore.GREEN + f"\nA soma total de todos os números lidos é: {soma}")