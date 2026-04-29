import os
from colorama import init, Back, Style, Fore
from dataclasses import dataclass

# Limpar tela
os.system ("CLS")

@dataclass
class Cliente:
    nome: str
    email: str
    telefone: str

    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"E-Mail: {self.email}")
        print(f"Telefone: {self.telefone}")

print('= Solicitando dados do Cliente =')
cliente = Cliente(
    nome= input('Digite seu nome: '),
    email= input(' Digite seu e-mail: '),
    telefone = input(' Digite seu telefone: ')
)

print('\n= Exibindo dados do cliente =')
cliente.mostrar_dados()