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

class CarroSedan(Carro):
    def __init__(self, marca, modelo, ano, tamanho_porta_malas):
        super().__init__(marca, modelo, ano)
        self.tamanho_porta_malas = tamanho_porta_malas

    def descricao(self):
        return super().descricao() + f" Porta malas {self.tamanho_porta_malas}"         


carro = Carro("Ford", "KA", "2008")
print(carro.descricao())

esportivo = CarroEsportivo("Honda", "Civic TSI", "2008", 240)
print(esportivo.descricao())

sedan = CarroSedan("Fiat", "Sienna", 2013, 450)
print(sedan.descricao())



print("Fim")
