"""Este é um módulo de exemplo 

Este módulo contém funções e exemplos de documentação de funções.
A função soma já é bastante conhecida.
"""

variavel_1 = 1

class Foo:
    """Este é uma classe de exemplo 

    Esta classe contém funções e exemplos de documentação de funções.
    A função soma já é bastante conhecida.
    """
    def soma(self, x: int | float, y: int | float) -> int | float:
        """Soma x e y

        :param x: número 1
        :type x: int or float
        :param y: número 2
        :type y: int or float

        :return: A soma entre x e y
        :rtype: int or float
        """
        return x + y

    def multiplica(
        self,
        x: int | float, 
        y: int | float,
        z: int | float | None = None
        ) -> int | float:
        """Multiplica x, y e/ou z

        Multiplica x e y. Se z for enviado, multiplica x, y, z.
        """
        if z is None:
            return x*y
        return x*y*z

    def bar(self) -> int:
        """O que ele faz
        
        :raises NotImplementedError: Se o método não for definido
        """
        raise NotImplementedError('teste')

variavel_2 = 2
variavel_3 = 3
variavel_4 = 4

