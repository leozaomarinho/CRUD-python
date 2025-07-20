from models.estoqueModel import EstoqueModel
from models.produtoModel import ProdutoModel
from views.estoque_view import EstoqueView

class EstoqueController:
    def __init__(self):
        self.model = EstoqueModel()
        self.view = EstoqueView()

    def iniciar(self):
        while True:
            self.view.menu()
            opcao = input("Escolha uma opção: ")
            if opcao == '1':
                id = input("ID do produto: ")
                nome = input("Nome do produto: ")
                preco = float(input("Preço do produto: "))
                quantidade = int(input("Quantidade do produto: "))
                try:
                    if self.model.adicionar_produto(id, nome, preco, quantidade):
                        self.view.mostrar_mensagem("Produto adicionado com sucesso.")
                    else:
                        self.view.mostrar_mensagem("Erro ao adicionar produto, verifique se o produto já existe.")
                except ValueError as e:
                    self.view.mostrar_mensagem(str(e))
