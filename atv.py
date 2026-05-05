import os
from dataclasses import dataclass
from colorama import init, Fore, Style

os.system('cls') 

init(autoreset=True)

@dataclass
class Empresa:
    nome: str
    cnpj: str
    telefone: str

def mostrar_dados(self):
    print(f'{Fore.GREEN}Nome: {self.nome}{Style.RESET_ALL}')
    print(f'{Fore.BLUE}CNPJ: {self.cnpj}{Style.RESET_ALL}')
    print(f'{Fore.YELLOW}Telefone: {self.telefone}{Style.RESET_ALL}')


nome = input('\nInforme o nome da empresa: ').title()
cnpj = input('\nInforme o CNPJ da empresa: ')
telefone = input('\nInforme o telefone da empresa: ')
empresa = Empresa(nome, cnpj, telefone)

with open('contato_empresas.csv', 'a', encoding='utf-8') as arquivo:
    arquivo.write(f'{empresa.nome},{empresa.cnpj},{empresa.telefone}\n')
print(f'{Fore.YELLOW}Dados da empresa salvos com sucesso!{Style.RESET_ALL}')


print('\n= Dados da Empresa =')
empresa.mostrar_dados()