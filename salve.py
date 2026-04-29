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

print('= Solicitando dados do Cliente =')
cliente = Cliente(
    nome= input('Digite seu nome: '),
    email= input(' Digite seu e-mail: '),
    telefone = input(' Digite seu telefone: ')
)

print('\n= Exibindo dados do cliente =')
print(f"Nome: {cliente.nome}")
print(f"E-Mail: {cliente.email}")
print(f"Telefone: {cliente.telefone}")