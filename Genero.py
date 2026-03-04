import os

from colorama import init, Fore, Back, Style

# Limpe o terminal.
os.system("cls")

print ("\n ------ BEM VINDO ------")

genero = input("Digite seu sexo: ").lower()
ano_de_nascimento = int(input("Digite o ano que você nasceu: "))

idade = 2026 - ano_de_nascimento

if genero == "Masculino" and idade == 18:
    print(Fore.GREEN + "\n Você deve obrigatóriamente prestar serviço militar!")
    print(Style.RESET_ALL)
else:
    print(Fore.RED + "\n Não deve se apresentar.")
    
    print(Style.RESET_ALL)
    
    
print (f"Sexo: ", genero)
print (f"Idade:", idade )