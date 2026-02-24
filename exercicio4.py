import os

# Limpe o terminal.
os.system("cls")

# ENTRADA DE DADOS

primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))

# ...

print("----------- INICIO DA EXECUÇÃO -----------") 


media = (primeiro_numero+segundo_numero) / 2
soma = (primeiro_numero+segundo_numero)
produto = (primeiro_numero*segundo_numero)

if primeiro_numero>segundo_numero:
    print("É o maior número",primeiro_numero)    
else:
    print("\nÉ o maior número:",segundo_numero)     
if primeiro_numero<segundo_numero:
    print("É o menor número",primeiro_numero)    
else:
    print("É o menor número:",segundo_numero)

# SAIDA DE DADOS    
    
print("\n- Exibindo dados -")    
print(f": Média",  media)
print (f": Soma",  soma)
print(f": Produto", produto)

print("----------- FIM DA EXECUÇÃO ---------")