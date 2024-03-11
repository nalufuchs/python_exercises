from random import randint

def maior (*num):
    maior = menor = 0
    tot = 0
    for n in num:
        if tot == 0:
            maior = n
            menor = n
        else:
            if n >= maior:
                maior = n
            if n <= menor:
                menor = n
        tot += 1
    print(f'Foram analisados {tot} números, sendo eles: {num}')
    print(f'O maior valor é {maior} e o menor {menor}')


maior(1,3,5,6,8,4)
maior(3,5,7,4)
maior(3)
maior(2,1)
maior(0)
