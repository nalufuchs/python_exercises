from datetime import datetime
from random import randint
class Pessoa:

    ano_atual = int(datetime.today().year)
#variável da classe em si, os objetos da classe terão a variável =
#métodos de classe não são alterados pelas instâncias, e sim = a todas

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
#métodos abaixos todos são métodos de INSTÂNCIAS, ou seja
#apenas para as instâncias (variáveis) criadas e individuais

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo.')
            return

        if self.falando:
            print(f'{self.nome} já está falando.')
            return

        print(f'{self.nome} está falando sobre {assunto}')
        self.falando = True


    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando.')

        print(f'{self.nome} parou de falar.')
        self.falando = False


    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo.')
            return

        if self.falando:
            print(f'{self.nome} não pode comer falando.')
            return

        print(f'{self.nome} está comendo {alimento}')
        self.comendo = True


    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return

        print(f'{self.nome} parou de comer.')
        self.comendo = False


    def get_ano_nascimento(self):
        return self.ano_atual - self.idade
    #método de instância, precisa da instância


    @classmethod  #uma função de CLASSE que retorna objeto
    def criar_por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)
    #ou seja, idade é uma variável local (não existe nas outras funções)
    #é uma função que responde à classe, e não aos atributos individuais
    #essa função cria uma pessoa de maneira geral

    @staticmethod
    def gerar_id(): #função independente, não precisa da classe nem instância
        rand = randint(1000, 1999)   #essa variável está disponível só nesse escopo
        return rand   #não pode usar self nem cls,
    #pode ser chamado pela instância ou pela classe