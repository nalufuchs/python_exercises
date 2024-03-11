#num = input('Digite um número de 0 a 9999:  ')
#u = num // 1 % 10
#d = num // 10 % 10
#c = num // 100 % 10
#m = num // 1000 % 10
#print ('O número escolhido possui: \n {} para unidade, \n {} para dezena, \n {} para centena, \n e {} para milhar'.format(u, d, c, m))




#n = str(num)
#uni = n[3:]
#dez = n[2]
#cent = n[1]
#mil = n[0]
#print('O número escolhido possui: \n {} para unidade, \n {} para dezena, \n {} para centena \n e {} para milhar'.format( num[3], num[2], num[1], num[0]) )



#n = str(input('Digite um numero de 0 a 9999: '))
#print(f'Unidade: {n[-1 : ]}')
#print('Dezena:  {} \nCentena: {}'.format(n[-2 : -1], n[-3 : -2]))
#print('Milhar:  {}'.format(n[-4 : -3]))

#n=input('Digite um número inteiro de 0 até 9999: ')
#m=f'{n:0>4}'
#print(f'Unidade: {m[3]}\n Dezena: {m[2]}\n Centena: {m[1]}\n Milhar: {m[0]}')

n = input ('Digite um número de 0 a 9999:  ')
m = f'{n:0>4}'
print(f' A unidade do seu número é {m[3]}, \n A dezena do seu número é {m[2]}, \n A centena do seu número é {m[1]},  \n E o milhar do seu número é {m[0]}')
