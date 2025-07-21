from produtoModel import Produto

class EstoqueModel:
    #responsável por gerenciar o estoque de produtos
    def __init__(self):
        self.produtos = {}

    def adicionar_produto(self, id, nome, preco, quantidade):
        # Verifica se o produto já existe,caso exista não adiciona o produto
        if id in self.produtos:
            raise ValueError(f'Produto com id {id} já existe.')
        self.produtos[id]=Produto(id,nome,preco,quantidade)
        return True
    
    def listar_produtos(self):
        # Retorna uma lista de todos os produtos no estoque
        return list(self.produtos.values())
    
    def atualizar_produto(self,id,nome=None,preco=None,quantidade=None):
        # Atualiza as informações de um produto existente
        if id in self.produtos:
            p = self.produtos[id]
            if nome: p.nome = nome
            if preco: p.preco = preco
            if quantidade is not None: p.quantidade = quantidade
            return True
        return False
    
    def remover_produto(self, id):
        # Remove um produto do estoque
        if id in self.produtos:
            del self.produtos[id]
            return True
        return False
    
    def ajustar_estoque(self,id,quantidade):
        # Ajusta a quantidade de um produto no estoque
        if id in self.produtos:
            self.produtos[id].quantidade += quantidade
            return True
        return False