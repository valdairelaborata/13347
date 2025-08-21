class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    # def __del__(self):
    #     print(f"Carro {self.modelo} sendo destruído")

    def __str__(self):
        return f"{self.marca} - {self.modelo} - {self.ano}"


    def __repr__(self):
        return f"Carro(marca: {self.marca}, modelo: {self.modelo})"

    def __eq__(self, outro_objeto):
        return self.marca == outro_objeto.marca and self.modelo == outro_objeto.modelo
    
    def __ne__(self, outro_objeto):
        return not self.__eq__(outro_objeto)


# del carro

# print(carro)

# print(repr(carro))  
  

carro_01 = Carro("Ford", "KA", 2008)
carro_02 = Carro("Honda", "Civic", 2012)


# sao_iguais = carro_01 == carro_02

sao_diferentes = carro_01 != carro_02

print(sao_diferentes)




print("Fim")
