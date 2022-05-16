'''
    public
    protected
    private
    _
    __
'''

class Database:
    def __init__(self):
        self.__dados = {}

    @property
    def get_dados(self):
        return self.__dados

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)
    
    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]


db = Database()

db.inserir_cliente(1, 'João')
db.inserir_cliente(2, 'Luiz')
db.inserir_cliente(3, 'Rose')

print(db.get_dados)
