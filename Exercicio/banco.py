"""Classe Banco"""

from pessoa import Pessoa, Cliente
from contas import Conta, ContaCorrente, ContaPoupanca


class Banco:
    def __init__(
        self,
        agencias: list[int] | None = None,
        clientes: list[Pessoa] | None = None,
        contas: list[Conta] | None = None
    ):
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []

    def _checa_agencia(self, conta: Conta):
        if conta.agencia in self.agencias:
            return True
        return False

    def _checa_conta(self, conta: Conta):
        if conta in self.contas:
            return True
        return False

    def _checa_cliente(self, cliente: Pessoa):
        if cliente in self.clientes:
            return True
        return False

    def _checa_se_conta_e_do_cliente(self, cliente, conta):
        if conta is cliente.conta:
            return True
        return False

    def autenticar(self, cliente: Pessoa, conta: Conta):
        if not self._checa_agencia(conta):
            print(f'ERRO AO AUTENTICAR (Agência não pertence ao banco.)')
            return False
        elif not self._checa_cliente(cliente):
            print(f'ERRO AO AUTENTICAR (Cliente não pertence ao banco.)')
            return False
        elif not self._checa_conta(conta):
            print(f'ERRO AO AUTENTICAR (Conta não pertence ao banco.)')
            return False
        elif not self._checa_se_conta_e_do_cliente(cliente, conta):
            print(f'ERRO AO AUTENTICAR (Conta não pertence ao cliente.)')
            return False
        else:
            return self._checa_agencia(conta) and \
                self._checa_cliente(cliente) and \
                self._checa_conta(conta) and \
                self._checa_se_conta_e_do_cliente(cliente, conta)

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}({class_dict})'
        return class_repr


# if __name__ == '__main__':
#     c1 = Cliente('Luiz', 30)
#     cc1 = ContaCorrente(111, 222, 0, 0)
#     c1.conta = cc1

#     c2 = Cliente('Adriene', 22)
#     cp1 = ContaPoupanca(112, 223, 350)
#     c2.conta = cp1

#     banco = Banco()
#     banco.clientes.extend([c1, c2])
#     banco.contas.extend([cc1, cp1])
#     banco.agencias.extend([111, 222])
#     print(banco)
#     print()

#     if banco.autenticar(c1, cc1):
#         cc1.depositar(10)
#         c1.conta.depositar(100)
#         print(c1.conta)
