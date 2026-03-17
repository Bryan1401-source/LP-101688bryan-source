import os
import time
from colorama import init, Fore

init(autoreset=True)
os.system("cls")

numero = int(input("Digite um número: "))



print("""  
      Começando a contagem regressiva:
    """)

for numero in range (numero,0,-1):
   print(numero)

   time.sleep(1)