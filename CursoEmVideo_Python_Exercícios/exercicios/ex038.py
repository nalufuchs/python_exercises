a = int(input('Digite um número inteiro:  '))
print('  ' * 10)
b = int(input('Digite outro número inteiro:  '))
print ('  ' * 10)
if a > b:
    print('\033[36m O primeiro valor é maior')
elif a < b:
    print('\033[36m O segundo valor é maior')
else:
    print('\033[36m Não existe valor maior, pois os números são iguais')