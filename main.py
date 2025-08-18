class Carro:
    def __init__(self, cor, placa, status, modelo):
        self.cor = cor
        self.placa = placa
        self.status = status
        self.modelo = modelo

    def ligar(self):
        self.status = "Ligado"

    def desligar(self):
        self.status = "Desligado"




meu_carro = Carro("Preta", "AKS2536", "Desligado", "Ford KA")
meu_carro.ligar()
meu_carro.desligar()

print("Fim")