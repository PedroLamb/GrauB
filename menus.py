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