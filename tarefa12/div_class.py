class Divisao:
    numerador: int = None
    denominador: int = None

    def __init__(self):
        n = input('numerador: ')
        d = input('denominador: ')
        try:
            self.numerador = float(n)
        except ValueError as e:
            print('numerador not  numeric')
            raise e
        try:
            self.denominador = float(d)
        except ValueError as e:
            print('denominador not  numeric')
            raise e
        try:
            self.resultado = self.numerador/self.denominador
            print(self.resultado)
        except ArithmeticError:
            print('divisão por 0')

