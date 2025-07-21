class EstoqueView:
    #responsável por exibir as informações do estoque
    def menu(self):
        print("Menu de Estoque:")
        print("1. Adicionar Produto")
        print("2. Listar Produtos")
        print("3. Atualizar Produto")
        print("4. Remover Produto")
        print("5. Ajustar Estoque")
        print("6. Sair")
    
    def mostrar_produtos(self, produto):
        print(produto)

    def mostrar_lista_produtos(self, lista):
        if lista:
            for produto in lista:
                self.mostrar_produtos(produto)
        else:
            print("Nenhum produto encontrado.")

    def mostrar_mensagem(self, mensagem):
        print(mensagem)