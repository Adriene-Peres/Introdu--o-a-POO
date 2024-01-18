# @property + @setter - getter e setter no modo Pythônico
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Atributos que começar com um ou dois underlines
# não devem ser usados fora da classe.

class Caneta:
    def __init__(self, cor):
        self._cor = cor
        # self.cor = cor # -> usaria o setter logo no inicio quandose chama o __init__
        self._cor_tampa = None

# pra escrever um setter deve-se ter uma property
    @property
    def cor(self):
        # print('ESTOU NO GETTER')
        return self._cor
    
    @cor.setter
    def cor(self, valor):
        # print('ESTOU NO SETTER', valor)
        # if valor == 'Rosa':
        #     raise ValueError('Não aceito essa cor')
        self._cor = valor
    
    @property
    def cor_tampa(self):
        return self._cor_tampa
    
    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor

        

caneta = Caneta('Azul')
caneta.cor = 'Rosa' # usando o setter
caneta.cor_tampa = 'Verde' # usando o setter
print(caneta.cor) # getter -> obter valor
print(caneta.cor_tampa) # getter -> obter valor