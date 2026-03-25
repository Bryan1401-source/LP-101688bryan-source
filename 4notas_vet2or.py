import os 
from colorama import init, Fore 

init(autoreset = True)

#Limpa o Terminal
os.system ("cls")



# Criando um Vetor.

# --- Criador um vetor para armazenar as notas ---

vetor_notas = []
QUANTIDADE_DE_NOTAS = 4

print(f"{Fore.CYAN} --- Sistema de Notas --- \n")

# Loop para ler as 4 notas

for i in range(QUANTIDADE_DE_NOTAS):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    vetor_notas.append(nota)
    
# Calculo de média aritmétrica

media = sum(vetor_notas) / len(vetor_notas)

# --- Lógica de verificação da aprovação---

if media >= 7:
    situacao = f"{Fore.GREEN}Aprovado"
elif media >= 5:
    situacao = f"{Fore.YELLOW}Recuperação" 
else:
    situacao = f"{Fore.RED}Reprovado"
    
 # --- Exibição dos resultados ---
print("\n" + "="*30)
print(f"Notas: {vetor_notas}")
print(f"Média final: {media:.2f}")
print(f"Situação: {situacao}")
print("="*30)


