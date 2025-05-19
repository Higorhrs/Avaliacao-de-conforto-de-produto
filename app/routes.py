from flask import Blueprint, render_template, request, redirect, Flask
from .db import conexão_db
  


main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template(
        'index.html'
        )

@main.route('/submit', methods=['POST'])
def submit():
    nome = request.form["nome"]
    idade = request.form["idade"]
    sexo = request.form["sexo"]
    email = request.form["email"]
    produto = request.form["produto"]
    conforto = request.form["conforto"]
    comentario = request.form.get("comentario")

    print(f"Recebido: {nome}, {idade}, {sexo}, {email}, {produto}, {conforto}, {comentario}") 
    

    conn = conexão_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO feedbacks (nome, idade, sexo, email, produto, conforto, comentario)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (nome, idade, sexo, email, produto, conforto, comentario))
    conn.commit()
    conn.close()

    return redirect('/')

@main.route('/test-db')
def test_db():
    try:
        conn = conexão_db()
        cursor = conn.cursor()
        cursor.execute("SELECT 1")
        result = cursor.fetchone()
        conn.close()
        return "Conexão bem-sucedida com o banco de dados!"
    except Exception as e:
        return f"Erro ao conectar ao banco de dados: {str(e)}"
