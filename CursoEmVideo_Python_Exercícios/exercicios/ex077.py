palavras = ('casa', 'navio', 'barco', 'elefante', 'igreja', 'luz', 'lanterna', 'ouvido', 'pacote')
vogal = ('a', 'e', 'i', 'o', 'u')

for p in palavras:
    print(f' \n Na palavra {p} temos:', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
