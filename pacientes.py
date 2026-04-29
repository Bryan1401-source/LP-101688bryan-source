import os
from colorama import init, Back, Style, Fore
from dataclasses import dataclass

# Limpar tela
os.system ("CLS")

@dataclass
class Paciente:
    nome: str
    idade: str
    Peso: str
    Altura: str

print('= Solicitando dados do Paciente =')
paciente = Paciente(
    nome= input('Digite seu Nome: '),
    idade = input(' Digite sua Idade: '),
    Peso = input(' Digite seu Peso: '),
    Altura = input(' Digite sua Altura: ')
)

print('\n= Exibindo dados do cliente =')
print(f"Nome:{paciente.nome}")
print(f"Idade:{paciente.idade} Anos")
print(f"Peso:{paciente.Peso} KG")
print(f"Altura:{paciente.Altura} M")