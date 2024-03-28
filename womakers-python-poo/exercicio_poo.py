#Crie uma classe que modele o objeto "carro".

class Carro:
#Um carro tem os seguintes atributos: ligado, cor, modelo, velocidade.
    def __init__(self) -> None:
        self.cor = 'prata'
        self.modelo = 'gol'
        self.velocidade = 0
        self.ligado = False
        self.velocidade_max = 200
        self.velocidade_min = 0

#Um carro tem os seguintes comportamentos: liga, desliga, acelera, desacelera.
    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

    def acelerar(self):
        if not self.ligado:
            return
        if self.velocidade < self.velocidade_max:
             self.velocidade += 10
        
    def desacelerar(self):
        if not self.ligado:
            return
        if self.velocidade > self.velocidade_min:
            self.velocidade -= 10

    def __str__(self) -> str:
        return f' carro {self.modelo} - ligado {self.ligado} - velocidade {self.velocidade}'


#Faça o carro "andar" utilizando os métodos da sua classe.
carro1 = Carro()
carro1.ligar()
print(carro1)
for _ in range (5):
    carro1.acelerar()
print(carro1)

#Faça o carro "parar" utilizando os métodos da sua classe
for _ in range (5):
    carro1.desacelerar()

carro1.desligar()
print(carro1)

