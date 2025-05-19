# Avaliação de Conforto de Produto

Este projeto é uma aplicação web desenvolvida em **Python** com o framework **Flask**, que coleta feedbacks de usuários sobre o conforto de produtos. Os dados inseridos pelos usuários são armazenados em um banco de dados **MySQL** e podem ser integrados a um servidor remoto na **AWS**.

## 📌 Objetivo

O objetivo principal é obter avaliações qualitativas e quantitativas dos usuários sobre determinados produtos, facilitando análises sobre conforto, uso e experiência.

---

## 🚀 Tecnologias Utilizadas

- **Python 3.11**
- **Flask**
- **Jinja2**
- **MySQL** (local e AWS RDS)
- **HTML/CSS**
- **VS Code**
- **Git/GitHub**
- **MySQL Workbench**
- **Amazon Web Services (AWS RDS)**

---
# Formulário de Avaliação
<img src="./Avaliacao-de-conforto-de-produto/templates/image (4).png" alt="Logo" width="200"/>

# Conexão com Banco de Dados
<img src="./Avaliacao-de-conforto-de-produto/templates/image (5).png" alt="Logo" width="200"/>



## 🛠️ Instalação

1. Clone o repositório:

```bash
git clone https://github.com/Higorhrs/Avaliacao-de-conforto-de-produto.git
cd Avaliacao-de-conforto-de-produto

## 🛠️ Crie e ative o ambiente virtual
python -m venv env_Flask
env_Flask\Scripts\activate  # Windows

## 🛠️ Instale as dependências
pip install -r requirements.txt



## 🛠️ Estrutura Banco de dados
CREATE TABLE db_avaliacao (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    idade INT,
    sexo VARCHAR(10),
    email VARCHAR(100),
    produto VARCHAR(100),
    conforto VARCHAR(20),
    comentario TEXT
);
