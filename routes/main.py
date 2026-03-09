from flask import Blueprint, render_template, session
from services.session_check import session_required

# cria o app Flask 'main' que é adicionado ao app.py (servidor principal) carregando as rotas contidas
main = Blueprint("main", __name__)

# rota "/main" leva para a pagina principal do site (signin.html)
@main.route("/main")

# decorator para garantir que o usuário só tenha direito de fazer logout caso já esteja conectado
# localizado em: services/session_check.py
@session_required

# função para renderizar a página 'main.html'
def main_page():
    # renderiza a página 'main.html' e usa variáveis para gerar html dinâmico
    return render_template("main.html", usuario_nome=session["usuario_nome"])