import os

from colorama import init, Fore, Back, Style

# Limpe o terminal.
os.system("cls")

print ("\n ----- BEM VINDO USUÁRIO ---------")

nota = float(input("Digite uma nota: "))

if nota >= 0 and nota <= 10:
    print(f"Sua nota foi {nota}")
else:
    print(f"O Sistema deseja que a nota seja entre Zero e Dez")
    
print("\n- Exibindo dados -")  
