from mouse import Mouse
from livro import Livro

mouse = Mouse('Mouse ótico, Saída USB. 1.600 dpi')
livro = Livro('livro de cs')

carrinho = [mouse, livro]

for item in carrinho:
    print(item.getDescricao())