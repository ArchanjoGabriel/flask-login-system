from flask import Flask
from routes.index import index
from routes.login_signin import login_signin
from routes.main import main
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

app.secret_key = os.getenv("SECRET_KEY")
app.register_blueprint(index)
app.register_blueprint(login_signin)
app.register_blueprint(main)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)