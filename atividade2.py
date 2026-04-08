import os
from colorama import init, Style,Fore,Back

os.system ("CLS")

def calcular_inflacao(preco):
    if preco < 100:
        # Inflaciona em 10%
        preco_novo = preco * 1.10
    else:
        # Inflaciona em 20%
        preco_novo = preco * 1.20
    
    return preco_novo

# Solicita o preço ao usuário
preco_original = float(input("Digite o preço do seu produto: "))

# Chama a função
resultado = calcular_inflacao(preco_original)

# Exibe o resultado final
print(f"O novo preço inflacionado é: R$ {resultado:.0f}")
