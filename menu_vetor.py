import os
from colorama import Fore, Style, init

# Iniciando o colorama
init(autoreset=True)

# Definição dos Dados

cardapio_nomes = ["Lasanha", "Bife com Feijão", "Salada de Maionese", "Strogonoff", "Suco Natural"]
cardapio_precos = [35.00, 42.50, 28.00, 45.00, 8.00]

# Vetores para armazenar o pedido do cliente
nomes_escolhidos = []
precos_escolhidos = []

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(f"{Fore.YELLOW}{Style.BRIGHT}=== CARDÁPIO DO RESTAURANTE ===")
    for i in range(len(cardapio_nomes)):
        print(f"{Fore.CYAN}{i + 1}. {cardapio_nomes[i]:<15} {Fore.GREEN}R$ {cardapio_precos[i]:.2f}")
    
    try:
        escolha = int(input(f"\n{Style.BRIGHT}Escolha o número do prato (ou 0 para cancelar): "))
        
        if escolha == 0:
            break
            
        if 1 <= escolha <= len(cardapio_nomes):
            # Adicionando aos "vetores" de pedido
            index = escolha - 1
            nomes_escolhidos.append(cardapio_nomes[index])
            precos_escolhidos.append(cardapio_precos[index])
            print(f"{Fore.GREEN}✔ {cardapio_nomes[index]} adicionado!")
        else:
            print(f"{Fore.RED}Opção inválida!")
            
    except ValueError:
        print(f"{Fore.RED}Por favor, digite um número válido.")

    continuar = input(f"\nDeseja escolher outro prato? (s/n): ").lower()
    if continuar != 's':
        break

# --- RESUMO FINAL ---
os.system('cls' if os.name == 'nt' else 'clear')
print(f"{Fore.YELLOW}{Style.BRIGHT}=== SEU PEDIDO ===")

total = 0
for i in range(len(nomes_escolhidos)):
    print(f"{Fore.WHITE}{nomes_escolhidos[i]:<15} {Fore.GREEN}R$ {precos_escolhidos[i]:.2f}")
    total += precos_escolhidos[i]

print(f"{Fore.YELLOW}{'-'*25}")
print(f"{Style.BRIGHT}VALOR TOTAL DA CONTA: {Fore.GREEN}R$ {total:.2f}")
print(f"{Fore.YELLOW}{'='*25}")


