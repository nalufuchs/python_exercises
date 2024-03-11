frase = input('Insira uma frase e iremos detectar se é ou não um palíndromo:  ').upper().strip().replace(' ', '')
#print(frase[::-1])
if frase == (frase[::-1]):
    print('É um palíndromo')
else:
    print('Não é um palíndromo.')