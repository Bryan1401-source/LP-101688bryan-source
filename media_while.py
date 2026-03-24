import os
from colorama import init, Fore

init(autoreset=True)
os.system("cls")

soma = 0
contador = 0

print(Fore.YELLOW + "Digite valores inteiros positivos (ou um negativo para encerrar):")

while True:
    valor = int(input("Informe um valor: "))
    
    if valor < 0:
        break
    
    soma += valor
    contador += 1

if contador > 0:
    media = soma / contador
    print(Fore.GREEN + f"\nForam inseridos {contador} números positivos.")
    print(Fore.CYAN + f"A média aritmética é: {media:.2f}")
else:
    print(Fore.RED + "Nenhum valor positivo foi informado.")
