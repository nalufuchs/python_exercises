import random
a = input('Primeiro aluno a ser sorteado:  ')
b = input('Segundo aluno  a ser sorteado:  ')
c= input('Terceiro aluno a ser sorteado:   ')
d = input('Quarto aluno a ser sorteado:   ')
lista = [a, b, c, d]
r = random.choice(lista)
print('O aluno sorteado é {}'.format(r))

