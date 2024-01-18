# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela


class Carro:
    def __init__(self, nome):
        self. nome = nome
        self._motor = None
        self._fabricante = None
    
    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor


class Motor:
    def __init__(self, nome):
        self.nome = nome
    

class Fabricante:
    def __init__(self, nome):
        self.nome = nome

fusca = Carro('Fusca')
motor_1_0 = Motor('1.0')
volksvagen = Fabricante('Volksvagen')

fusca.motor = motor_1_0
fusca.fabricante = volksvagen
print(fusca.nome, fusca.motor.nome, fusca.fabricante.nome)


fiat_uno = Carro('Uno')
fiat = Fabricante('Fiat')
fiat_uno.motor = motor_1_0
fiat_uno.fabricante = fiat
print(fiat_uno.nome, fiat_uno.motor.nome, fiat_uno.fabricante.nome)

focus = Carro('Focus')
ford = Fabricante('Ford')
motor_2_0 = Motor('2.0')
focus.motor = motor_2_0
focus.fabricante = ford
print(focus.nome, focus.motor.nome, focus.fabricante.nome)