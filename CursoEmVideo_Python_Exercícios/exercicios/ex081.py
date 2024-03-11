numeros = []
cont = 0
while True:
    n = int(input('Insira um valor:  '))
    resp = str(input('Gostaria de continuar? [ S / N ]  ')).upper().strip()[0]
    numeros.append(n)
    cont = cont+1
    if resp == 'N':
        break
print(f'Foram digitados {cont} números, sendo eles: {numeros} ')
numeros.sort(reverse=True)
print(f'Os valores ordenados de forma decrescente é: {numeros}')
if 5 in numeros:
    print('Existe o número 5 e ele foi adicionado na lista')
else:
    print('Não foi adicionado o número 5 na lista')
