num = list()

while True:
    n = int(input('Digite um número:  '))
    if n not in num:
        num.append(n)
        print('Adicionado com sucesso!')
    else:
        print('Valor duplicado! Não será considerado!')
    resp = str(input('Gostaria de continuar? [ S / N ]  ').upper().strip()[0])
    if resp == 'N':
        break
num.sort()
print(f'Você adicionou os valores {num}')