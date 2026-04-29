import os
from colorama import init, Back, Style, Fore
from dataclasses import dataclass

# Limpar tela
os.system ("CLS")

@dataclass
class Pessoa:
    nome: str
    idade: int
@dataclass
class Pet:
    nome: str
    idade: int
    

pessoa1 = Pessoa('Marta', 20)
pet1 = Pet('Sacan', 5)
pessoa2 = Pessoa('Bryan', 16)
pet2 = Pet('Yoshi', 2)


print(f"Nome: {pessoa1.nome} \nIdade:  {pessoa1.idade}")
print(f"Nome: {pet1.nome} \nIdade:  {pet1.idade}")


print(f"Nome: {pessoa2.nome} \nIdade:  {pessoa2.idade}")
print(f"Nome: {pet2.nome} \nIdade:  {pet2.idade}")

