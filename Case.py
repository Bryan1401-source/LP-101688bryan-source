import os

from colorama import init, Fore, Back, Style

# Limpe o terminal.
os.system("cls")

print (Fore.BLACK + "\n ----- BEM VINDO USUÁRIO ---------")

print(Style.RESET_ALL)

nome = input("Digite seu nome: ")
dia = input("Digite o dia da semana: ").lower()

match dia:
    case "segunda":
        print("Hoje é segunda-feira")
    case "terça":
        print("Hoje é terça-feira")
    case "quarta":
        print("Hoje é quarta-feira")
    case "quinta":
        print("Hoje é quinta-feira")
    case "sexta":
        print("Hoje é sexta-feira")
    case "sabado" | "domingo":
        print("Hoje é fim de semana")
    
    case _:
        print("Dia inválido.")


print(dia)

print (Fore.CYAN + "\n ========= FIM DA EXECUÇÃO =========")
        

