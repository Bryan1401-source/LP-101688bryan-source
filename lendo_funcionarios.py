import os
from dataclasses import dataclass
from colorama import init, Fore, Style

os.system('cls' if os.name == 'nt' else 'clear') 

init(autoreset=True)

@dataclass
class Funcionario:
    nome: str
    idade: int

    def mostrar_dados(self):
        print(f'{Fore.GREEN}Nome: {self.nome}{Style.RESET_ALL}')
        print(f'{Fore.BLUE}Idade: {self.idade}{Style.RESET_ALL}')

lista_funcionarios = []

try:
    with open('lista_funcionarios.csv', 'r') as arquivo:
        for linha in arquivo:
            nome, idade = linha.strip().split(',')
            lista_funcionarios.append(Funcionario(    
                nome=nome, 
                idade=int(idade)
            ))
except FileNotFoundError:
    print(f"{Fore.RED}Erro: O arquivo 'lista_funcionarios.csv' não foi encontrado.{Style.RESET_ALL}")

for funcionario in lista_funcionarios:
    funcionario.mostrar_dados()
    print('-------------------------')
