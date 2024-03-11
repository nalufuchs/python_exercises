num = int(input('Digite um número:  '))
opcao = int(input('''Para converter esse valor em outra linguagem, selecione: 
                  [ 1 ] para binário
                  [ 2 ] para hexadecimal 
                  [ 3 ] para octal
                     '''))
if opcao == 1:
    print('O número {} em binário foi convertido para {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('O número {} em hexadecimal foi convertido para {}'.format(num, hex(num)[2:]))
elif opcao == 3:
    print('O número {} em octal foi convertido para {}'.format(num, oct(num)[2:]))
else:
    print ('Opção inválida, tente novamente')


