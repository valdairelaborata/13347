class Calculadora:
    def __init__(self, valor_inicial):
        self.resultado = valor_inicial

    def adicao(self, a):
        self.resultado = self.resultado + a
        return self.resultado   

    def subtracao(self, a):
        self.resultado = self.resultado - a
        return self.resultado 
    
    def multiplicacao(self, a):
        self.resultado = self.resultado * a
        return self.resultado 
    
    def divisao(self, a):
        self.resultado = self.resultado / a
        return self.resultado  



calculadora = Calculadora(10)   
print(calculadora.adicao(5))
print(calculadora.divisao(3))
print(calculadora.multiplicacao(5))
print(calculadora.subtracao(20))