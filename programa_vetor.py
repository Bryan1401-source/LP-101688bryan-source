
import os
from colorama import init, Fore

init(autoreset=True)

os.system ("cls")

# Criando um vetor.
vetor_notas = []
QUANTIDADES_NOTAS = 4
soma = 0

# Adicionando 3 notas
for i in range(QUANTIDADES_NOTAS):
    nota = float(input(Fore.YELLOW + f"Digite a {i+1}ª nota: "))
    soma += nota
    vetor_notas.append(nota)
    
media = soma / QUANTIDADES_NOTAS 

print("\n Exibindo dados")
#forEach 
# enumarate   
# Exibindo as notas informadas
for i, uma_nota in enumerate(vetor_notas, start=1):
    print(f"{i}ª Nota: {uma_nota}")
    
    
print(f"Média: {media}")
    