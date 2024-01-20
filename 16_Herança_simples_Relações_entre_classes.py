# Herança simples - Relações entre classes
# Associação - usa, Agregação - tem
# Composição - É dono de, Herança - É um
#
# Herança vs Composição
#
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class
# object - todas as classes herdam de object

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome 
        self.sobrenome = sobrenome

    def falar_nome_classe(self):
        print(self.nome, self.sobrenome, self.__class__.__name__) # pega o nome da classe

class Cliente(Pessoa): # cliente herda de pessoa
    ...

class Aluno(Pessoa): # aluno herda de pessoa
    ...


c1 = Cliente('Adriene', 'Peres')
c1.falar_nome_classe()
a1 = Aluno('Maria','Helena')
a1.falar_nome_classe()

