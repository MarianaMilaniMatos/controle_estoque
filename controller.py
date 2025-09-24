from model import EstoqueModel, UsuarioModel
class EstoqueController:
    def __init__(self):
        self.estoque_model = EstoqueModel()
        self.usuario_model = UsuarioModel()

    def cadastrar_produto(self, id, nome, categoria, quantidade, preco_compra, preco_venda, fornecedor):
        self.estoque_model.adicionar_produto(id, nome, categoria, quantidade, preco_compra, preco_venda, fornecedor)

    def listar_produtos(self):
        return self.estoque_model.listar_produtos()

    def remover_produto(self, indice):
        self.estoque_model.remover_produto(indice)

    def autenticar_usuario(self, usuario, senha):
        return self.usuario_model.autenticar(usuario, senha)

    # Novo método para filtrar produtos com estoque baixo
    def listar_estoque_baixo(self):
        produtos = self.listar_produtos()
        alertas = [produto for produto in produtos if produto.estoque_baixo()]
        return alertas
