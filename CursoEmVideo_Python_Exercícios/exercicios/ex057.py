sexo = input('Insira seu sexo [M/F]:  ').upper().strip()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo [ M / F]:   ').strip().upper()[0])
print(f'Sexo {sexo} registrado com sucesso.')

