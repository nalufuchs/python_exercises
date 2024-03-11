frase = '   Curso em Vídeo Python   '
print(frase)
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[13:])
print(frase[3:13:2])
print(frase[::2])
print(frase.count('O'))
print(frase.count('v'))
print(frase.count('V'))
print(frase.upper() .count('O'))
print(len(frase))
print(frase.__len__())
print(len(frase.strip()))
print ('Curso' in frase)
print (frase.find('Curso'))
print(frase.lower().strip().find('curso'))
print(frase.split())
dividido = frase.split()
print(dividido)
print(dividido[0])
print (dividido[2][3])




frase.replace('Vídeo', 'Android')
#('Não é salvo quando se coloca apenas assim, se quiser salvar, deve-se adicionar ao = novamente')
print(frase)
print(frase.replace('Vídeo', 'Android'))



print("""Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard'
 dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. 
 It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged""")
