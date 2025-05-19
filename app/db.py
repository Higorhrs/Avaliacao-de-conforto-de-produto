import mysql.connector
import os

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
