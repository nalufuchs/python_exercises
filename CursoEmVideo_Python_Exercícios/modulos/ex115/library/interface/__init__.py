def linha(tam=42):
    return '-' * tam

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


def título(txt):
    print(linha())
    print(f'{txt.center(42)}')
    print(linha())


def menu(lista):
    título('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[35m{c}\033[m - \033[36m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[33mSua opção:  \033[m')
    return opc



