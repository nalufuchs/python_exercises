c = ('\033[m',           #cor 0
       '\033[0;30;41m',  #cor  1 vermelha
       '\033[0;30;46m',  #cor 2 azul
       '\033[0;30;42m',  #cor 3 verde
        '\033[0;30;47m',    #cor 4 branco
     )


def titulo(txt, cor=0):
    tam = len(txt) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {txt}')
    print('~' * tam)
    print(c[0], end='')

def ajuda():
    titulo('SISTEMA DE AJUDA PYHELP', 3)
    while True:
        h = input('Função ou biblioteca > ').lower().strip()
        if h == 'fim':
            titulo('\033[30;41mOBRIGADO E ATÉ A PRÓXIMA!', 1)
            break
        else:
            titulo(f'Acessando o manual de comando {h}', 2)
            print(c[4], end='')
            print(help(h))
            print(c[0], end='')




print(ajuda())