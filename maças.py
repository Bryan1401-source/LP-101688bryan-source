import os

# Limpe o terminal.
os.system("cls")

# ENTRADA DE DADOS

maças = float(input("Quantidade de maçãs desejada: "))

if maças < 12:
    produto = maças*1.30
else:
    maças >= 12
    produto = maças*1.00
    
    
print("\n- Exibindo dados -")
print(f"Quantidade de maçãs: R$ {maças} reais")
print(f"Valor total da compra: R$ {produto} reais")

print("\n -------------- FIM DE EXECUÇÃO  ------------------\n ")