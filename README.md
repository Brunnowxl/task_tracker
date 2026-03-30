# Task Tracker

Para utilizar o Task Tracker, após clonar o repositório na sua máquina, você
pode utilizar tanto pelo meio convencional, `python3 task-cli.py [args]`, como
pode transforma-lo em um executável simples, utiliza-se o comando `chmod +x
task-cli`, então roda o programa com `./task-cli [args]`, a linha reponsável por
permitir isto é a linha do topo `#!/bin/python3`.

## Utilizando o Task Tracker

Agora que ja sabe executar o arquivo, aqui estão as ações permitidas:
- Adicionar: utiliza o comando `add`
- Atualizar: utiliza o comando `update`
- Remover: utiliza o comando `delete`
- Marcar: É possível marcar tarefas como concluídas ou em andamento
- Listar: É possível listar todas as tarefas, ou por status

### Adicionando tarefas

Executa-se o arquivo utilizando `python3 task-cli.py` ou `./task-cli` seguido da
ação `add` e da tarefa a ser atribuída
Ex: `./task-cli add "estudar para a prova"`

É importante que, caso a descrição da tarefa seja uma frase, ela deve ser
colocada entre aspas. Se for uma atividade que consista apenas em uma palavra, 
não há necessidade das aspas

### Atualizando tarefas

Executa-se o arquivo seguido da ação `update`, do id da tarefa que será
atualizada e da nova descrição
Ex: `./task-cli update 1 "fazer atividade"`

Assim como para adicionar, é necessário colocar a descrição entre aspas caso ela
consista em uma frase

### Deletando tarefas

Executa-se o arquivo seguido da ação `delete` e do id da tarefa a ser deletada
Ex: `./task-cli delete 1`

### Marcando tarefas em andamento e concluída

Executa-se o arquivo seguido da ação de marcação que deve ser feita
Ex: `./task-cli mark-done 1`. Marca a tarefa com id 1 como concluída
Ex: `./task-cli mark-in-progress 1`. Marca a tarefa com id 1 como em andamento

### Listando tarefas

Caso o arquivo seja executado seguido apenas da `list`, é listada todas as
tarefas, para listar as tarefas a partir do seu status, seja em andamento, a
fazer ou conluída, adiciona-se o status da tarefa após o list
Ex: `./task-cli list`. Lista todas
Ex: `./task-cli list todo`. Tarefas a fazer
Ex: `./task-cli list done`. 
