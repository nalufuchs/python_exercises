name = str(input ('Insira seu nome completo:  '))
div = name.split()
print('Seu primeiro nome é \033[36m{}\033[m'.format(div[0]))
#print('Seu último nome é {}'.format(div[-1]))
print('Seu último nome é \033[33m{}\033[m'.format(div[len(div)-1]))
#a funcao pede o nome (div) na função len-div (ou seja, quantos nomes teria, ai mostra o numero máximo, portanto o numero máximo = sobrenome final, e -1 pq o python conta de 0 em diante, e não de 1 em diante. Ou seja, o 3 na real é o 2

