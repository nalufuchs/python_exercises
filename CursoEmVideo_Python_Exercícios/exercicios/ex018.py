from math import radians, sin, cos, tan
a = float(input('Digite o valor de um ângulo de um círculo (de 0 a 360º) para serem calculados seu seno, cosseno e tangente:   '))
#s = math.sin(a)
#c = math.cos(a)
#t = math.tan(a)
#print ('Se seu ângulo é {}, seu seno é {:.3f}, seu cosseno é {:.3f} e sua tangente é {:.3f}'.format(a,s,c,t))
s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))
print('Se seu ângulo é {}, seu seno é {:.2f}, seu cosseno é {:.2f} e sua tangente é {:.2f}'.format(a,s,c,t))

