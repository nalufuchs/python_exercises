def voto(n):
    from datetime import date
    i = date.today().year - n
    if 65 >= i >= 18:
        print(f'{i} anos. O voto é OBRIGATÓRIO!')
    elif i > 65 or 16 <= i < 18:
        print(f'{i} anos. O voto é OPCIONAL!')
    else:
        print(f'{i} anos. O voto foi NEGADO!')


voto(int(input('Em que ano você nasceu?  ')))