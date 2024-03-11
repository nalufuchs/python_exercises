maior = 0
menor = 0
for p in range (1,6):
    peso = float(input(f'Peso da {p}a pessoa:  ').replace(',', '.'))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print(f'O maior peso lido foi {maior} kg e o menor foi {menor} kg')



