from estado import Estado


class Cidade:
    nome: str = None
    estado: Estado = None

    def __init__(self, nome, estado: Estado):
        self.nome = nome
        self.estado = estado
