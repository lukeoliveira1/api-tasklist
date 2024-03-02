
API de Gerenciamento de Tarefas
Esta é uma API simples para gerenciar tarefas com Django Rest Framework. A API permite criar, listar, atualizar e excluir tarefas.

Modelos
Task
title (CharField): Título da tarefa (máximo de 50 caracteres).
status (CharField): Situação da tarefa, com opções 'A fazer', 'Em progresso' e 'Concluída'.
description (TextField): Descrição da tarefa (máximo de 250 caracteres).
Endpoints
Listar Todas as Tarefas
GET /api/tasks/

Retorna todas as tarefas cadastradas.

Criar uma Nova Tarefa
POST /api/tasks/

Cria uma nova tarefa com base nos dados fornecidos no corpo da requisição.

Corpo da Requisição
json
Copy code
{
    "title": "Título da Tarefa",
    "status": "TODO",
    "description": "Descrição da Tarefa"
}
Detalhes de uma Tarefa
GET /api/tasks/<id>/

Retorna os detalhes de uma tarefa específica com base no ID fornecido.

Atualizar uma Tarefa
PUT /api/tasks/<id>/

Atualiza os detalhes de uma tarefa específica com base no ID fornecido.

Corpo da Requisição
json
Copy code
{
    "title": "Novo Título da Tarefa",
    "status": "IN_PROGRESS",
    "description": "Nova Descrição da Tarefa"
}
Excluir uma Tarefa
DELETE /api/tasks/<id>/

Exclui uma tarefa específica com base no ID fornecido.

Autenticação
A API não requer autenticação para acessar os endpoints.
