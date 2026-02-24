import os

# Limpe o terminal.
os.system("cls")

numero = int(input("Digite um número: "))

# Condicional composto
if numero > 10:
    print("É MAIOR QUE DEZ!")
if numero < 10:
    print("É MENOR QUE DEZ")
if numero == 10:
    print("É IGUAL A DEZ!")
    
print ("FIM")