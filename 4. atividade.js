// CALCULE A MÉDIA ARITMÉTRICA DO VETOR ABAIXO:
// UTILIZE OS RECURSOS DO ES6.

notas = [10,10,10]

console.log(`Calculando a média aritmética do vetor: `)
const media = notas.reduce((soma, atual) => soma + atual, 0) / 3
console.log(media)