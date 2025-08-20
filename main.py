class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def descricao(self):
        return f"{self.marca} {self.modelo} {self.ano}"

class CarroEsportivo(Carro):
    def __init__(self, marca, modelo, ano, velcidade_maxima):
        super().__init__(marca, modelo, ano)
        self.velcidade_maxima = velcidade_maxima


    def descricao(self):
        return super().descricao() + f" {self.velcidade_maxima}"



carro = Carro("Ford", "KA", "2008")
print(carro.descricao())

esportivo = CarroEsportivo("Honda", "Civic TSI", "2008", 240)
print(esportivo.descricao())



print("Fim")
