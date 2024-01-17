# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

# Parte A - salvando dados
import json

CAMINHO_ARQUIVO = 'Exercício_Salve_sua_classe_em_JSON.json'

class Pessoa:
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
    
p1 = Pessoa('Adriene', 'Peres', 22)
p2 = Pessoa("José", 'Santos', 34)
p3 = Pessoa("Maria", 'Silva', 24)

dados = [vars(p1), p2.__dict__, vars(p3)]

def fazer_dump():
    with open(CAMINHO_ARQUIVO, 'w', encoding='utf8') as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    fazer_dump()