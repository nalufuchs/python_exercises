n = int(input('Escolha um número para realizarmos sua tabuada do 1 ao 10:  '))
print('=-=' * 4)
print ('A tabuada é:')
for c in range (1, 11):
    print(f'{c} x {n} = {n*c}')
print('=-=' * 4)