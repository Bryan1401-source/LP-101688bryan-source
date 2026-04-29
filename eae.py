import os
from colorama import init, Back, Style, Fore
from dataclasses import dataclass

os.system("cls")

@dataclass
class Cliente:
    nome: str
    email: str
    telefone: str

@dataclass
class Funcionario:
    nome: str
    email: str
    matricula: str
    setor: str

cliente1 = Cliente('Bryan', 'bryan@gmail.com', '719484928')
funcionario1 = Funcionario('Carlos', 'carlosfuncionario@gmail.com', '29586', 'Financeiro')

print(f'Nome:  {cliente1.nome}')
print(f"E-Mail: {cliente1.email}")
print(f"Telefone: {cliente1.telefone}\n")

print(f'Nome:  {funcionario1.nome}')
print(f"E-Mail: {funcionario1.email}")
print(f"Matricula: {funcionario1.matricula}")
print(f"Setor: {funcionario1.setor}")
