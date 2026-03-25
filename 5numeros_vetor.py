import os 
from colorama import init, Fore 

init(autoreset = True)

#Limpa o Terminal
os.system ("cls")



# Criando um Vetor.

print(f"{Fore.CYAN}--- --------- \n")

# 1. Criando o vetor (lista)
numero = []
QUANTIDADES_DE_NUMEROS = 5

# Lendo os 5 números solicitados 

for i in range (QUANTIDADES_DE_NUMEROS):
    valor = float(input(f"Digite o {i+1}º número: "))
    numero.append(valor)
    
# Processando os dados
maior_numero = max(numero)
menor_numero = min(numero)

# Mostrando os resultados 

print("\n" + "-"*35)
print(f"{Fore.YELLOW}Números digitados: {numero}")
print(f"{Fore.GREEN}O MAIOR número é: {maior_numero}")
print(f"{Fore.RED}O MENOR número é: {menor_numero}")
print("-"*35)