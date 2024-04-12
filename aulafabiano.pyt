import os

perfume = [{'nome': 'malbec', 'marca': 'boticario', 'ativo': False}, 
           {'nome': 'humor', 'marca': 'natura', 'ativo': True},
           {'nome': 'portiolli', 'marca': 'jequiti', 'ativo': False}]

def exibirNomePrograma():
    print('PERFUME 1.0')

def exibirOpcoes():
    print('1. Cadastrar perfume')
    print('2. Listar perfumes')
    print('3. Alternar estado de um perfume')
    print('4. Sair\n')

def finalizar():
    exibirSubtitulo('Finalizar app')

def voltarMenuPrincipal():
    input('\nDigite uma tecla para voltar ao menu ')
    main()

def opcaoInvalida():
    print('Opção inválida!\n')
    voltarMenuPrincipal()

def exibirSubtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrarPerfume():
    exibirSubtitulo('Cadastro de novos perfumes')
    nomePerfume = input('Digite o nome do perfume a ser cadastrado: ')
    marca = input(f'Digite a marca do perfume {nomePerfume}: ')
    dadosPerfume = {'nome': nomePerfume, 'marca': marca, 'ativo': False}
    perfume.append(dadosPerfume)
    print(f'O perfume {nomePerfume} foi cadastrado com sucesso!')
    voltarMenuPrincipal()

def listarPerfumes():
    exibirSubtitulo('Listagem de perfumes')
    print(f'{"Nome do perfume".ljust(20)} | {"Marca".ljust(15)} | Status')
    for perfumeItem in perfume:
        nomePerfume = perfumeItem['nome']
        marca = perfumeItem['marca']
        status = 'ativado' if perfumeItem['ativo'] else 'desativado'
        print(f'- {nomePerfume.ljust(20)} | {marca.ljust(15)} | {status}')
    voltarMenuPrincipal()

def alterarPerfume():
    exibirSubtitulo('Alterar estado do perfume')
    nomePerfume = input('Digite o nome do perfume que deseja alterar o status: ')
    perfumeEncontrado = False

    for perfumeItem in perfume:
        if nomePerfume == perfumeItem['nome']:
            perfumeEncontrado = True
            perfumeItem['ativo'] = not perfumeItem['ativo']
            mensagem = f'O perfume {nomePerfume} foi ativado com sucesso' if perfumeItem['ativo'] else f'O perfume {nomePerfume} foi desativado com sucesso'
            print(mensagem)
            
    if not perfumeEncontrado:
        print('O perfume não foi encontrado')
            
    voltarMenuPrincipal()

def escolherOpcao():
    try:
        opcaoEscolhida = int(input('Escolha uma opção: '))
        if opcaoEscolhida == 1: 
            cadastrarPerfume()
        elif opcaoEscolhida == 2: 
            listarPerfumes()
        elif opcaoEscolhida == 3: 
            alterarPerfume()
        elif opcaoEscolhida == 4: 
            finalizar()
        else: 
            opcaoInvalida()
    except:
        opcaoInvalida()

def main():
    os.system('cls')
    exibirNomePrograma()
    exibirOpcoes()
    escolherOpcao()

if __name__ == '__main__':
    main()