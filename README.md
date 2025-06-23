# Projeto Django - Todo List

Este é um projeto de uma lista de tarefas (Todo List) desenvolvido com Django e Bootstrap.

## Funcionalidades

- Listar tarefas
- Adicionar nova tarefa
- Editar tarefa existente
- Deletar tarefa
- Marcar tarefa como concluída (checkbox)

## Tecnologias utilizadas

- Python 
- Django 
- SQLite (banco de dados padrão)
- Bootstrap ( estilo da interface)

## Como rodar o projeto localmente

1. Clone este repositório:
   git clone https://github.com/seu-usuario/seu-repositorio.git

2.  Entre na pasta do projeto:
   
cd DjangoDB

3. Crie e ative o ambiente virtual:

  py -m venv venv
  venv\Scripts\activate 

4. Execute as migrações do banco de dados:
   python manage.py migrate

5. Rode o servidor:
python manage.py runserver
