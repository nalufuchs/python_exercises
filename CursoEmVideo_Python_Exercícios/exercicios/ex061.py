print('=-=' *10)
print('Dez termos de uma P.A.')
print('=-=' *10)
t1= int(input('Primeiro termo:  '))
r = int(input('Razão:   '))
termo = t1
contador = 1
#t10 = t1 +(10-1) * r
while contador <= 10:
    print(f'{termo} -> ', end= ' ')
    termo = termo + r
    contador += 1
print('FIM!')


