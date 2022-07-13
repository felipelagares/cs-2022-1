class Vetor:
    def __init__(self):
        self.vet = []
        self.cont = 0
        while True:
            try:
                n = int(input('numero: '))
                self.vet.append(n)
            except ValueError as e:
                print('not  integer')
                break

            # python nao possui um tamanho limite definivel para os arrays
            self.cont += 1
            if self.cont > 10:
                print('len(vetor) > 10')
                break
            if n == 0:
                break
