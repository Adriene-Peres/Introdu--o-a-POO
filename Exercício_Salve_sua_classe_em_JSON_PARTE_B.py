# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.


# Parte B - recuberando dados

import json
from Exercício_Salve_sua_classe_em_JSON_PARTE_A import CAMINHO_ARQUIVO, Pessoa, fazer_dump

# fazer_dump()

with open(CAMINHO_ARQUIVO, 'r', encoding='utf8') as arquivo:
    pessoas = json.load(arquivo)
    p1 = Pessoa(**pessoas[0])
    p2 = Pessoa(**pessoas[1])
    p3 = Pessoa(**pessoas[2])

print(p1.nome, p1. sobrenome, p1.idade)
print(p2.nome, p2.sobrenome, p2.idade)
print(p3.nome, p3.sobrenome, p3.idade)
