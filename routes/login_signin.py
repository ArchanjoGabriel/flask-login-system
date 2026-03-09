from flask import Blueprint, render_template, request, redirect, url_for, session
from services.add_usuario import novo_usuario
from services.check_user import verificar_usuario
from services.session_check import session_required

# cria o app Flask 'login_signin' que é adicionado ao app.py (servidor principal) carregando as rotas contidas
login_signin = Blueprint("login_signin", __name__)

# rota "/signin" leva para a pagina de cadastro do site (signin.html)
# aceita métodos 'GET' para renderização da página e 'POST' para obter informações de formulários
@login_signin.route("/signin", methods=["GET", "POST"])
def signin_page():
    # verifica se um formulario de cadastro foi enviado usando o metodo 'POST'
    if request.method == "POST":
        # se verdadeiro, salva os dados (nome, email, senha) em variaveis
        nome_usuario = request.form.get("nome")
        email_usuario = request.form.get("email")
        senha_usuario = request.form.get("senha")

        # faz uma verificação para garantir que o usuario não tenha deixado campos em branco
        # se algum campo ficou em branco o usuário é alertado
        if not nome_usuario or not email_usuario or not senha_usuario:
            return "Preencha todos os campos"
        
        # feita a verificação os dados são enviadas para a função 'novo_usuario' que contém instruções para salvar as informações do usuário no banco de dados
        # a função está contida em: services/add_usuario.py
        usuario = novo_usuario(nome_usuario, email_usuario, senha_usuario)

        # garante que não possa existir 2 usuarios com o mesmo email
        if not usuario:
            return "Já existe um usuário com este e-mail cadastrado!"

        # apos o cadastro o usuario é redirecionado para a pagina de acesso especificando a rota da função 'login_page' contida neste arquivo
        return redirect(url_for("login_signin.login_page"))
    
    # garante que caso o usuario ja tenha realizado o login ele não precise realizar o login novamente
    if "usuario_id" in session:
        return redirect(url_for("main.main_page"))

    # renderiza o template que leva o usuário para a página onde ele pode realizar seu cadastro, caso ainda não o tenha feito    
    return render_template("signin.html")

# rota "/login" leva para a pagina de acesso do site (login.html)
# aceita métodos 'GET' para renderização da página e 'POST' para obter informações de formulários
@login_signin.route("/login", methods=["GET", "POST"])
def login_page():
    # verifica se um formulario de acesso foi enviado usando o metodo 'POST'
    if request.method == "POST":
        # se verdadeiro, salva os dados (email, senha) em variaveis
        email_usuario = request.form.get("email")
        senha_usuario = request.form.get("senha")

        # faz uma verificação para garantir que o usuario não tenha deixado campos em branco
        # se algum campo ficou em branco o usuário é alertado
        if not email_usuario or not senha_usuario:
            return "Preencha todos os campos"

        usuario = verificar_usuario(email_usuario, senha_usuario)
        """
        Função para verificar se o email e senha do usuário são válidos
        A função está contida em: services/check_user.py
        Retorna:
            Usuario -> se o login for válido
            None -> se email ou senha estiverem incorretos
        """

        # verifica se a variável'usuario' é diferente de None
        if usuario:
            # se sim o id e nome do usuário são salvos numa session e o usuário redirecionado para a pagina main
            session["usuario_id"] = usuario.id
            session["usuario_nome"] = usuario.nome
            return redirect(url_for("main.main_page"))
        
        # caso 'usuario'=None, o usuario é alertado
        else:
            return "Email ou Senha incorretos"
    # garante que caso o usuario ja tenha realizado o login ele não precise realizar o login novamente
    if "usuario_id" in session:
        return redirect(url_for("main.main_page"))
    
    # renderiza o template que leva o usuário para a página onde ele pode realizar seu acesso, caso ainda não o tenha feito
    return render_template("login.html")

# rota "/logout", contém a função para desconectar o usuário
@login_signin.route("/logout", methods=["GET", "POST"])

# decorator para garantir que o usuário só tenha direito de fazer logout caso já esteja conectado
@session_required

# função que remove todos os dados da session
def logout_page():

    # limpa todos os dados contidos na session
    session.clear()

    # após a limpeza redireciona o usuário para a rota ("/") contida em routes/index.py
    return redirect(url_for("index.index_page"))