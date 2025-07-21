from models.estoqueModel import EstoqueModel
from models.produtoModel import Produto
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
                print('-----------------------------')
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

            elif opcao == '2':
                print('-----------------------------')
                produtos = self.model.listar_produtos()
                self.view.mostrar_lista_produtos(produtos)

            elif opcao == '3':
                print('-----------------------------')
                id = input('ID do produto a ser atualizado: ')
                nome = input("Novo nome do produto (deixe em branco para não alterar): ")
                preco = input("Novo preço do produto (deixe em branco para não alterar): ")
                quantidade = input("Nova quantidade do produto (deixe em branco para não alterar): ")

                preco = float(preco) if preco else None
                quantidade = int(quantidade) if quantidade else None

                try:
                    if self.model.atualizar_produto(id, nome or None, preco, quantidade):
                        self.view.mostrar_mensagem("Produto atualizado com sucesso.")
                    else:
                        self.view.mostrar_mensagem("Erro ao atualizar produto, verifique se o produto existe.")
                except ValueError as e:
                    self.view.mostrar_mensagem(str(e))

            elif opcao == '4':
                print('-----------------------------')
                id = input("ID do produto a ser removido: ")
                if self.model.remover_produto(id):
                    self.view.mostrar_mensagem("Produto removido com sucesso.")
                else:
                    self.view.mostrar_mensagem("Erro ao remover produto, verifique se o produto existe.")

            elif opcao == '5':
                print('-----------------------------')
                id = input("ID do produto para ajustar estoque: ")
                quantidade = int(input("Quantidade a ajustar (use negativo para remover): "))
                if self.model.ajustar_estoque(id, quantidade):
                    self.view.mostrar_mensagem("Estoque ajustado com sucesso.")
                else:
                    self.view.mostrar_mensagem("Erro ao ajustar estoque, verifique se o produto existe.") 
            
            elif opcao == '6':
                print('-----------------------------')
                self.view.mostrar_mensagem("Saindo do sistema.")
                break
            else:
                self.view.mostrar_mensagem("Opção inválida, tente novamente.")