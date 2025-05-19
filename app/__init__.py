from flask import Flask
from .db import criar_tabela
from dotenv import load_dotenv
import os

def create_app():
    load_dotenv()
    
    app = Flask(__name__)
    app.secret_key = os.getenv("SECRET_KEY", "12345")

    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    criar_tabela()
    return app
