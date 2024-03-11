print('=-' * 10)
print('CONTADOR DE P.A.')
print('=-' * 10)
t1 = int(input('Digite o primeiro termo da P.A.:  '))
razao = int(input('Digite a razão de sua P.A.:  '))
termo = t1
contador = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while contador <= total:
        print(f'{termo} -> ', end=' ' )
        termo = termo+razao
        contador = contador+1
    print('PAUSA!')
    mais = int(input('Quantos termos a mais gostaria de adicionar? Digite zero para interromper:  '))
print(f'Progressão finalizada com {total} termos')









