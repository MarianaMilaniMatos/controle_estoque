from model import EstoqueModel, UsuarioModel

class EstoqueController:
    def __init__(self):
        self.estoque_model = EstoqueModel() #instância do modelo de estoque
        self.usuario_model = UsuarioModel() #instância do modelo de usuário

#todos os métodos do controlador existem no modelo
    def cadastrar_produto(self, id, nome, categoria, quantidade, preco_compra, preco_venda, fornecedor):
        self.estoque_model.adicionar_produto(id, nome, categoria, quantidade, preco_compra, preco_venda, fornecedor)

    def listar_produtos(self):
        return self.estoque_model.listar_produtos()

    def remover_produto(self, indice):
        self.estoque_model.remover_produto(indice)

    def autenticar_usuario(self, usuario, senha):
        return self.usuario_model.autenticar(usuario, senha)

    def listar_estoque_baixo(self):
        return self.estoque_model.listar_estoque_baixo()
    
