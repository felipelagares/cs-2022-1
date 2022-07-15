from utils import TipoLogradouro


class Logradouro:
    nome: str = None
    tipo: TipoLogradouro = None

    def __init__(self, nome, tipo: TipoLogradouro):
        self.nome = nome
        self.tipo = tipo