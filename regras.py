import os 

# Limpe o terminal.

os.system ("cls")

# ENTRADA DE DADOS

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

# ...

print("\n -------------- INICIO DE EXECUÇÃO  ------------------\n")

print("\n- Exibindo dados -")
print(f"Nome: {nome}")
print(f"Idade: {idade}")

if idade < 16:
    print("Você não pode votar!")
if idade == 17:
    print("Seu voto é opcional!")
if idade >= 18:
    print("Voto obrigatório!!")
if idade >= 65:
    print("Seu voto não é obrigatório!")    
  
    

print("\n -------------- FIM DE EXECUÇÃO  ------------------\n ")