import os
from colorama import init, Fore

init(autoreset=True)
os.system("cls")

somador_de_notas = 0
contador = 0

while True:
    nota = float(input(Fore.CYAN + "Digite uma nota: "))
    somador_de_notas += nota
    contador += 1
    
    continuar = input(Fore.YELLOW + "Deseja inserir mais uma nota? (S/N): ").upper()
    
    if continuar == "N":
        break

if contador > 0:
    media = somador_de_notas / contador
    print(Fore.GREEN + f"\nVocê inseriu {contador} notas.")
    print(Fore.GREEN + f"A média é: {media:.2f}")
else:
    print(Fore.RED + "Nenhuma nota foi registrada.")
