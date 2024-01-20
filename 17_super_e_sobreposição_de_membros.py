# super() e a sobreposição de membros - Python Orientado a Objetos
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class
# -------------------------------------------------------------------------------------

# class MinhaString(str):
#     def upper(self):
#         print('CHAMOU UPPER')
#         retorno = super().upper()
#         # retorno = super(MinhaString, self).upper()
#         return retorno

# # super() retorna temporariamente a super classe, possibilitando chamar métodos
# # permite sobreposição de um metodo da super classe

# string = MinhaString('Adriene')
# # print(string)
# print(string.upper())
# -------------------------------------------------------------------------------------

class A:
    atributo_a = 'valor_a'

    def __init__(self, atributo):
        self.atributo = atributo

    def metodo(self):
        print('A')

class B(A):
    atributo_b = 'valor_b'

    def __init__(self, atributo, outra_coisa):
        super().__init__(atributo)
        self.outra_coisa = outra_coisa

    def metodo(self):
        print('B')

class C(B):
    atributo_c = 'valor_c'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print('Eiiiiiiiiiiiiiiiiiiiiiiiiii')

    def metodo(self):
        # super(C, self).metodo() # = super().metodo() = B
        # super(B, self).metodo() # = A
        print('C')

c = C('atributo', 'outra_coisa')
print(c.atributo)
print(c.outra_coisa)
# print(c.atributo_a)
# print(c.atributo_b)
# print(c.atributo_c)
c.metodo()