class CarrinhoCompras:
    def __init__(self):
        self.produtos = []

    def inserir_produtos(self, product):
        self.produtos.append(product)

    def lista_produtos(self):
        for product in self.produtos:
            print(product.nome, product.valor)

    def soma_total(self):
        total = 0
        for product in self.produtos:
            total += product.valor
        return total


class Product:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor
        pass