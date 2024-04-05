from abc import ABC, abstractmethod

class Cliente(ABC):
    def __init__(self, nome, telefone, renda_mensal):
        self.nome = nome
        self.telefone = telefone
        self._renda_mensal = renda_mensal
    
    @property
    def renda_mensal(self):
        return self._renda_mensal

    @renda_mensal.setter
    def renda_mensal(self, value):
        self._renda_mensal = value

    @abstractmethod
    def possui_cheque_especial(self):
        pass


class ClienteMulher(Cliente):
    def __init__(self, nome, telefone, renda_mensal):
        super().__init__(nome, telefone, renda_mensal)

    def possui_cheque_especial(self):
        return True


class ClienteHomem(Cliente):
    def __init__(self, nome, telefone, renda_mensal):
        super().__init__(nome, telefone, renda_mensal)

    def possui_cheque_especial(self):
        return False


class ContaCorrente:
    def __init__(self, clientes):
        self._clientes = clientes
        self._saldo = 0
        self._operacoes = []

    def deposito(self, valor):
        self._saldo += valor
        self._operacoes.append(f'Depósito: +{valor}')

    def saque(self, valor):
        if self.pode_sacar(valor):
            self._saldo -= valor
            self._operacoes.append(f'Saque: -{valor}')
            return True
        else:
            print("Saldo insuficiente.")
            return False

    def pode_sacar(self, valor):
        for cliente in self._clientes:
            if cliente.possui_cheque_especial():
                if valor > (self._saldo + cliente.renda_mensal):
                    return False
            elif valor > self._saldo:
                return False
        return True


# Exemplo de uso:

cliente1 = ClienteMulher("Maria", "123456789", 3000)
cliente2 = ClienteHomem("João", "987654321", 2000)

conta = ContaCorrente([cliente1, cliente2])

print("Saldo inicial da conta:", conta._saldo)
conta.deposito(1000)
print("Saldo após depósito de 1000:", conta._saldo)
conta.saque(500)
print("Saldo após saque de 500:", conta._saldo)