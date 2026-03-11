import os
import time
from colorama import init, Fore

init(autoreset=True)
os.system("cls")

numero = int(input("Digite um número: "))
# 
print ("""
          
========== $$ INICIANDO CONTAGEM REGRESSIVA PARA SUA MORTE $$ ===========
    """)
for i in range (numero, 0, -1):
   print(i)
   time.sleep(1)
   
print (Fore.WHITE + """
          
              ========== $$ VOCÊ MORREU $$ ===========
    """)