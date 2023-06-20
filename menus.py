import os

def menuInicial():
    os.system('cls')
    print('''  _    _       _  __ _ _      
| |  | |     (_)/ _| (_)     
| |  | |_ __  _| |_| |___  __
| |  | | '_ \| |  _| | \ \/ /
| |__| | | | | | | | | |>  < 
 \____/|_| |_|_|_| |_|_/_/\_\ 
                              ''')
    print('1 - Acessar')
    print('2 - Cadastrar')
    print('3 - Sair')    
    item = input('Escolha uma opção: ')
    return item

def menuPerfis():
    print('1 - Alterar Assinatura')
    print('2 - Acessar Perfil')
    print('3 - Editar Perfil')
    print('4 - Adicionar Perfil')
    print('5 - Remover Perfil')
    print('6 - Voltar ao menu anterior')
    item = input('Escolha uma opção: ')
    return item

def menuLogado():
    os.system('cls')
    print('1 - Buscar por nome')
    print('2 - Últimos assistidos')
    print('3 - Favoritos')
    print('4 - Filmes')
    print('5 - Séries')
    print('6 - Documentários')
    print('7 - Animações')
    print('8 - Programas de TV')
    print('9 - Retornar ao menu anterior')
    item = input('Escolha uma opção: ')
    return item

def menuMidiaNormal():
    print('1 - Assistir')
    print('2 - Favoritar/Desfavoritar')
    print('3 - Retornar ao menu anterior')
    item = input('Escolha uma opção: ')
    return item

def menuMidiaSeriePrograma():
    print('1 - Listar Episódios')
    print('2 - Favoritar/Desfavoritar')
    print('3 - Retornar ao menu anterior')
    item = input('Escolha uma opção: ')
    return item