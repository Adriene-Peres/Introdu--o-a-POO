# Métodos em instâncias (objetos) de classes Python
# Hard coded - É algo que foi escrito diretamente no código

class Carro:
    def __init__(self, modelo):
        self.modelo = modelo

    def acelerar(self):
        print(f'{self.modelo} está acelerando...')


fusca = Carro('Fusca')
print(fusca.modelo)
fusca.acelerar()
Carro.acelerar(fusca)

print()

celta = Carro(modelo = 'Celta')
print(celta.modelo)
celta.acelerar()
Carro.acelerar(celta)