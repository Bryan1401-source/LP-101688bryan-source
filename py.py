import os
from colorama import init, Style, Fore, Back

def logo():
    os.system("CLS")
    print("==========")
    print("   SENAI  ")
    print("==========")

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b



def multiplicar(a, b):
    print(f"Multiplicação: {a * b}")

def dividir(a, b):
    if b != 0:
        print(f"Divisão: {a / b}")
    else:
        print("Divisão: Erro: Divisão por Zero!")

logo()
print("= Solicitando dados =")

              
numeros = []
for i in range(2):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

soma = somar(numeros[0], numeros[1])
subtracao = subtrair(numeros[0], numeros[1])

logo()
print("= Exibindo dados =")
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")

multiplicar(numeros[0], numeros[1])
dividir(numeros[0], numeros[1])
