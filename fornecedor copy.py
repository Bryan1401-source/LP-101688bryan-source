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

    def mostrar_dados(self):
        print(f"Nome:{self.Nome}")
        print(f"Peso: 719{self.Telefone}")
        print(f"Endereço:{self.Endereço}")
        print(f"Idade:{self.Email}@gmail.com")


print('= Solicitando dados do Fornecedor =')
fornecedor = Fornecedor(
    Nome= input('Digite seu Nome: '),
    Email = input(' Digite seu E-mail: '),
    Telefone = input(' Digite seu Telefone: '),
    Endereço = input(' Digite seu Endereço: ')
)

print('\n= Exibindo dados do Fornecedor =')
fornecedor.mostrar_dados()
