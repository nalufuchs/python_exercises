def escreva(txt):
#    print('~' * len(txt))
#    print(txt.title())
#    print('~' * len(txt))
#ou versao do professor:
    tam = len(txt) + 4
    print('~' * tam)
    print(f'  {txt}')
    print('~' * tam)


#programa principal
escreva(str(input('Insira algo: ')))