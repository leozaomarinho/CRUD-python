from produto import Produto

class Estoque:
    def __init__(self):
        self.produtos = {}

    def adicionar_produto(self, id, nome, preco, quantidade):
        if id in self.produtos:
            raise ValueError(f'Produto com id {id} já existe.')
        self.produtos[id]=Produto(id,nome,preco,quantidade)
        return True
    
    def listar_produtos(self):
        return list(self.produtos.values())
    
