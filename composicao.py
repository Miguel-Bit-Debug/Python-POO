class Cliente:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade
        self.__enderecos = []

    
    @property
    def nome(self):
        return self.__nome
    
    @property 
    def idade(self):
        return self.__idade

    @property
    def enderecos(self):
        return self.__enderecos


    def insere_endereco(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado))

    def lista_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)


class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado