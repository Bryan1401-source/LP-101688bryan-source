const idade = 65

if (idade >= 65) {
    console.log('Seu voto não é obrigatório')
} else if (idade >= 18) {
    console.log('Seu voto é obrigatório.')
} else if (idade == 16 || idade == 17) {
    console.log('Seu voto é opcional')
} else {
    console.log ('Você não pode votar')
}