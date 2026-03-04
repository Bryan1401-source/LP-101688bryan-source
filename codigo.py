import os

from colorama import init, Fore, Back, Style

# Limpe o terminal.
os.system("cls")

print (Fore.LIGHTGREEN_EX + "\n ------ BEM VINDO CLIENTE ------")
print(Style.RESET_ALL)

print (Fore.GREEN + """
       ============= $ MENU $ =================
       Código          Prato          Preço
         01          Picanha          R$ 25,00
         02          Lasanha          R$ 20,00
         03          Strogonoff       R$ 18,00
         04          Bife Acebolado   R$ 15,00
         05          Pão com Ovo      R$ 5,00
       
       
       """)
       
print(Style.RESET_ALL)       

menu = input("Digite um código: ")


print(Style.RESET_ALL)

print("""
      =======   Prato Escolhido com Valor: =======
           """)

match menu:
    case "01":
        print("Picanha")
        print("R$ 25,00")
    case "02":
        print("Lasanha")
        print("R$ 20,00")
    case "03":
        print("Strogonoff")
        print("R$ 18,00")
    case "04":
        print("Bife Acebolado")
        print("R$ 15,00")
    case "05":
        print("Pão com Ovo")
        print("R$ 5,00")
    case _:
        print("Prato não disponivél no menu.\n")
        

