import os
from colorama import init, Style, Back, Fore

import os

def calculo_de_media(vetor_notas):
    soma = sum(vetor_notas)
    return soma / len(vetor_notas)
notas = []
os.system("cls")
print("= Solicitando Dados =")

print("=== Cadastro de Indivíduos ===")

for i in range(3):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    notas.append(nota)

media = calculo_de_media(notas)


print("= Exibindo Dados =")
print("\n=== Resultado ===")
print(f"Notas registradas: {notas}")
print(f"Média final: {media:.2f}")

