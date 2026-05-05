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

with open('contato_empresas.csv', 'r') as arquivo:
    lista_empresas = []
    for linha in arquivo:
        nome,cnpj,telefone = linha.strip().split(',')
        lista_empresas.append(Empresa(    
            nome=nome, 
            cnpj=cnpj, 
            telefone=telefone
        ))
             

for empresa in lista_empresas:
    empresa.mostrar_dados()
    print('-------------------------')