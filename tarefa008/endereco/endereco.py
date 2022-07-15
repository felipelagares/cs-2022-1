from utils import TipoEndereco
from bairro import Bairro
from logradouro import Logradouro


class Endereco:
    numero: int = None
    complemento: str = None
    CEP: int = None

    def __init__(self, numero, complemento, cep,
                 logradouro: Logradouro, bairro: Bairro, tipo: TipoEndereco):
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.logradouro = logradouro
        self.bairro = bairro
        self.tipo = tipo
