import os
import time


def logoSenai():
    os.system("cls || clear")
    print("=== SENAI === ")

def calcular_situacao_imc(peso, altura):
    imc = peso / (altura ** 2)
    
    if imc < 18.5:
        situacao = "Você está abaixo do peso"
    elif imc < 25:
        situacao = "Peso normal"
    elif imc < 30:
        situacao = "Sobrepeso"
    elif imc < 35:
        situacao = "Obesidade grau I"
    elif imc < 40:
        situacao = "Obesidade grau II"
    else:
        situacao = "Obesidade grau III (mórbida)"
        
    return imc, situacao

nomes_completos = []
idades = []
alturas = []
pesos = []

while True:
    logoSenai()
    nome = input("Digite o primeiro nome do usuário (ou 'sair' se quiser encerrar!): ")
    
    if nome.lower() == 'sair':
        print("Encerrando o programa. Obrigado por participar!")
        time.sleep(3)
        break
    
    sobrenome = input("Digite o sobrenome do usuário: ")
    idade = int(input("Digite a idade do usuário: "))
    altura = float(input("Digite a altura do usuário: "))
    peso = float(input("Digite o peso do usuário: "))
    
    nomes_completos.append(f"{nome} {sobrenome}")
    idades.append(idade)
    alturas.append(altura)
    pesos.append(peso)

logoSenai()
print("\nRelatório Final de Pesquisas:")

for i in range(len(nomes_completos)):
    # Chamada da função de cálculo para cada usuário
    imc_valor, status = calcular_situacao_imc(pesos[i], alturas[i])
    
    print(f"--- Usuário {i+1} ---")
    print(f"Nome Completo: {nomes_completos[i]}")
    print(f"Idade: {idades[i]} anos")
    print(f"Altura: {alturas[i]}m")
    print(f"Peso: {pesos[i]}kg")
    print(f"IMC: {imc_valor:.2f}")
    print(f"Situação: {status}")
    print("-" * 20)

