import os
from colorama import init, Back, Style, Fore
from dataclasses import dataclass

os.system("cls")

@dataclass
class Endereço:
    logradouro: str
    numero: int

@dataclass
class Cliente:
    nome: str
    idade: int
    endereço: Endereço

    def mostrar_dados (self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Endereço: {self.endereço.logradouro}")
        print(f"Número: {self.endereço.numero}")




print('= Solicitando dados do Cliente =')
cliente = Cliente(
    nome= input('Digite seu nome: '),
    idade = input(' Digite sua idade: '),
    endereço = Endereço(
    logradouro= input(' Digite seu endereço: '),
    numero = input('Digite seu número: ')
    ))

print('\n= Exibindo dados do cliente =')
cliente.mostrar_dados()