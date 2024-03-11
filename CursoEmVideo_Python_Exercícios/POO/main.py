from pessoa import Pessoa

p1 = Pessoa('Luiz', 29)
""""
p1.comer('maçã')
p1.comer('maçã')
p1.parar_comer()
p1.parar_comer()
p1.comer('maçã')
p1.falar('POO')
p1.parar_comer()
p1.falar('POO')
p1.comer('maçã')
p1.parar_falar()
p1.comer('maçã')
"""
#p2 = Pessoa('Marcos', 32)
#p1.falar('POO')
#p2.comer('churrasco')

""" 
#criar pessoa por instância ou por método de classe
p3 = Pessoa.criar_por_ano_nascimento("João", 1987)
print(p3)
print(p3.nome, p3.idade)
"""
 #instância estática,
print(Pessoa.gerar_id())
print(p1.gerar_id())     #funciona dos 2 jeitos,
#não tenho acesso à instância dentro do método, mas ele não precisa
