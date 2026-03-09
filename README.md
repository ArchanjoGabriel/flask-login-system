# Flask Login System

Sistema simples de autenticação desenvolvido com **Flask**, com cadastro de usuários, login seguro e proteção de rotas.

🔗 **Aplicação online:**  
https://flask-login-system-z76s.onrender.com/

---

## 🚀 Funcionalidades

- Cadastro de usuários
- Login com autenticação segura
- Hash de senha
- Sessões de usuário
- Proteção de rotas com decorator `login_required`
- Verificação de email duplicado
- Logout

---

## 🛠 Tecnologias utilizadas

- Python
- Flask
- SQLAlchemy
- PostgreSQL
- Werkzeug
- HTML / Jinja2

---

## 🔐 Segurança

O projeto implementa algumas práticas básicas de segurança:

- Senhas armazenadas com **hash criptográfico**
- Sessões protegidas com `SECRET_KEY`
- Verificação para impedir cadastro com email duplicado
- Rotas protegidas usando decorator `login_required`

---


---

## ⚙️ Como executar localmente

### 1. Clonar o repositório

 - git clone https://github.com/ArchanjoGabriel/flask-login-system.git

### 2. Entrar na pasta

 - cd flask-login-system

### 3. Criar ambiente virtual

 - python -m venv venv

### 4. Ativar ambiente

 - Linux / Mac

 - source venv/bin/activate

 - Windows

 - venv\Scripts\activate

 ### 5. Instalar dependências

 - pip install -r requirements.txt

 ### 6. Configurar variáveis de ambiente

 - SECRET_KEY=sua_secret_key
 - DATABASE_URL=sua_database_url

 ### 7. Rodar aplicação

 - python app.py

---

## 📚 Objetivo do projeto

Este projeto foi desenvolvido com objetivo de praticar:

- desenvolvimento backend com Flask
- autenticação de usuários
- integração com banco de dados
- boas práticas de organização de código

---

## 👨‍💻 Autor

**Gabriel Archanjo**

GitHub:  
https://github.com/ArchanjoGabriel