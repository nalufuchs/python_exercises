n1 = float(input('Insira um número:  '))
n2 = float(input('Insira outro número:   '))
#print('=' * 30)
#print('O que você gostaria de realizar com esses valores? Digite: ')
#print(' [ 1 ] para somar \n [ 2 ] para subtrair \n [ 3 ] para verificar qual o maior '
#      '\n [ 4 ] para novos números \n [ 5 ] para sair do programa')
#print('=' * 25)
acao = 0
maior = 0
while acao != 5:
    print('=' *30)
    acao = int(input('O que você gostaria de realizar com esses valores? Digite: \n [ 1 ] para somar \n [ 2 ] para subtrair \n [ 3 ] para verificar qual o maior \n [ 4 ] para novos números \n [ 5 ] para sair do programa. \n R:   '))
    print ('=' *30)
    if acao == 1:
        print(f'A soma dos seus números {n1} e {n2} resulta em {n1+n2}')
    elif acao == 2:
        print(f'Seus números {n1} e {n2} subtraídos entre si, nessa ordem, se dá {n1-n2}.')
    elif acao  == 3:
        maior = n1
        if n2 > maior:
            maior = n2
        print(f'O maior número selecionado foi {maior}')
    elif acao == 4:
        n1 = float(input('Insira o novo número:   '))
        n2 = float(input('Insira o próximo número:  '))
print('Você encerrou o programa.')



