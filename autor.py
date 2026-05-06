import os
from dataclasses import dataclass
os.system('cls')

@dataclass
class Livro:
    nome: str
    autor: str
    categoria: str
    preço: str

lista_livros = []

while True:
    os.system('cls')
    print("\n--- SISTEMA DE CADASTRO ---")
    print("1 - Adicionar Livro")
    print("2 - Listar Livros")
    print("3 - Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        os.system('cls')
        livro_novo = Livro(
            nome=input("Nome: "),
            autor=input("Autor: "),
            categoria=input("Categoria: "),
            preço=input("Preço: ")
        )
        lista_livros.append(livro_novo)
        
        with open('catalogo_livros.csv', 'a', encoding='utf-8') as arquivo:
            arquivo.write(f'{livro_novo.nome}, {livro_novo.autor}, {livro_novo.categoria}, {livro_novo.preço}\n')
        print("Livro adicionado e salvo!")

    elif opcao == '2':
        try:
            os.system('cls')
            print("\n--- Lista de Livros ---")
            if not lista_livros:
                print("Nenhum livro cadastrado nesta sessão.")
            else:
                for l in lista_livros:
                    print(f"Livro: {l.nome} | Autor: {l.autor} | R${l.preço}")
        except FileNotFoundError:
            print('Arquivo não encontrado')

    elif opcao == '3':
        os.system('cls')
        print("Saindo do programa...")
        break
    
    else:
        print("Opção inválida!")
