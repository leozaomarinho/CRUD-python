from models.estoqueModel import EstoqueModel
from models.produtoModel import ProdutoModel
from views.estoque_view import EstoqueView

class EstoqueController:
    def __init__(self):
        self.model = EstoqueModel()
        self.view = EstoqueView()

    def iniciar(self):
        while