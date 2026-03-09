from flask import Blueprint, render_template

index = Blueprint("index", __name__)

# rota "/" carrega a pagina inicial do site (index.html)
@index.route("/")
def index_page():
    return render_template("index.html")