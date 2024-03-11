import random
a1 = str(input('Nome do primeiro aluno a ser sorteado:   '))
a2 = str(input('Nome do segundo aluno a ser sorteado:   '))
a3 = str(input('Nome do terceiro aluno a ser sorteado:   '))
a4 = str(input('Nome do quarto aluno a ser sorteado:   '))
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('A ordem de apresentação será')
print (lista)


