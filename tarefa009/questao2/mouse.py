from produto import Produto


class Mouse(Produto):
    tipo: str = None

    def __init__(self, desc):
        super().__init__(desc)
