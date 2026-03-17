import os
import time
from colorama import init, Fore

os.system('cls' if os.name == 'nt' else 'clear')

init(autoreset=True)

qtd_alunos = int(input("Quantos alunos deseja avaliar? "))

for i in range(qtd_alunos):

   
    print(Fore.CYAN + f"--- Sistema de Notas (Aluno {i+1}/{qtd_alunos}) ---" + Fore.RESET)

    n1 = float(input("Digite a 1ª nota: "))
    n2 = float(input("Digite a 2ª nota: "))
    n3 = float(input("Digite a 3ª nota: "))

    media = (n1 + n2 + n3) / 3

    print("\nProcessando resultado...")
    time.sleep(1)

    print(f"\nMédia Final: {media:.2f}")

    if media >= 7:
        print(Fore.GREEN + "Situação: APROVADO")
    elif media < 4:
        print(Fore.RED + "Situação: REPROVADO")
    else:
        print(Fore.YELLOW + "Situação: EM RECUPERAÇÃO")
    
    input("\nPressione Enter para continuar...")

print(Fore.MAGENTA + "\nProcessamento finalizado!")

