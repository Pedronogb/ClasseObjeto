class Conta_bancaria:
    def __init__(self, numero, nome, saldo, agencia):
        self.numero = numero
        self.nome = nome
        self.saldo = saldo
        self.agencia = agencia
        self.transacoes = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.transacoes.append(f"Depósito: +R${valor:.2f}")
            print(f"Depósito de R${valor:.2f} realizado com sucesso")
        else:
            print("Valor de depósito inválido!")

    def sacar(self, valor):
        if valor < 0:
            print("Valor de saque inválido!")
        elif valor > self.saldo:
            print("Saldo insuficiente")
        else:
            self.saldo -= valor
            self.transacoes.append(f"Saque: -R${valor:.2f}")
            print(f"Saque de {valor:.2f} bem sucedido")

    def ver_saldo(self):
        print(f"Saldo: R$ {self.saldo}")

conta1 = Conta_bancaria("0547320474389", "Pedro Gabriel", 0.00, 500)
conta1.depositar(300)
print(f"Saldo atual: R$ {conta1.saldo:.2f}")
print(f"Transações: ", conta1.transacoes)
print()
conta1.sacar(100)
print(f"Saldo atual: R$ {conta1.saldo:.2f}")
print(f"Transações: ", conta1.transacoes)
print()

conta1.ver_saldo()


