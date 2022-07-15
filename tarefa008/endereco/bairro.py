from cidade import Cidade


class Bairro:
    nome: str = None

    def __init__(self, nome, cidade: Cidade):
        self.nome = nome
        self.cidade = cidade
