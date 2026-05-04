import os
from dataclasses import dataclass
from colorama import init, Style, Back, Fore

os.system('CLS')

@dataclass
class Cliente:
    nome: str
    idade: int
    peso: str
    altura: str

    def mostrar_dados(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}\n')
        print(f'Peso: {self.peso}\n')
        print(f'Altura: {self.altura}\n')

lista_clientes = []


print('Solicitando dados')
for i in range(2):
    novo_cliente = Cliente(
        nome = input('Digite seu nome: '),
        idade= int(input('Digite sua idade: ')),
        peso= input('Digite seu peso: '),
        altura= input('Digite sua altura: ')
    )
    lista_clientes.append(novo_cliente)

print('\n Exibindo dados')
for cliente in lista_clientes:
    cliente.mostrar_dados()