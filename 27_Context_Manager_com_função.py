# Context Manager com fução - Criando e usando gerenciamento de contexto

from contextlib import contextmanager

@contextmanager
def my_open(caminho_arquivo, modo):
    try:
        print('ABRINDO ARQUIVO')
        arquivo = open(caminho_arquivo, modo, encoding='utf8')
        yield arquivo
    # except Exception as e:
    #     print('Ocorreu erro', e)
    finally:
        print('FECHANDO ARQUIVO')
        arquivo.close()

with my_open('Context_Manager_com_função.txt', 'w') as arquivo:
    arquivo.write('linha 1\n')
    arquivo.write('linha 2\n', 123)
    arquivo.write('linha 3\n')
    print('WITH', arquivo)
