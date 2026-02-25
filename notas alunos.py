import os 

# Limpe o terminal.

os.system ("cls")

# ENTRADA DE DADOS

nome = input("Aluno, Digite seu nome: ")
nota1 = float(input("Digite a nota da primeira unidade: "))
nota2 = float(input("Digite a nota da segunda unidade: "))

media = (nota1+nota2) / 2

print("\n- Exibindo dados -")
print(f"Nome do Aluno: {nome}")
print(f"Primeira Unidade: {nota1}")
print(f"Segunda Unidade: {nota2}")
print(f"Media Total: {media}")

if media >= 9:
    print("Aprovado")
elif media == 7.5 <= media <= 9:
    print("Aprovado")
elif media == 6 <= media <= 7.5:
    print("Aprovado")
elif media >= 4 <= media <= 6:
    print("Reprovado")
else:
    print("Reprovado")
    

    


print("\n -------------- FIM DE EXECUÇÃO  ------------------\n ")    