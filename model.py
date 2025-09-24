
class Produto:
    def __init__(self, id, nome, categoria, quantidade, preco_compra, preco_venda, fornecedor):
        self.id = id
        self.nome = nome
        self.categoria = categoria
        self.quantidade = quantidade
        self.preco_compra = preco_compra
        self.preco_venda = preco_venda
        self.fornecedor = fornecedor

    def descricao(self):
        return f"{self.id}- {self.nome} ({self.categoria}) - {self.quantidade} unidades - Compra: R${self.preco_compra:.2f}, Venda: R${self.preco_venda:.2f} - Fornecedor: {self.fornecedor}"

class EstoqueModel:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, id, nome, categoria, quantidade, preco_compra, preco_venda, fornecedor):
        produto = Produto(id, nome, categoria, quantidade, preco_compra, preco_venda, fornecedor)
        self.produtos.append(produto)

    def listar_produtos(self):
        return self.produtos

    def remover_produto(self, indice):
        if 0 <= indice < len(self.produtos):
            self.produtos.pop(indice)

class UsuarioModel:
    def __init__(self):
        self.usuario = 'admin'
        self.senha = '1234'

    def autenticar(self, usuario, senha):
        return usuario == self.usuario and senha == self.senha