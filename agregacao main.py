from agregacao import *

carrinho = CarrinhoCompras()
p1 = Product('Bolu de murangu', 50)
p2 = Product('Bolu de chocolate', 60)
p3 = Product('Bolu de coco', 40)

carrinho.inserir_produtos(p1)
carrinho.inserir_produtos(p1)
carrinho.inserir_produtos(p1)
carrinho.inserir_produtos(p1)
carrinho.inserir_produtos(p1)
carrinho.inserir_produtos(p1)
carrinho.inserir_produtos(p2)
carrinho.inserir_produtos(p2)
carrinho.inserir_produtos(p2)
carrinho.inserir_produtos(p2)
carrinho.inserir_produtos(p2)
carrinho.inserir_produtos(p2)
carrinho.inserir_produtos(p3)
carrinho.inserir_produtos(p3)
carrinho.inserir_produtos(p3)
carrinho.inserir_produtos(p3)
carrinho.inserir_produtos(p3)
carrinho.inserir_produtos(p3)

carrinho.lista_produtos()

print(carrinho.soma_total())

