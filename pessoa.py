from random import randint
from datetime import datetime


class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))
    def __init__(self, nome, idade, comendo=False, falando=False):
        self._nome = nome
        self._idade = idade
        self._comendo = comendo
        self._falando = falando

    def falar(self, assunto):
        if self._comendo is True:
            print(f'{self._nome} não pode falar comendo')
            return
        
        if self._falando is True:
            print(f'{self._nome} já está falando')
            return
        
        print(f'{self._nome} está falando sobre {assunto}')
        self._falando = True
    
    def para_falar(self):
        if not self._falando:
            print(f'{self._nome} não está falando')
            return
        
        print(f'{self._nome} parou de falar')
        self._falando = False

    def comer(self, alimento):
        if self._comendo is True:
            print(f'{self._nome} já está comendo')
            return
        
        if self._falando is True:
            print(f'{self._nome} não pode comer falando')
            return

        print(f'{self._nome} está comendo {alimento}')
        self._comendo = True
    
    def parar_comer(self):
        if not self._comendo:
            print(f'{self._nome} não está comendo')
            return
        print(f'{self._nome} parou de comer')
        self._comendo = False

    def get_idade(self, ano_nascimento):
        self._idade = (self.ano_atual - ano_nascimento)
        return self._idade

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = (cls.ano_atual - ano_nascimento)
        return cls(nome, idade)

    @staticmethod
    def gera_id():
        rand = randint(5, 500)
        rand_salt = randint(1000, 5000)
        return f'{rand}000X{rand_salt}'
