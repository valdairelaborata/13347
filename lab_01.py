class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def descricao(self):
        return f'{self.marca} - {self.modelo}'


carro =  Carro("Ford", "KA")
print(carro.descricao())