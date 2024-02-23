from model.restaurante import Restaurante

restaurante_1 = Restaurante('Praça', 'Gourmet')
restaurante_1.receber_avaliacao('Gui', 10)
restaurante_1.receber_avaliacao('Laís', 8)
restaurante_1.receber_avaliacao('Emy', 9)
# restaurante_2 = Restaurante('Mexican Food', 'Mexicana')
# restaurante_2.alterar_status()
# restaurante_3 = Restaurante('Japones', 'Japonesa')
# restaurante_4 = Restaurante('Pastelaria', 'Pastel')

def main() :
    Restaurante.listar_restaurantes()

if __name__ == '__main__' :
    main()