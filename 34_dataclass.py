# dataclasses - O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
# usuário.
# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.python.org/3/library/dataclasses.html

from dataclasses import dataclass


# as chamadas entre parentese servem para fazer alterações na estrutura da data class
# order - é possivel utilizar o metodo sorted com a dataclass sem definir a key
@dataclass(repr=True)
class Pessoa:
    nome: str
    sobrenome: str

    # deve ser escrito caso no decorator da dataclass o init esteja desativado (init=False)
    # def __init__(self, nome, sobrenome) -> None:
    #     self.nome = nome
    #     self.sobrenome = sobrenome
    #     self.nome_completo = f'{self.nome} {self.sobrenome}'

    # def __post_init__(self): # existe caso a dataclass apresente um init
    #     self.nome_completo = f'{self.nome} {self.sobrenome}'

    # @property
    # def nome_completo(self):
    #     return f'{self.nome} {self.sobrenome}'

    # @nome_completo.setter
    # def nome_completo(self, valor):
    #     nome, *sobrenome = valor.split()
    #     self.nome = nome
    #     self.sobrenome = ' '.join(sobrenome)


if __name__ == '__main__':
    # p1 = Pessoa('Adriene', 'Peres')
    # p1.nome_completo = 'José Maria Cardoso'
    # print(p1)
    # print(p1.nome_completo)

    lista = [Pessoa('A', 'Z'), Pessoa('B', 'Y'), Pessoa('C', 'X')]
    ordenadas = sorted(lista, reverse=False, key=lambda p: p.sobrenome)
    print(ordenadas)
