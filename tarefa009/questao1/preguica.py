from abstract_animal import Animal


class Preguica(Animal):
    name = 'Felipe'
    age = 21

    def __init__(self, name, age):
        super().__init__(name, age)

    @staticmethod
    def sound():
        print('grunhir')

    @staticmethod
    def escalar():
        print('escalar')
