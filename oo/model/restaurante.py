class Restaurante:
    
    restaurantes = []

    def __init__(self, _nome, categoria) :
        self._nome = _nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self) :
        return f'{self._nome} | {self.categoria}'
    
    @classmethod
    def listar_restaurantes(cls) :
        print(f'{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante._ativo}')

    @property
    def ativo(self) :
        return 'Ativo' if self._ativo else 'Inativo'
    
    def alterar_status(self) :
        self._ativo = not self._ativo

restaurante1 = Restaurante('Praça', 'Gourmet')
restaurante1.alterar_status()
restaurante2 = Restaurante('Centro', 'Gourmet')
restaurante3 = Restaurante('Taboão', 'Lanches')
restaurante4 = Restaurante('Bremer', 'Almoço')

Restaurante.listar_restaurantes()