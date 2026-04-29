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

    def mostrar_dados(self):
        print(f"Nome:{self.nome}")
        print(f"Idade:{self.idade} Anos")
        print(f"Peso:{self.Peso} KG")
        print(f"Altura:{self.Altura} M")


print('= Solicitando dados do Paciente =')
paciente = Paciente(
    nome= input('Digite seu Nome: '),
    idade = input(' Digite sua Idade: '),
    Peso = input(' Digite seu Peso: '),
    Altura = input(' Digite sua Altura: ')
)

print('\n= Exibindo dados do cliente =')
paciente.mostrar_dados()
