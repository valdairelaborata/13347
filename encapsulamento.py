class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.__velocidade = 0

    @property
    def velocidade(self):
        return self.__velocidade
    
    def __verifica_combustivel(self):
        print('Verificar nível de combustível')

    def acelerar(self, valor):
        self.__velocidade += valor
        self.__verifica_combustivel()


carro = Carro("Ford", "KA")
carro.acelerar(10)
carro.acelerar(10)
carro.acelerar(10)
print(carro.velocidade)
