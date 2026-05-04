import os
from dataclasses import dataclass

os.system('cls')

@dataclass
class Pet:
    nome: str
    idade: int
    raca: str

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade} anos")
        print(f"Raça: {self.raca}")
        print("-" * 20)

lista_pets = []

print("--- Início do Cadastro de Pets ---")

while True:
    nome = input("\nDigite o nome do pet: ")
    idade = int(input("Digite a idade do pet: "))
    raca = input("Digite a raça do pet: ")

    novo_pet = Pet(nome=nome, idade=idade, raca=raca)
    lista_pets.append(novo_pet)

    opcao = input("Deseja cadastrar outro pet? (sim/não): ").lower()
    if opcao != 'sim':
        break

print("\n--- Pets Cadastrados ---")
for pet in lista_pets:
    pet.exibir_dados()

if not lista_pets:
    print("Nenhum pet cadastrado.")