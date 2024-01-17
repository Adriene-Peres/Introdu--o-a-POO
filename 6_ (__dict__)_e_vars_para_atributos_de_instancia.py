# __dict__ e vars para atributos de instância
# mantém os valores que podem ser escritos em um objeto

class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade


# dados = {'nome': 'João', 'idade': 35}
# p1 = Pessoa(**dados)

p1 = Pessoa('João', 35)
print(p1.__dict__) # printa os valores das instâncias em um dicionario 
# __dict__ não é so para leitura. Pode-se tambem adicionar outras chaves/valor ao dicionario
# ex.: p1.__dict__['outra'] = 'coisa' ----> adiciona outra chave no objeto p1
#      p1.__dict__['nome'] = 'EITA' ----> muda o valor da chave nome no objeto p1
#      del p1.__dict__['nome']  ----> deleta a chave nome no objeto p1

print(vars(p1)) # função para mostrar o __dict__ de um objeto  
