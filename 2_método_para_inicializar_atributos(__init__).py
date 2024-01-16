# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.

# string = 'Adriene' #str
# print(string.upper())
# print(isinstance(string, str))

# -------------------------------------------------------------------
# o primerio parâmetro de um método que trata de uma instância
# (objeto que se está gerando) deve ser 'self'. O python passa isso automaticamete.
# Ouseja, não é necessário passa-lo na chamada da função.

class Pessoa:
    def __init__(self, nome, sobrenome): # inicializar atributos
        self.nome = nome
        self.sobrenome = sobrenome

# p1 = Pessoa()
# p1.nome = "Adriene"
# p1.sobrenome = 'Peres'
# print(p1.nome, p1.sobrenome)

p1 = Pessoa('Adriene', 'Peres')
p2 = Pessoa('Maria', 'Joana')


print(p1.nome, p1.sobrenome)
print(p2.nome, p2.sobrenome)