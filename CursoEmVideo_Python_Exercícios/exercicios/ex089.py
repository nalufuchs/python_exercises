#geral =[todos os alunos [nome, [notas], media]]   lista dentro de lista dentro de lista
geral = []
aluno  = []

#O professor fez:
#ficha = list()
#nome = str(input('Nome:  '))
#nota1 = float(input('Nota 1:  '))
#nota2 = float(input('Nota 2:  '))
#media = (nota1+nota2)/2
#ficha.append([nome, [nota1, nota2], media]
#repete a estrutura de if resposta in "s" else break
#para o boletim, usou enumerat:
#for i, a in enumerate(ficha)
#   print(f'{i}{a[0]}{a[2]:.1f}')
#loop dos alunos é  igual, if == 999: break
#exeto adicionou um len(ficha)-1 como condição para mostrar, sendo -1 pq o último numero n é considerado

while True:
    aluno.append(str(input('Insira o nome do aluno:  ')).title())
    aluno.append(float(input('Insira a nota da primeira avaliação:  ').replace(',', '.')))
    aluno.append(float(input('Insira o nome da segunda avaliação:  ').replace(',','.')))
    resp = str(input('Quer adicionar outro aluno? [ S / N ]  ').upper().strip()[0])
    med = f'{(aluno[1] + aluno[2])/2:.2f}'
    aluno.append(med)
    geral.append(aluno[:])
    aluno.clear()
    if resp in 'Nn':
        break
print('=-' * 16)
print(f'{"No":<5} {"Nome":<15} {"Média":<5}')
print('-' * 28)

pos = 0
for n in geral:
    print(f'{pos:<5} {geral[pos][0]:<15} {geral[pos][3]:<5}')
    pos += 1
    print('-' * 30)

while True:
    resp = int(input('Gostaria de mostrar as notas de qual aluno? (999 para interromper)  '))
    if resp == 999:
        break
    else:
        print(f'Notas de {geral[resp][0]} são {geral[resp][1:3]}')
