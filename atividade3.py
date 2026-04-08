import os
from colorama import init, Style, Fore

os.system("CLS")

init(autoreset=True)

def calcular_idade(ano_nascimento):

    ano_atual = 2026
    return ano_atual - ano_nascimento

try:
    print(Fore.YELLOW + "--- CALCULADOR DE IDADE ---")
    ano_em_que_nasceu = int(input("Digite o seu ano de nascimento: "))
    
    idade = calcular_idade(ano_em_que_nasceu)
    
    print(f"\nSua idade é: {Fore.GREEN}{Style.BRIGHT}{idade} anos.")
except ValueError:
    print(Fore.RED + "Erro: Por favor, insira um número de ano válido.")
