a = int(input('Insira o primeiro número:  '))
b = int(input('Insira o segundo número:  '))
c = int(input('Insira o terceiro número:  '))
#Verificar quem  é menor
menor = b
if a<b and a<c:
    menor = a
if c<a and c<b:
    menor = c
print('O menor valor é {}'.format(menor))
#verificar quem é maior
maior = a
if b>a and b>c:
    maior = b
if c > a and c>b:
    maior = c
print('O maior valor é {}'.format(maior))
