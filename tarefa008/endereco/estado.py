from pais import Pais


class Estado:
    sigla: str = None
    nome: str = None
    pais: Pais = None

    def __init__(self, sigla, nome, pais: Pais):
        self.sigla = sigla
        self.nome = nome
        self.pais = pais
