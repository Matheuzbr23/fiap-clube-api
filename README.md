# fiap-clube-api
 fiap-clube-api

Necessário ter o **Python3** instalado na maquina para rodar a aplicação localmente.

Após clonar o repositório siga os seguintes steps para rodar a aplicação local:

1) Executar o comando "python3 manage.py migrate" em algum CLI de sua preferencia para que seja criado as tabelas do banco de dados (Necessário ter instalado o postgresql localmente na maquina)

2) Executar o comando "python3 manage.py createsuperuser" e seguir os steps no CLI a fim de criar um super usuário que será utilizado na autenticação do serviço.

3) Executar o comando "python manage.py runserver" para subir a aplicação localmente.

4) Acessar o http://localhost:8000/ (A documentação swagger com todas as rotas podem ser visualizadas http://localhost:8000/api/schema/swagger-ui/)

