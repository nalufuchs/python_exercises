class Televisao:
    
    def __init__(self) -> None:
        self.ligada= False
        self.canal = 3
        self.canal_min = 1
        self.canal_max = 99
        self.volume  = 30
        self.volume_min = 0
        self.volume_max = 100

    def ligar(self):
        self.ligada = True

    def desligar(self):
        self.ligada = False

    def mudar_canal_para_cima(self):
        if not self.ligada:
            return
        
        if self.canal < self.canal_max:
            self.canal += 1
    
    def mudar_canal_para_baixo(self):
        if not self.ligada:
            return
        
        if self.canal > self.canal_min:
            self.canal -= 1

    def aumentar_volume(self):
        if not self.ligada:
            return
        if self.volume < self.volume_max:
            self.volume += 10

    def diminuir_volume(self):
        if not self.ligada:
            return
        if self.volume > self.volume_min:
            self.volume -= 10

    def __str__(self) -> str:
         return f'Televisão: {self.ligada} \n Volume: {self.volume} \n Canal: {self.canal} '

#Criando instancias

tv_sala = Televisao()
tv_quarto = Televisao()

print(tv_sala.ligada)
tv_sala.ligar()
print(tv_sala.ligada, tv_quarto.ligada)

for _ in range(3):
    tv_sala.aumentar_volume()

print('TV sala:', tv_sala)
print('TV quarto:', tv_quarto)