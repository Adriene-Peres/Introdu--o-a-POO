# Escopo da classe e de métodos da classe

class Animal:
    # nome = 'Leão' ---> (fora da classe) print(Animal.nome)
    def __init__(self,nome):
        self.nome = nome
    
    def comendo(self, alimento):
        return f'{self.nome} está comendo {alimento}'
    
    def executar(self, *args, **kwargs):
        return self.comendo(*args, **kwargs)


leao = Animal(nome='Leão')
print(leao.nome)
print(leao.executar('carne'))