import os

# Limpe o terminal.
os.system("cls")

# ENTRADA DE DADOS

primeiro_numero = int(input("Digite um número: "))
segundo_numero = int(input("Digite um número: "))

# ...

print("\n -------------- INICIO DE EXECUÇÃO  ------------------\n")


maior = max(primeiro_numero, segundo_numero)
menor = min(primeiro_numero, segundo_numero)


print("\n- Exibindo dados -")
print(f"Primeiro Número: {primeiro_numero}")
print(f"Segundo Número: {segundo_numero}")
print(f"É maior: {maior}")
print(f"É menor: {menor}")

print("\n -------------- FIM DE EXECUÇÃO  ------------------\n ")
