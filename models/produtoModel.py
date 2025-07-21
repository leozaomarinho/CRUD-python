class Produto:
    #entidade que representa um produto
    def __init__(self,id,nome,preco,quantidade):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def __str__(self):
        return f'Produto(id={self.id}, nome="{self.nome}", preco={self.preco}, quantidade={self.quantidade})'