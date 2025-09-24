
#classe principal com atributos dos produtos
class Produto:
    def __init__(self, id, nome, categoria, quantidade, preco_compra, preco_venda, fornecedor):
        self.id = id
        self.nome = nome
        self.categoria = categoria
        self.quantidade = quantidade
        self.preco_compra = preco_compra
        self.preco_venda = preco_venda
        self.fornecedor = fornecedor

#métodos para exibir as informações dos produtos
    def descricao(self):
        return f"{self.id}- {self.nome} ({self.categoria}) - {self.quantidade} unidades - Compra: R${self.preco_compra:.2f}, Venda: R${self.preco_venda:.2f} - Fornecedor: {self.fornecedor}"

#método para verificar se o estoque está baixo (alerta para produtos com quantidade menor que 10)
    def estoque_baixo(self):
        return self.quantidade < 10

#classe para gerenciar o estoque de produtos (contém todos as funcionalidades de adicionar, listar e remover produtos)
class EstoqueModel:
    def __init__(self):
        self.produtos = [] #lista para armazenar os produtos

    def adicionar_produto(self, id, nome, categoria, quantidade, preco_compra, preco_venda, fornecedor):
        produto = Produto(id, nome, categoria, quantidade, preco_compra, preco_venda, fornecedor) #cria um novo objeto produto
        self.produtos.append(produto) #adiciona o produto à lista

    def listar_produtos(self):
        return self.produtos

    def remover_produto(self, indice):
        if 0 <= indice < len(self.produtos): #remove o produto pelo índice, se o índice for válido
            self.produtos.pop(indice)
            
    def listar_estoque_baixo(self):
        produtos = self.listar_produtos() #lista todos os produtos
        alertas = []
        for produto in produtos: #Para cada produto (linha 27, objeto criado na classe produto), na lista de produtos
            if produto.estoque_baixo(): #se o estoque estiver baixo
                alertas.append(produto) #adiciona o produto à lista de alertas
        return alertas #retorna a lista de produtos com estoque baixo
            

#classe para gerenciar autenticação de usuário
class UsuarioModel:
    def __init__(self):
        self.usuario = 'admin'
        self.senha = '1234'

    def autenticar(self, usuario, senha):
        return usuario == self.usuario and senha == self.senha #verifica se o usuário e senha estão corretos