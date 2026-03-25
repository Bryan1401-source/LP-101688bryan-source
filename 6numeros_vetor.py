import os 
from colorama import init, Fore 

init(autoreset = True)

#Limpa o Terminal
os.system ("cls")



print(f"{Fore.CYAN}--- Contador de Pares e Impares --- /n")

# Criando o vetor e os contadores

numero = []
pares = 0
impares = 0
quantidade_de_numeros = 6

# Lendo os 6 números

for i in range(quantidade_de_numeros):
    num = int(input(f"Digite a {i+1}º número inteiros: "))
    numero.append(num)
    
    # Veerificando se é par ou impar
    
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
        
        
# Exibindo resultados

print("\n" + "="*35)
print(f"{Fore.YELLOW}Números informados: {numero}")
print(f"{Fore.GREEN}Quantidade de PARES: {pares}")
print(f"{Fore.MAGENTA}Quantidade de ÍMPARES: {impares}")
print("="*35)