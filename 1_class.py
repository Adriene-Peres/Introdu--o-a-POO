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

class Pessoa:
    ...

p1 = Pessoa()
p1.nome = "Adriene"
p1.sobrenome = 'Peres'
print(p1.nome, p1.sobrenome)
