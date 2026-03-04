import os

from colorama import init, Fore, Back, Style

# Limpe o terminal.
os.system("cls")

print (Fore.BLACK + "\n ----- BEM VINDO USUÁRIO ---------")

print(Style.RESET_ALL)

numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite um número: "))
caractere = input("Digite um caractere:")

match caractere:
    case ("*"):
        resultado = ((numero1 * numero2))
    case ("/"):
        resultado = ((numero1 / numero2))
    case ("-"):
        resultado = ((numero1 - numero2))
    case ("+"):
        resultado = ((numero1 + numero2))
    case _:
        print("\n Operação inválida.\n")
        resultado = 0
        
        
        

print (f"Resultado {resultado}")
