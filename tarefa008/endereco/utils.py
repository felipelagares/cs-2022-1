from enum import Enum


class TipoEndereco(Enum):
    Comercial = 'Comercial'
    Residencial = 'Residencial'


class TipoLogradouro(Enum):
    Alameda = 'Alameda'
    Avenida = 'Avenida'
    Marginal = 'Marginal'
    Rua = 'Rua'
    Rodovia = 'Rodovia'
    Via = 'Via'
    Viela = 'Viela'
    Travessa = 'Travessa'
