"""classe Pessoa/Cliente"""

from contas import Conta, ContaCorrente, ContaPoupanca


class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome: str):
        self._nome = nome

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade: int):
        self._idade = idade

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        class_dict = f'{self.nome!r}, {self.idade!r}'
        class_repr = f'{class_name}({class_dict})'
        return class_repr


class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int) -> None:
        super().__init__(nome, idade)
        self.conta: Conta | None = None


# if __name__ == '__main__':
#     c1 = Cliente('Luiz', 30)
#     c1.conta = ContaCorrente(111, 222, 0, 0)
#     print(c1)
#     print(c1.conta)

#     c2 = Cliente('Adriene', 22)
#     c2.conta = ContaPoupanca(111, 333, 350)
#     print(c2)
#     print(c2.conta)
