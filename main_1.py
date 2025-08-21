class Numero:
    def __init__(self, valor):
        self.valor = valor


    def __add__(self, outro_objeto):
        novo_valor = self.valor + outro_objeto.valor
        return Numero(novo_valor)
    

numero_1 = Numero(5)        
numero_2 = Numero(10)

# resultado = numero_1 + numero_2

print("Fim")

