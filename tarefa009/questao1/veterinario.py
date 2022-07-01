from abstract_animal import Animal


class Veterinario(Animal):
    name = 'Gilmar'
    age = 30

    def __init__(self, name, age):
        super().__init__(name, age)

    @staticmethod
    def sound():
        print('falar')

    @staticmethod
    def correr():
        print('correr')

    @staticmethod
    def examinar(animal: Animal):
        animal.sound()
