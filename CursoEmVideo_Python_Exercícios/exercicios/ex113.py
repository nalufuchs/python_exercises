#refazer o desafio 103 mas com trataemnto de erros

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError,TypeError):
            print('\033[0;31mERRO! Por favor, digite um  número válido.\033[m')
        except KeyboardInterrupt:
            print('\033[0;36mO operador decidiu não informar mais dados.\033[m')
            return 0
        else:
            return n

def leiaFloat(txt):
    while True:
        try:
            n = float(input(txt))
        except (ValueError, TypeError):
            print('\033[31mERRO! O valor digitado não é um número real válido\033[m')
        except KeyboardInterrupt:
            print('\033[36mO usuário decidiu por interromper o programa.\033[m')
            return 0
        else:
            return n





num = leiaInt('Insira um valor:  ')
n2 = leiaFloat('Digite um número real:  ')
print(f'Os valores digitado foram {num} e {n2}')





