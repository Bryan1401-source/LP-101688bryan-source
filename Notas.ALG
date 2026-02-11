Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 11/02/2026
Var
// Seção de Declarações das variáveis 

primeira_nota : real
segunda_nota : real
terceira_nota : real
media : real
resultado : caractere


Inicio
          // ENTRADA DE DADOS
  escreva("Primeira Unidade: ")
  leia(primeira_nota)
  escreva("Segunda Unidade: ")
  leia(segunda_nota)
  escreva("Terceira Unidade: ")
  leia(terceira_nota)

          // PROCESSAMENTO
  
  media <- primeira_nota + segunda_nota + terceira_nota / 3
  
  se media >= 7 entao
     resultado <- "Aprovado"
  senao
      resultado <- "Reprovado"
      
   fimse
      
      
          // SAÍDA
          
  escreval
  escreva("Media Final: ",media:3:1)
  escreval
  escreva("Resultado Final: ",resultado)
      

  


Fimalgoritmo