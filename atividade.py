import os
from colorama import init, Style,Fore,Back

def logo ():
    os.system("Cls")
    print("==============")
    print("     SENAI   ")
    print("==============")

def valor (centimetro):
    centimetro = n1 * 100
    print(f"Sua quantia de came em centimetros: {centimetro:.0f}")

logo()
print("= Solicitando dados =")
n1 = float(input("Digite a quantidade de came que você deseja: "))

logo()
print("= Exibindo Dados =")
print(f"Sua quantia de carne em metros: {str(n1).replace('.', ',')}m")
valor (n1)