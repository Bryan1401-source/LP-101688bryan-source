import os

from colorama import Fore, Init, Style

# Inicialização do vetor
vetor = []

print("Digite 5 números:")

# Recebendo os valores
for i in range(5):
    num = float(input(f"Digite o {i+1}º valor: "))
    
    # Regra: se for negativo, atribui 0
    if num < 0:
        vetor.append(0)
    else:
        vetor.append(num)

# Listando os valores do vetor
print("\n--- VALORES NO VETOR ---")
for i in range(len(vetor)):
    print(f"Posição {i}: {vetor[i]}")
