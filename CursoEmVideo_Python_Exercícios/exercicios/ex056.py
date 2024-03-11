soma = 0
velho = 0
contador = 0
nomevelho = 0
for g in range (1, 5):
    print(f' ====== DADOS DA {g} PESSOA ======')
    nome = input (f'Qual o nome dessa pessoa?  ')
    idade = int (input (f'Qual a idade dessa pessoa?  '))
    sexo = input (f'Qual o sexo dessa pessoa? [M / F]  ').upper().strip()
    soma = soma + idade
    media = (soma)/4
    if sexo == 'M':
        if g == 1:
            velho = idade
            nomevelho = nome
        if idade > velho:
            velho = idade
            nomevelho = nome
    if sexo == 'F' and idade > 18:
        contador = 1 + contador
print('=' *10)
if contador == 0:
    print('Não existem mulheres com idade maior que 18 anos.')
else:
    print(f'O número de mulheres que possuem mais que 18 é de {contador}')
if velho == 0:
    print('Não foram disponibilizados dados de homens para serem avaliados')
else:
    print(f'O mais velho se chama {nomevelho} e possui a idade de {velho}')
print(f'A média de idade dos 4 participantes é {media:.0f}')
