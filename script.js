// Função que irá executar quando clicar no botão btnGerar.
function gerarTabuada () { 
    // Pega o valor do campo input HTML.
    const numeroInput = document.getElementById('numeroInput')
    let numero = parseInt(numeroInput.value)

    const resultadoDiv = document.getElementById('resultadoTabuada')

    // Limpa o conteúdo anterior
    resultadoDiv.innerHTML = ''

    // Adiciona Titulo para Tabuada
    resultadoDiv.innerHTML += `<h2>Tabuada do numero ${numero}: </h2>`

    // Laço de repetição para calcular a tabuada do numero
    for (let i = 1; i <= 10; i++) { // CORRIGIDO: mudado '1 <= 10' para 'i <= 10'
        let resultado = numero * i
        resultadoDiv.innerHTML += `<p>${numero} x ${i} = ${resultado}</p>`
    }
} 

const btnGerar = document.getElementById('btnGerar')
btnGerar.addEventListener('click', gerarTabuada)
