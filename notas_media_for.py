import os
from colorama import init, Fore

init(autoreset=True)

os.system('cls' if os.name == 'nt' else 'clear')

print(Fore.CYAN + "=== Calculador de Média ===" + "\n")

notas = []

for i in range(1, 5):
    nota = float(input(f"Digite a {i}ª nota: "))
    notas.append(nota)

media = sum(notas) / len(notas)

print("\n" + Fore.YELLOW + "-" * 20)
print(Fore.GREEN + f"A média final é: {media:.2f}")
print(Fore.YELLOW + "-" * 20)
