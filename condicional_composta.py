import os

# Limpa o terminal
os.system("cls || clear")

idade = int(input("Digite sua idade: "))

# Condicional composta.
if idade >= 14:
    print("Acesso negado.")

else:
    print("Acesso permitido.")

print("Programa encerrado.")