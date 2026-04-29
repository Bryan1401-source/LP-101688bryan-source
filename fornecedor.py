import os
from colorama import init, Back, Style, Fore
from dataclasses import dataclass

# Limpar tela
os.system ("CLS")

@dataclass
class Fornecedor:
    Nome: str
    Email: str
    Telefone: str
    Endereço: str

print('= Solicitando dados do Fornecedor =')
fornecedor = Fornecedor(
    Nome= input('Digite seu Nome: '),
    Email = input(' Digite seu E-mail: '),
    Telefone = input(' Digite seu Telefone: '),
    Endereço = input(' Digite seu Endereço: ')
)

print('\n= Exibindo dados do Fornecedor =')
print(f"Nome:{fornecedor.Nome}")
print(f"Idade:{fornecedor.Email}@gmail.com")
print(f"Peso: 719{fornecedor.Telefone}")
print(f"Endereço:{fornecedor.Endereço}")