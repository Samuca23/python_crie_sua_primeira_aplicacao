from model.avaliacao import Avaliacao
from model.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    
    restaurantes = []

    def __init__(self, _nome, categoria) :
        self._nome = _nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)

    def __str__(self) :
        return f'{self._nome} | {self.categoria}'
    
    @classmethod
    def listar_restaurantes(cls) :
        print(f'{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante._ativo}')

    @property
    def ativo(self) :
        return 'Ativo' if self._ativo else 'Inativo'
    
    def alterar_status(self) :
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota) :
        if 0 < nota <=5 :
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self) :
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)

        return round(soma_das_notas / quantidade_de_notas, 1)

    def adicionar_no_cadarpio(self, item) :
        if isinstance(item, ItemCardapio) :
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self) :
        print(f'Cardapio do Restaurando {self._nome}\n')
        for i, item in enumerate(self._cardapio, start=1) :
            if hasattr(item, 'descricao'):
                print (f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Descrição: {item.descricao}')
            else :
                print (f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Descrição: {item.tamanho}')

            