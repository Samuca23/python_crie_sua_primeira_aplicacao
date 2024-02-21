import os

restaurantes = []

def init() :
    print("""
    █▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
    ▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█
        """)

def opcoes() :
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def invalido() :
    print('Opção inválida!\n')
    input('Digite uma tecla para voltar ao menu')
    main()

def cadastro_restaurante() :
    os.system('cls')
    print('Cadastro de novos Restaurantes\n')
    nome = input('Informe o nome do restaurante: ')

def escolher_opcao() :
    try:
        opcao = input('Escolha um opção: ')
        opcao = int(opcao)
        if opcao == 1 :
            print('1')
        elif opcao == 2:
            print('2')
        elif opcao == 3:
            print('3')
        elif opcao == 4:
            finalizar_app()
        else:
            invalido()
    except:
        invalido()

def finalizar_app() :
    os.system('cls')
    print('Encerrando APP\n')


def main() :
    os.system('cls')
    init()
    opcoes()
    escolher_opcao()

if __name__ == '__main__' :
    main()