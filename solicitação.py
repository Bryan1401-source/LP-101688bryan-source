import os

from colorama import init, Fore, Back, Style


# Limpe o terminal.
os.system("cls")

# ENTRADA DE DADOS

print ("\n Cadastre-se: ")

login = input(": Digite seu nome de usuário: ")
senha = int(input(": Digite sua senha: "))

if login and senha:
    print (f"\n {login} cadastrado com sucesso")
print ("\n ------ Inicio de Execução------")

print ("\n ----- Entre -----")   

login1 = (input("Digite seu nome de usuário: "))
senha1 = int(input("Digite sua senha: "))

print ("\n ------Tela de Bem-Vindo ------\n")

if login == login1 and senha == senha1:
    print(Fore.GREEN + f"\n Bem-vindo, {login1}")
else:
    print (Fore.RED + "Error - Login ou Senha inválido\n")
   
print(Style.RESET_ALL)

# print("\n- Exibindo dados -")  
  
# print (f": Usuário: ",  login)

# print (f": Senha: ",  senha)

# print("----------- FIM DA EXECUÇÃO ---------")
