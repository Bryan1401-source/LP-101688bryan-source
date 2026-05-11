document.querySelector('.add-task-box button').addEventListener('click', function() {
    const input = document.getElementById('taskInput');
    const taskText = input.value;

    if (taskText === '') {
        alert("Digite uma atividade primeiro!");
        return;
    }

    const taskList = document.querySelector('.task-list');

    // Criando a estrutura da nova tarefa
    const newTask = document.createElement('div');
    newTask.classList.add('task-item');
    newTask.innerHTML = `
        <input type="checkbox" class="task-check">
        <div class="task-info">
            <span>${taskText}</span>
            <small>Recém adicionada</small>
        </div>
        <button class="delete-btn" style="background:none; border:none; cursor:pointer; color:red; margin-left:auto;">🗑️</button>
    `;

    taskList.appendChild(newTask);
    input.value = ''; // Limpa o campo

    // Lógica para excluir
    newTask.querySelector('.delete-btn').addEventListener('click', () => {
        newTask.remove();
    });

    // Lógica para riscar ao concluir
    newTask.querySelector('.task-check').addEventListener('change', function() {
        if(this.checked) {
            newTask.style.opacity = "0.5";
            newTask.querySelector('span').style.textDecoration = "line-through";
        } else {
            newTask.style.opacity = "1";
            newTask.querySelector('span').style.textDecoration = "none";
        }
    });
});