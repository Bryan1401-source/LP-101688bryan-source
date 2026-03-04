import os

from colorama import init, Fore, Back, Style

# Limpe o terminal.
os.system("cls")

print ("\n ------ BEM VINDO ALUNO ------")


usuario = input("Digite seu nome de usuário: ")
primeira_nota = float(input("Digite a nota da primeira unidade: "))
segunda_nota = float(input("Digite a nota da primeira unidade: "))
terceira_nota = float(input("Digite a nota da primeira unidade: "))
faltas = int(input("Digite quantas falta você tem: "))

print ("\n ------ RESULTADO ------")

media = (primeira_nota + segunda_nota + terceira_nota) / 3

if faltas <= 40 and media >= 7:
    print(Fore.GREEN + f"{usuario}, Você foi aprovado(a), parabéns!!!")
else:
    print(Fore.RED + f"{usuario}, foi Reprovado!")


print(Style.RESET_ALL) 

print("\n- Exibindo dados -")  

print (f": Aluno: ",  usuario)
print (f": I Unidade: ",  primeira_nota)
print (f": II Unidade: ",  segunda_nota)
print (f": III Unidade: ",  terceira_nota)
print (f": Total de Faltas: ", faltas)
print (f"Media Final", media)
