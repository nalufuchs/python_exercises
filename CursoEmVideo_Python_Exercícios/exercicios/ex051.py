print('=-=' *10)
print('Dez termos de uma P.A.')
print('=-=' *10)
t1= int(input('Primeiro termo:  '))
r = int(input('Razão:   '))
t10 = t1 +(10-1) * r
for c in range (t1,  t10 + r, r):
    print(f'{c}', end= '-> ')
print('Acabou!')