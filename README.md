# README

## Descrição da Aplicação

Esta é uma API em Python Flask que permite aos usuários registrar seus aumigos, criar rotinas de alimentação e receber notificações para alimentar seus cachorros em horários específicos. A API utiliza o Swagger para documentação e teste de endpoints.

## Como Executar

1. Certifique-se de ter o Python instalado. Você pode fazer o download em [python.org](https://www.python.org/).

2. Clone este repositório para o seu ambiente local:

    ```
    git clone https://github.com/Rodrigocambraia14/DoggoReminder.API.git
    ```

3. Navegue até o diretório do projeto:

    ```
    cd DoggoReminder.API
    ```

. Ative o ambiente virtual:

    - No Windows:

    ```
    venv\Scripts\activate
    ```

    - No macOS e Linux:

    ```
    source venv/bin/activate
    ```

5. Execute o aplicativo Flask:

    ```
    python app.py
    ```

6. Acesse a documentação Swagger em seu navegador, geralmente em `http://localhost:5000/swagger`, para visualizar e testar os endpoints disponíveis.

## Requirements

bcrypt==4.1.2
blinker==1.7.0
click==8.1.7
colorama==0.4.6
Flask==3.0.2
Flask-Cors==4.0.0
flask-swagger-ui==4.11.1
itsdangerous==2.1.2
Jinja2==3.1.3
MarkupSafe==2.1.5
schedule==1.2.1
Werkzeug==3.0.1


## Observações

1. Este projeto é apenas um MVP, portanto, não possui recursos como autenticação JWT, OAuth2, endpoints de funcionalidades complexas e afins.

## Exemplo de Uso

1. Autentique utilizando o usuário da seed: tester@PUCRIO.com e a senha: PUC@123
1. Registre um cachorro utilizando o endpoint **POST /dogs/add**.
2. Crie uma rotina de alimentação para o cachorro utilizando o endpoint **POST /food_routines/add_**.
3. Receba notificações para alimentar o cachorro nos horários especificados utilizando o endpoint **GET /food_routine/get_notifications**, ou utilizando o front DoggoReminderUI.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
