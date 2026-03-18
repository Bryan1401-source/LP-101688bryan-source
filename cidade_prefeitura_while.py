import os
from colorama import init, Fore

init(autoreset=True)

os.system("cls")

# Variáveis para cálculos
total_familias = 0
soma_salarios = 0
soma_filhos = 0
maior_salario = None
menor_salario = None

while True:
    
    print(Fore.YELLOW + "=== PESQUISA PREFEITURA ===")
    print("1 | Adicionar família")
    print("2 | Sair e exibir resultados")
    print("=" * 27)
    
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        print(Fore.CYAN + "--- Cadastro de Família ---")
        
        try:
            salario = float(input("Salário mensal: R$ "))
            filhos = int(input("Número de filhos: "))

            # Acumuladores
            total_familias += 1
            soma_salarios += salario
            soma_filhos += filhos

            # Lógica de Maior e Menor salário
            if maior_salario is None or salario > maior_salario:
                maior_salario = salario
            if menor_salario is None or salario < menor_salario:
                menor_salario = salario

            print(Fore.GREEN + "\nDados registrados!")
            
        except ValueError:
            print(Fore.RED + "\nErro: Digite valores válidos, por favor!")
        
        input("\nPressione Enter para continuar...")

    elif opcao == '2':
        print(Fore.YELLOW + "=== RESULTADOS FINAIS ===")
        
        if total_familias > 0:
            media_salarial = soma_salarios / total_familias
            media_filhos = soma_filhos / total_familias
            
            print(f"a) Total de famílias: {Fore.WHITE}{total_familias}")
            print(f"b) Média salarial: {Fore.GREEN}R$ {media_salarial:.2f}")
            print(f"c) Média de filhos: {Fore.CYAN}{media_filhos:.1f}")
            print(f"d) Maior salário: {Fore.GREEN}R$ {maior_salario:.2f}")
            print(f"e) Menor salário: {Fore.GREEN}R$ {menor_salario:.2f}")
        else:
            print(Fore.RED + "Nenhuma família foi cadastrada.")
            
        print("=" * 25)
        break # Encerra o programa
    
    else:
        print(Fore.RED + "\nOpção inválida!")
        input("\nPressione Enter para tentar novamente...")
