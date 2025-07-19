from produtoModel import Produto

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
    
    def atualizar_produto(self,id,nome=None,preco=None,quantidade=None):
        if id in self.produtos:
            p = self.produtos[id]
            if nome: p.nome = nome
            if preco: p.preco = preco
            if quantidade is not None: p.quantidade = quantidade
            return True
        return False
    
    def remover_produto(self, id):
        if id in self.produtos:
            del self.produtos[id]
            return True
        return False
    
    def ajustar_estoque(self,id,quantidade):
        if id in self.produtos:
            self.produtos[id].quantidade += quantidade
            return True
        return False