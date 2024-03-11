def leiaInt(txt):
    n = input(txt)
    while not n.isnumeric():
        print('ERRO! Digite um número inteiro!')
        return leiaInt(txt)
    return n


num = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {num}')

def leiaInt(numero):
    while True:
        num = input(numero)
        if num.isnumeric():
            return num
        print('\033[31mERRO! Digite um número inteiro válido\033[m')


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')

def leiaInt(frase):
    num = input(frase)
    while not num.isdecimal():
        print('\033[31mERRO! Digite um número inteiro.\033[m')
        num = input(frase)
    num = int(num)
    return num


n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}.')


def leiaint():
    n = str(input('Digite um numero: '))
    while not n.isnumeric():
        n = str(input('Voce nao digitou um numero. Por favor digite um numero: '))
    n = int(n)
    return n


numero = leiaint()
print(f'Voce digitou corretamente o numero: {numero}')
