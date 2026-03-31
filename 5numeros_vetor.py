import os

# Inicialização do vetor e variáveis
numeros = []
negativos_qtd = 0
soma_positivos = 0

print("Digite 5 números:")

# Preenchendo o vetor
for i in range(5):
    num = float(input(f"Posição {i+1}: "))
    numeros.append(num)
    
    # Processamento dos dados
    if num < 0:
        negativos_qtd += 1
    else:
        soma_positivos += num

# Exibição dos resultados
print("\n--- RESULTADO ---")
print(f"Vetor completo: {numeros}")
print(f"Quantidade de números negativos: {negativos_qtd}")
print(f"Soma dos números positivos: {soma_positivos}")
