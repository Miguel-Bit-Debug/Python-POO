from pydoc import cli
from composicao import *

cliente = Cliente('miguel', 21)

cliente.insere_endereco('sp', 'sp')

cliente.lista_enderecos()