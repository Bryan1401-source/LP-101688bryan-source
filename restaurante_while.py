import os
from colorama import init, Fore, Style

init(autoreset=True)
os.system("cls")

total_pagar = 0

while True:
    # Exibição do Menu
    print(Fore.YELLOW + "="*30)
    print(Fore.WHITE + "      CARDÁPIO DO DIA")
    print(Fore.YELLOW + "="*30)
    print("Código | Prato          | Valor")
    print("  1    | Picanha        | R$ 25,00")
    print("  2    | Lasanha        | R$ 20,00")
    print("  3    | Strogonoff     | R$ 18,00")
    print("  4    | Bife Acebolado | R$ 15,00")
    print("  5    | Pão com ovo    | R$  5,00")
    print(Fore.YELLOW + "="*30)

    opcao = input("\nDigite o código do prato desejado: ")

    # Processamento da escolha
    if opcao == '1':
        total_pagar += 25.00
        print(Fore.GREEN + "Picanha adicionada!")
    elif opcao == '2':
        total_pagar += 20.00
        print(Fore.GREEN + "Lasanha adicionada!")
    elif opcao == '3':
        total_pagar += 18.00
        print(Fore.GREEN + "Strogonoff adicionado!")
    elif opcao == '4':
        total_pagar += 15.00
        print(Fore.GREEN + "Bife Acebolado adicionado!")
    elif opcao == '5':
        total_pagar += 5.00
        print(Fore.GREEN + "Pão com ovo adicionado!")
    else:
        print(Fore.RED + "Código inválido!")

    # Pergunta se deseja continuar
    continuar = input("\nDeseja escolher outro prato? (S/N): ").upper()
    
    if continuar == 'N':
        break
    
    os.system("cls")

# Resultado Final
print(Fore.CYAN + "="*30)
print(Fore.WHITE + f"TOTAL A PAGAR: R$ {total_pagar:.2f}")
print(Fore.CYAN + "="*30)
