def fatorial(n=1, show=False):
    """
    Calcula o Fatorial de um número.
    :param n: número a ser fatoriado
    :param show:  mostrar ou não a conta
    :return: Retorna o fatorial de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print('=', end=' ')
        f *= c
    return f


print(fatorial(5, show=True))
