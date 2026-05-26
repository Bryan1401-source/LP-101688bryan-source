// CRIANDO UM VETOR
const vetorNumeros = [18,20,30,40,50]

console.log(' Listando todos os elementos do vetor')
console.log(vetorNumeros)

console.log('\n Multiplicando cada elemento do vetor por 2: ')
const dobrados = vetorNumeros.map ( n => n * 2)
console.log(dobrados)
console.log(vetorNumeros)

console.log('\n Filtrando os elementos em impares')
vetorNumeros.push(1)
vetorNumeros.push(3)
const impares = vetorNumeros.filter(n => n % 2 == 1)
console.log(impares)

console.log('\n Filtrando os elementos em pares')
const pares = vetorNumeros.filter(n => n % 2 == 0)
console.log(pares)

console.log('\n Filtrando elementos negativos')
vetorNumeros.push(-2)
const negativos = vetorNumeros.filter(n => n < 0)
console.log(negativos)

console.log('\nSomando todos os elementos do vetor: ')
const total = vetorNumeros.reduce((soma, atual) => soma + atual, 0)
console.log(total)