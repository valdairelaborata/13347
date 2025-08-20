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


conta = ContaBancaria(10, "Titular")
conta.titular = 'Titular 002'
# print(conta.saldo)
# conta.deposito(10)
# print(conta.saldo)
# conta.deposito(10)
# print(conta.saldo)
# conta.deposito(10)
# print(conta.saldo)
# conta.saque(10)
# conta.saque(100)
# print(conta.saldo)
