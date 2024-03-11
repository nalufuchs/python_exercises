#resposta = int(input('Insira um número entre 0 e 10:  '))
extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')

#while not resposta in range (0,11):
#    print('Resposta inválida. Tente novamente')
#    resposta = int(input('Digite um número de 0 a 10:  '))
#print ('O valor digitado em sua lista, por extenso, é {}'.format((extenso[resposta])))

#outro jeito de fazer:
while True:
    num = int(input('Digite um número entre 0 e 10:  '))
    if 0 <= num <= 20:
        break
    print('Tente novamente')
print(f'Você digitou o número {num} que, por extenso, é {extenso[num]}')