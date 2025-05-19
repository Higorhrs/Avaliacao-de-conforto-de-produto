'''from flask import Flask, render_template, request, redirect # type: ignore
import os
from dotenv import load_dotenv 
import mysql.connector 

load_dotenv()
template_dir = os.path.abspath('templates')

app = Flask(__name__, template_folder=template_dir)
app.secret_key = '12345'


def conexão_db():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

def criar_tabela():
    conn = conexão_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS feedbacks (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(100),
            idade INT,
            sexo VARCHAR(10),
            email VARCHAR(100),
            produto VARCHAR(100),
            conforto VARCHAR(20),
            comentario TEXT
        );
    """)
    conn.commit()
    cursor.close()
    conn.close()
    print("✅ Tabela 'feedbacks' verificada/criada com sucesso.")


@app.route('/')
def home():
    return render_template('index.html') 

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        nome = request.form["nome"]
        idade = request.form["idade"]
        sexo = request.form["sexo"]
        email = request.form["email"]
        produto = request.form["produto"]
        conforto = request.form["conforto"]
        comentario = request.form.get("comentario")

    
        conn = conexão_db()
        cursor = conn.cursor()
        
        cursor.execute("INSERT INTO feedbacks (nome, idade, sexo, email, produto, conforto, comentario) VALUES (%s, %s, %s, %s, %s, %s, %s)",(nome, idade, sexo, email, produto, conforto, comentario))
        conn.commit()
        conn.close()

        return redirect('/')
        

@app.route('/test-db')
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
    


    
    
if __name__ == '__main__':
    criar_tabela()
    app.run(debug=True)
    
    
'''