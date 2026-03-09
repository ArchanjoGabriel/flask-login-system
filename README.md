# Flask Login System

Sistema simples de autenticação desenvolvido com Flask.

## Tecnologias

- Flask
- SQLAlchemy
- PostgreSQL
- Werkzeug

## Funcionalidades

- Cadastro de usuário
- Login com verificação de senha
- Hash de senha
- Sessão de usuário
- Proteção de rotas com decorator `login_required`

## Como executar

1. Criar ambiente virtual

python -m venv venv

2. Ativar ambiente

Linux/Mac:
source venv/bin/activate

Windows:
venv\Scripts\activate

3. Instalar dependências

pip install -r requirements.txt

4. Configurar variáveis de ambiente

SECRET_KEY  
DATABASE_URL

5. Rodar aplicação

python app.py