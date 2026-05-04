import os
from dataclasses import dataclass
from colorama import init, Style, Back, Fore

os.system('CLS')

@dataclass
class Funcionario:
    nome: str
    email: str
    telefone: str

    def mostrar_dados(self):
        print(f'Nome: {self.nome}\n')
        print(f'E-mail: {self.email}@gmail.com \n')
        print(f'Telefone: {self.telefone}\n')
        


lista_funcionario = []

print('Solicitando dados')
for i in range(3):
    novo_funcionario = Funcionario(
        nome=input('Digite seu nome: '),
        email=input('Digite seu e-mail: '),
        telefone=input('Digite seu telefone: ')
    )

    lista_funcionario.append(novo_funcionario)

print('\n Exibindo dados')
for funcionario in lista_funcionario:
    funcionario.mostrar_dados()

