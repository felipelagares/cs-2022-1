from abstract_animal import Animal


class Cavalo(Animal):
    name = 'Bolinha'
    age = 5

    def __init__(self, name, age):
        super().__init__(name, age)

    @staticmethod
    def sound():
        print('relinchar')

    @staticmethod
    def correr():
        print('correr')

