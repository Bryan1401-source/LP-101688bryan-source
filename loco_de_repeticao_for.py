import os
from colorama import init, Fore

init(autoreset=True)
os.system('cls' if os.name == 'nt' else 'clear')

# Solicita o número ao usuário
num = int(input(f"{Fore.CYAN}Digite um número para ver a tabuada: "))

print(f"\n{Fore.YELLOW}Tabuada do {num}:")

# Gera a tabuada de 1 a 10
for i in range(1, 11):
    resultado = num * i
    print(f"{Fore.WHITE}{num} x {i} = {Fore.GREEN}{resultado}")
