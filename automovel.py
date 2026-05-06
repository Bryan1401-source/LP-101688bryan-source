import os
from dataclasses import dataclass
from colorama import Fore, Style, Back, init

init (autoreset=True)

os.system('cls' if os.name == 'nt' else 'clear')

@dataclass
class Automovel:
    Marca: str
    Modelo: str
    Fabricação: str
    Cor: str
    Preço: str

lista_automoveis = []

while True:
    print(Back.BLACK + Fore.WHITE  + Style.BRIGHT + "\n--- SISTEMA DE CADASTRO DE AUTOMÓVEIS ---")
    print(Back.BLACK + Fore.WHITE + Style.BRIGHT + "1 - Adicionar Carro")
    print(Back.BLACK + Fore.WHITE + Style.BRIGHT + "2 - Listar Carros")
    print(Back.BLACK + Fore.RED + Style.BRIGHT + "3 - Sair")
    
    opcao = input(Back.BLACK + Fore.WHITE + Style.BRIGHT +"Escolha uma opção: ")

    if opcao == '1':
        os.system('cls' if os.name == 'nt' else 'clear')
        carro_novo = Automovel(
            Marca=input(Back.BLACK + Fore.WHITE  + Style.BRIGHT + "Marca: "),
            Modelo=input(Back.BLACK + Fore.WHITE  + Style.BRIGHT + "Modelo: "),
            Fabricação=input(Back.BLACK + Fore.WHITE  + Style.BRIGHT + "Fabricação: "),
            Cor=input(Back.BLACK + Fore.WHITE  + Style.BRIGHT + "Cor: "),
            Preço=input(Back.BLACK + Fore.WHITE  + Style.BRIGHT + "Preço: ")
        )
        lista_automoveis.append(carro_novo)
        
        with open('catalogo_carros.csv', 'a', encoding='utf-8') as arquivo:
            arquivo.write(f'{carro_novo.Marca}, {carro_novo.Modelo}, {carro_novo.Fabricação}, {carro_novo.Cor}, {carro_novo.Preço}\n')
        
        print(Back.BLACK + Fore.GREEN  + Style.BRIGHT + "\nCarro adicionado e salvo com sucesso!")

    elif opcao == '2':
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(Back.BLACK + Fore.WHITE  + Style.BRIGHT + "\n--- Lista de Automóveis (Sessão Atual) ---")
            if not lista_automoveis:
                print(Back.BLACK + Fore.RED  + Style.BRIGHT + "Nenhum carro cadastrado nesta sessão.")
            else:
                for c in lista_automoveis:
                    print(Back.BLACK + Fore.WHITE  + Style.BRIGHT + f"Marca: {c.Marca} | Modelo: {c.Modelo} | Ano: {c.Fabricação} | R$ {c.Preço}")
        except FileNotFoundError:
            print(Back.BLACK + Fore.RED  + Style.BRIGHT + "Arquivo não encontrado...")
    

    elif opcao == '3':
        os.system('cls')
        print(Back.BLACK + Fore.RED  + Style.BRIGHT + "Saindo do programa...")
        break
    
    else:
        print(Back.BLACK + Fore.RED  + Style.BRIGHT + "Opção inválida!")
