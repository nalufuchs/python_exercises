from random import sample
from time import sleep

number = (sample(range(10), 1))
print('\033[33m=-=\033[m'*10)
print('\033[1mOlá, vamos brincar de adivinha?\033[m')
print ('\033[33m=-=\033[m'*10)
sleep(2)
cores = {'amarelo' : '\033[33m' , 'final' : '\033[m' , 'vermelho' : '\033[31m' , 'verde' : '\033[32m' , 'azul' : '\033[36m' }

answ = print(int(input('Estou pensando em um número de {} 0 {} a {} 10 {}. Tente adivinhar qual é:  '.format(cores['azul'], cores['final'], cores['azul'], cores['final']))))
if answ == number:
    print('{}Uau! Parece que temos um leitor de mentes! Você acertou, meus parabéns!{}'.format(cores['verde'], cores['final']))

else:
    print('{}Passou longe!{} Vou te dar uma última chance!'.format(cores['amarelo'], cores['final']))
    answ2 =  int(input('Estou pensando no {}mesmo{} número de {}0{} a {}10{}:  '.format(cores['azul'], cores['final'], cores['azul'], cores['final'], cores['azul'], cores['final'])))
    if answ2 == number:
        print('{}Dizem que na segunda tentativa é o que vale, e você acertou! Parabéns!{}'.format(cores['verde'], cores['final']))
    else:
        print('{}Você perdeu!{} Chega de chances por hoje, mas você lutou bem!'.format(cores['vermelho'], cores['final']))
print ('{} Meu número escolhido era {} {}'.format( cores['azul'], number, cores['final']))





