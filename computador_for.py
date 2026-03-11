import os
import time
from colorama import init, Fore

init(autoreset=True)
os.system("cls")

numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite um número: "))
numero3 = int(input("Digite um número: "))
numero4 = int(input("Digite um número: "))
numero5 = int(input("Digite um número: "))


soma = numero1 + numero2 + numero3 + numero4 + numero5

print (f"Soma total: {soma}")