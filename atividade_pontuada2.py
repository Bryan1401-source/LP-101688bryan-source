import os
from colorama import init, Fore, Back, Style


os.system("cls")
init (autoreset=True)


numeros = []


for i in range (5):
    num = int(input(Fore.WHITE + Style.BRIGHT + f"Digite o {i+1}º número: "))
    numeros.append(num)

quantidade_pares = 0
somando_pares = 0
quantidade_impares = 0
somando_impares = 0
quantidade_positivos = 0
quantidade_negativos = 0
soma_geral = sum(numeros)

# Processando os números
for num in numeros:

    if num % 2 == 0:
        quantidade_pares += 1
        somando_pares += num
    else:
        quantidade_impares += 1
        somando_impares += num
    
    if num > 0:
        quantidade_positivos += 1
    elif num < 0:
        quantidade_negativos += 1

media_pares = somando_pares / quantidade_pares if quantidade_pares > 0 else 0
media_impares = somando_impares / quantidade_impares if quantidade_impares > 0 else 0
media_geral = soma_geral / len(numeros)

print(Fore.YELLOW + Style.BRIGHT  + "\n--- Estatísticas dos Números ---")
print(Fore.WHITE + Style.BRIGHT + f"Quantidade de pares: {quantidade_pares}")
print(Fore.WHITE + Style.BRIGHT + f"Quantidade de ímpares: {quantidade_impares}")
print(Fore.WHITE + Style.BRIGHT + "-" * 25)
print(Fore.WHITE + Style.BRIGHT + f"Quantidade de positivos: {quantidade_positivos}")
print(Fore.WHITE + Style.BRIGHT + f"Quantidade de negativos: {quantidade_negativos}")
print(Fore.WHITE + Style.BRIGHT + "-" * 25)
print(Fore.WHITE + Style.BRIGHT + f"Total de números inseridos: {len(numeros)}")
print(Fore.WHITE + Style.BRIGHT + "-" * 25)
print(Fore.WHITE + Style.BRIGHT + f"Maior número: {max(numeros)}")
print(Fore.WHITE + Style.BRIGHT + f"Menor número: {min(numeros)}")
print(Fore.WHITE + Style.BRIGHT + "-" * 25)
print(Fore.WHITE + Style.BRIGHT + f"Média de números pares: {media_pares:.2f}")
print(Fore.WHITE + Style.BRIGHT + f"Média de números ímpares: {media_impares:.2f}")
print(Fore.WHITE + Style.BRIGHT + "-" * 25)
print(Fore.WHITE + Style.BRIGHT + f"Média de todos os números: {media_geral:.2f}")
print(Fore.WHITE + Style.BRIGHT + f"Números na ordem inversa: {numeros[::-1]}")







print (Fore.WHITE + Style.BRIGHT + "-" * 25)