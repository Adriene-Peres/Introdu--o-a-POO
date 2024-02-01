"""Classe Conta"""

from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia: int, conta: int,
                 saldo: float = 0) -> None:
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @abstractmethod
    def sacar(self, valor: float) -> float: ...

    def depositar(self, valor: float) -> float:
        self.saldo += valor
        self.detalhes(f'(DEPOSITO R${valor:.2f}).')
        print('--')
        return self.saldo

    def detalhes(self, msg: str = '') -> None:
        print(f'O seu saldo é {self.saldo:.2f}. {msg}')

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}({class_dict})'
        return class_repr


class ContaPoupanca(Conta):
    def sacar(self, valor: float) -> float:
        if self.saldo >= valor:
            self.saldo -= valor
            self.detalhes(f'(SAQUE R${valor:.2f}).')
            print('--')
        else:
            print(f'(SAQUE NEGADO) Não é possível sacar esse valor.')
            self.detalhes()
            print('--')
        return self.saldo


class ContaCorrente(Conta):
    def __init__(self, agencia: int, conta: int, saldo: float = 0,
                 limite: float = 0):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor: float) -> float:
        if self.saldo >= valor:
            self.saldo -= valor
            self.detalhes(f'(SAQUE R${valor:.2f}).')
            print('--')
        elif valor < (self.limite+self.saldo):
            self.saldo -= valor
            self.detalhes(f'(SAQUE COM LIMITE EXTRA R${valor:.2f}).')
            print('--')
        else:
            self.detalhes(f'(SAQUE NEGADO) Não é possível sacar esse valor.')
            print('--')
        return self.saldo


# if __name__ == '__main__':
#     cc2 = ContaCorrente(1234, 3231231, 0, 250)
#     cc2.depositar(580.6)
#     cc2.sacar(600.0)
#     print(cc2)

#     cp3 = ContaPoupanca(1234, 313445654)
#     cp3.depositar(580.6)
#     cp3.sacar(1)
#     print(cp3)
