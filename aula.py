import os

# Limpe o terminal.
os.system("cls")

# ENTRADA DE DADOS

primeiro_inteiro = int(input("Digite um número: "))
segundo_inteiro = int(input("Digite um número: "))

# ...

print("\n -------------- INICIO DE EXECUÇÃO  ------------------\n")

media = (primeiro_inteiro+segundo_inteiro) / 2
soma = (primeiro_inteiro+segundo_inteiro)
produto = (primeiro_inteiro*segundo_inteiro)

menor = min(primeiro_inteiro, segundo_inteiro)
maior = max(primeiro_inteiro, segundo_inteiro)

if primeiro_inteiro == segundo_inteiro:
    print("Os números são iguais")

print("\n- Exibindo dados -")
print(f"Soma: {soma}")
print(f"Média: {media}")
print(f"Produto: {produto}")
print(f"Maior número: {maior}")
print(f"Menor número: {menor}")

print("\n -------------- FIM DE EXECUÇÃO  ------------------\n ")