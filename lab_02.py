class ContaBancaria:
    def __init__(self, saldo, titular):
        self._saldo = saldo
        self._titular = titular

    @property
    def titular(self):
        return self._titular
    
    @titular.setter
    def titular(self, titular):
        self._titular = titular
    
    @property
    def saldo(self):
        return self._saldo

    def saque(self, valor):
        if valor <= self._saldo:
            self._saldo -= valor
        else:
            print('Valor inválido para o saque.')
    
    def deposito(self, valor):
        self._saldo += valor

class ContaCorrente(ContaBancaria):
    def __init__(self, saldo, titular, limite):
        super().__init__(saldo, titular)
        self._limite = limite

    @property
    def limite(self):
        return self._limite

    def saque(self, valor):
        if valor <= self.saldo + self._limite:
            self._saldo -= valor   
        else:
            print("Saldo insuficiente")     


conta_corrente = ContaCorrente(10, 'Titular 001', 1000)

conta_corrente.saque(10)
print(conta_corrente.saldo)
conta_corrente.saque(500)
print(conta_corrente.saldo)
conta_corrente.saque(600)
print(conta_corrente.saldo)
conta_corrente.saque(500)
print(conta_corrente.saldo)
conta_corrente.saque(1)
print(conta_corrente.saldo)



print('Fim')