f = str((input('Digite uma frase:   ')).strip().upper())

#print( f.count('a'))
#print(f.find('a'))
#print(f.rfind('a'))
#print(len(f))

#print("Diogo X Ana X dsas".rfind("X"))

print('A letra A aparece \033[1;33m{}\033[m vezes na frase'.format(f.count('A')))
print('A letra A aparece pela \033[1;32mprimeira\033[m vez na posição \033[1;34m{}\033[m'.format(f.find('A')+1))
print('A letra A aparece pela \033[1;31múltima \033[m vez na posição \033[1;35m{}\033[m'.format(f.rfind('A')+1))