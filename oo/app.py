from model.restaurante import Restaurante
from model.cardapio.bebida import Bebida
from model.cardapio.prato import Prato

restaurante_1 = Restaurante('Praça', 'Gourmet')
bebida = Bebida('Suco de Menlancia', 5.0, 'grande')
bebida.aplicar_desconto()
prato = Prato('Pãozinho', 4.0, 'O melhor pão da cidade')
prato.aplicar_desconto()
restaurante_1.adicionar_no_cadarpio(bebida)
restaurante_1.adicionar_no_cadarpio(prato)

def main() :
    restaurante_1.exibir_cardapio

if __name__ == '__main__' :
    main()