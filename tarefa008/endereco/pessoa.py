from datetime import datetime
from endereco import Endereco


class PessoaFisica:
    nome: str = None
    sexo: str = None
    data_nascimento: datetime = None

    def __init__(self, nome, sexo, data: datetime, endereco: Endereco):
        self.nome = nome
        self.sexo = sexo
        self.data_nascimento = data
        self.endereco = endereco
