import os

restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False}, {'nome':'Pizza Suprema', 'categoria':'Italiana', 'ativo':True}]

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

def voltar_ao_menu() :
    input('Digite uma tecla para voltar ao menu')
    main()
    
def exibir_sub_titulo(texto) :
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def invalido() :
    print('Opção inválida!\n')
    voltar_ao_menu()

def cadastro_restaurante() :
    ''' Essa função é reponsável por cadastrar um novo restaurante
    Inputs:
    - Nome do restaurante
    - Categoria

    Output:
    - Adiciona um novo restaurante a lista de restaurantes
    
    '''
    exibir_sub_titulo('Cadastro de novos Restaurantes')
    nome = input('Informe o nome do restaurante: ')
    categoria = input(f'Digite o nome da categoria do restaurante {'nome'}: ')
    dados = {'nome':nome, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados)
    print(f'O restaurante {nome} foi cadastrado com sucesso')
    voltar_ao_menu()

def listar_restaurantes() :
    exibir_sub_titulo('Listagem dos Restaurantes')

    print(f'{'Nome do restaurante'.ljust(23)} | {'Categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f' - {restaurante['nome'].ljust(20)} | {restaurante['categoria'].ljust(20)} | {ativo}')
    voltar_ao_menu()

def alterar_status_restaurante() :
    exibir_sub_titulo('Alterando estado do restaurante')
    nome = input('Digite o nome restaurante que deseja alterar: ')
    for restaurante in restaurantes :
        if nome == restaurante['nome'] :
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome} foi ativado com sucesso ' if restaurante['ativo'] else f'O restaurante {nome} foi desativado com sucesso'
            print(mensagem)
    if not restaurante :
        print('O restaurante não foi encontrado')

    voltar_ao_menu()

def escolher_opcao() :
    try:
        opcao = input('Escolha um opção: ')
        opcao = int(opcao)
        if opcao == 1 :
            cadastro_restaurante()
        elif opcao == 2:
            listar_restaurantes()
        elif opcao == 3:
            alterar_status_restaurante()
        elif opcao == 4:
            finalizar_app()
        else:
            invalido()
    except:
        invalido()

def finalizar_app() :
    exibir_sub_titulo('Encerrando APP')

def main() :
    os.system('cls')
    init()
    opcoes()
    escolher_opcao()

if __name__ == '__main__' :
    main()