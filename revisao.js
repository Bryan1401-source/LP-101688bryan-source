// CRIADOR DO VETOR
const vetorNumeros = [18,20,30,40,50]

console.log (`Exibindo todos os elementos`)
console.log(vetorNumeros)

console.log(`\n Exibindo apenas o primeiro elemento`)
console.log(vetorNumeros[0])

console.log(`\n Exibindo apenas o segundo elemento`)
console.log(vetorNumeros[1])

console.log(`\nAdicionando um elemento no final do vetor: `)
vetorNumeros.push(60)
console.log(vetorNumeros)

console.log(`\nAdicionando um elemento no inicio do vetor: `)
vetorNumeros.unshift(0)
console.log(vetorNumeros)

// REMOVE APENAS O ULTIMO ELEMENTO DO VETOR:

console.log(`\nRemovendo o ultimo elemento do vetor: `)
vetorNumeros.pop()
console.log(vetorNumeros)

// REMOVE APENAS O PRIMEIRO ELEMENTO DO VETOR:
console.log(`\nRemovendo o primeiro elemento do vetor: `)
vetorNumeros.shift()
console.log(vetorNumeros)