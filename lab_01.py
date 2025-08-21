class ContaBancaria:
    def __init__(self, numero, titular, saldo):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo

    @property
    def titular(self):
        return self._titular
    
    @titular.setter
    def titular(self, titular):
        self._titular = titular

    
    @property
    def saldo(self):
        return self._saldo

    def sacar(self, valor):
        if valor <= self._saldo:
            self._saldo -= valor
        else:
            print('Valor inválido para o saque.')
    
    def depositar(self, valor):
        self._saldo += valor

    def __str__(self):
        return f"Conta de {self._titular}: {self._saldo}"


conta = ContaBancaria("65425", "Emerson", 500)
print(conta)

conta.depositar(10)
print(conta)

conta.sacar(10)
print(conta)

conta.depositar(10)
print(conta)

print("Fim")
