n = 0
#for n in range (0, 51):
#    print('.', end=' ')
#    if n % 2 == 0 and n != 0:
#        print (n, end= ', ')
#gasta muita memória do computador, pois, ao rodar, ele tem que fazer vários laços até contar.

for n in range (0, 51, 2):
#    print('.', end=' ')
    if n % 2 == 0:
        print(n, end= ', ')