import os

# Limpe o terminal.
os.system("cls")

# ENTRADA DE DADOS

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: ")) 


print("\n- Processando dados -")

imc = peso / (altura*altura)



if imc < 18.5:
    print("Abaixo do Peso")
elif imc == 18.6 <= imc <=  24.9:
    print("Peso Ideal (Parabéns!)")
elif imc == 25 <= imc <= 29.9:
    print("Levemente acima do Peso")
elif imc == 30 <= imc <= 34.9:
    print("Obesidade Grau I")
elif imc == 35 <= imc <= 39.9:
    print ("Obesidade Grau II (Severa)")
elif imc > 40:
    print("Obesidade III (Mórbida)")
    


print("\n- Exibindo dados -")
print(f"Peso: {peso}")
print(f"Altura: {altura}")
print(f"IMC: {imc}")


print("\n -------------- FIM DE EXECUÇÃO  ------------------\n ")
