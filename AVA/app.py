from flask import Flask, render_template, request, redirect, url_for,jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='templates', static_folder='styles', static_url_path='/styles')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///seu_banco_de_dados.db'
db = SQLAlchemy(app)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/cadastro')
def cadastro_page():

    return render_template('cadastro.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/carrinho')
def carrinho():
    return render_template('carrinho.html')

class Usuario(db.Model):
    nome = db.Column(db.String(100))
    sobrenome = db.Column(db.String(100), unique = True)
    email = db.Column(db.String(100))
    senha = db.Column(db.String(100))
    tipo = db.Column(db.String(100))

@app.route('/salvar_dados', methods=['POST'])
def salvar_dados():
    if request.method == 'POST':
        dados = request.json

        novo_usuario = Usuario(
            nome=dados['nome'],
            sobrenome=dados['sobrenome'],
            email=dados['email'],
            senha=dados['senha'],
            tipo=dados['tipo']
        )

        db.session.add(novo_usuario)
        db.session.commit()

        return 'Dados salvos com sucesso!', 200
    else:
        return 'Método não permitido', 405

if __name__ == '__main__':
    app.run()

