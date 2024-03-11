from datetime import date
nasc = int(input('Insira o ano de nascimento do nadador:   '))
ano = date.today().year
idade = ano - nasc
print('\033[36m==\033[m'*15)
if idade <= 9:
    print('O competidor irá para a classificação \033[36mMIRIM\033[m')
elif 9 < idade <= 14:
    print('O competidor irá para a classificação \033[36mINFANTIL\033[m')
elif 14< idade <= 19:
    print('O competidor irá para a classificação \033[36mJUNIOR\033[m')
elif idade == 20:
    print('O competidor irá para a classificação \033[36mSÊNIOR\033[m')
elif idade > 20:
    print('O competidor irá para a classificação \033[36mMASTER\033[m')