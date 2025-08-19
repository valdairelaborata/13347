class ContaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0

    def depositar(self, valor) :
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor

    def dados(self):
        return f"Titular: {self.titular}, saldo:{ self.saldo}"

conta = ContaBancaria("Flávio")
conta.depositar(10)
print(conta.dados())
conta.sacar(15)
print(conta.dados())
conta.sacar(10)
print(conta.dados())

print("Fim")