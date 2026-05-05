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

QUANTIDADE_FUNCIONARIOS = 2
lista_funcionarios = []

print('= Solicitação de Dados =')
for i in range(QUANTIDADE_FUNCIONARIOS):
    novo_funcionario = Funcionario(
        nome=input(f'\nInforme o nome do funcionário {i + 1}: '),
        idade=int(input(f'\nInforme a idade do funcionário {i + 1}: '))
    )
    lista_funcionarios.append(novo_funcionario)

print('\n= Lista de Funcionários =')
for funcionario in lista_funcionarios:
    funcionario.mostrar_dados()
    print('-------------------------')

print ('= Salvando Dados =')
with open('lista_funcionarios.csv', 'a', encoding='utr-8') as arquivo:
    for funcionario in lista_funcionarios:
        arquivo.write(f'{funcionario.nome},{funcionario.idade}\n')
print(f'{Fore.YELLOW}Dados salvos com sucesso!{Style.RESET_ALL}')

print('\n= Fim do Programa =') 