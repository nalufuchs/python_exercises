h=float(input('Qual a altura da parede que deseja pintar? '))
l=float(input('Qual a largura da parede que deseja pintar? '))
a=h*l
t=a/2
print('Considerando que sua parede possui {}m x {}m e como área resultante possui {} metros quadrados, serão necessários {}  litros de tinta para pintá-la'.format(h, l, a,t))
