import os
from colorama import init, Fore

init(autoreset=True)

# Inicialização das variáveis
total_familias = 0
soma_salarios = 0
soma_filhos = 0
maior_salario = 0
menor_salario = 0

while True:
    print(Fore.YELLOW + "\n--- PESQUISA PREFEITURA ---")
    print("1 | Adicionar família")
    print("2 | Sair e exibir resultados")
    
    opcao = input(Fore.WHITE + "\nEscolha uma opção: ")

    if opcao == '1':
        salario = float(input("Digite o salário da família: R$ "))
        filhos = int(input("Digite o número de filhos: "))

        # Lógica para Maior e Menor Salário
        if total_familias == 0:  # Primeira família cadastrada
            maior_salario = salario
            menor_salario = salario
        else:
            if salario > maior_salario:
                maior_salario = salario
            if salario < menor_salario:
                menor_salario = salario

        # Acumuladores e Contadores
        soma_salarios += salario
        soma_filhos += filhos
        total_familias += 1
        
        print(Fore.GREEN + "Dados registrados com sucesso!")
        input("\nPressione Enter para continuar...")
        os.system("cls")

    elif opcao == '2':
        break
    else:
        print(Fore.RED + "Opção inválida!")

# Exibição dos resultados finais
os.system("cls")
if total_familias > 0:
    media_salario = soma_salarios / total_familias
    media_filhos = soma_filhos / total_familias

    print(Fore.WHITE + "========== RESULTADOS DA PESQUISA ==========")
    print(f"a) Total de famílias: {total_familias}")
    print(f"b) Média salarial: R$ {media_salario:.2f}")
    print(f"c) Média de filhos: {media_filhos:.1f}")
    print(f"d) Maior salário: R$ {maior_salario:.2f}")
    print(f"e) Menor salário: R$ {menor_salario:.2f}")
    print(Fore.WHITE + "============================================")
else:
    print(Fore.RED + "Nenhum dado foi inserido para gerar o relatório.") 
    
    
