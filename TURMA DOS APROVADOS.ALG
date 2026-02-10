Algoritmo "Turma dos Aprovados"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 10/02/2026
Var
// Seção de Declarações das variáveis
   nome: caractere
   turma: caractere
   idade: inteiro
   primeira_nota: real
   segunda_nota: real
   terceira_nota: real
   soma: real
   nota: real
   media: real
   resultado: caractere

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
   // ENTRADA DE DADOS
   escreva("Digite seu nome: ")
   leia(nome)
   
   escreva("turma: ")
   leia(turma)
   
   escreva("idade: ")
   leia(idade)
   
   escreva("Digite a primeira nota: ")
   leia(primeira_nota)
   
   escreva("Digite a segunda nota: ")
   leia(segunda_nota)
   
   escreva("Digite a terceira nota: ")
   leia(terceira_nota)
   
   
   //PROCESSAMENTO
   soma <- primeira_nota + segunda_nota + terceira_nota

   media <- soma / 3
   
 //media <- primeira_nota + segunda_nota + terceira_nota / 2
 
    se media >= 5 entao
       resultado <- "Aprovado"
    senao
         resultado <- "Reprovado"
    fimse
    

   // SAÍDA
   escreval
   escreva("Nome: ",nome, " Almeida")
   escreval
   escreva("Turma: ",turma)
   escreval
   escreva("Idade: ", idade, " anos")
   escreval
   escreva("Notas: ",primeira_nota,segunda_nota,terceira_nota)
   escreval
   escreva("Media: ",media, " pontos")
   escreval
   escreva("Resultado: ", resultado)


Fimalgoritmo
