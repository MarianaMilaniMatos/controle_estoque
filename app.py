from flask import Flask, render_template, request, redirect, url_for, session, flash
from controller import EstoqueController

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'  
controller = EstoqueController()

# Rota de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        senha = request.form['senha']
        if controller.autenticar_usuario(usuario, senha):
            session['usuario'] = usuario
            return redirect(url_for('index'))
        else:
            flash('Usuário ou senha inválidos!')
    return render_template('login.html')

# Rota de logout
@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('login'))

# Rota principal
@app.route("/")
def index():
    if 'usuario' not in session:
        return redirect(url_for('login'))

    # Lista de todos os produtos
    disponiveis = controller.listar_produtos()

    # Filtra produtos com estoque baixo (quantidade < 10)
    estoque_baixo = [produto for produto in disponiveis if produto.estoque_baixo()]

    return render_template("index.html", disponiveis=disponiveis, estoque_baixo=estoque_baixo)

# Rota para adicionar produto
@app.route("/adicionar", methods=["POST"])
def adicionar():
    if 'usuario' not in session:
        return redirect(url_for('login'))

    id = request.form["id"]
    nome = request.form["nome"]
    categoria = request.form["categoria"]
    quantidade = int(request.form["quantidade"])
    preco_compra = float(request.form["preco_compra"])
    preco_venda = float(request.form["preco_venda"])
    fornecedor = request.form["fornecedor"]

    controller.cadastrar_produto(id, nome, categoria, quantidade, preco_compra, preco_venda, fornecedor)
    return redirect(url_for("index"))

# Rota para remover produto
@app.route("/remover/<int:indice>", methods=["POST"])
def remover(indice):
    if 'usuario' not in session:
        return redirect(url_for('login'))

    controller.remover_produto(indice)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
