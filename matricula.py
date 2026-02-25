import os

# Limpe o terminal.
os.system("cls")

# ENTRADA DE DADOS

matricula = int(input("Digite sua matricula: "))
certidao = int(input("Digite o ano do seu nascimento: ")) 
tempo_de_trabalho = int(input("Digite o tempo de trabalho: "))

print("\n- Processando dados -")

idade = 2026 - certidao

if idade >= 65 and tempo_de_trabalho >= 30:
    print("Requerer Aposentadoria")
    
else:
    print("Não requer Aposentadoria")



print("\n- Exibindo dados -")
print(f"Código: {matricula}")
print(f"Ano que Nasceu: {certidao}")
print(f"Total de anos Trabalhados: {tempo_de_trabalho}")
print(f"Idade: {idade}")


print("\n -------------- FIM DE EXECUÇÃO  ------------------\n ")