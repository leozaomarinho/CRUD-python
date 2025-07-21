from controllers.estoque_controller import EstoqueController
from models.estoqueModel import EstoqueModel
from views.estoque_view import EstoqueView

if __name__ == "__main__":
    controller = EstoqueController()
    controller.iniciar()