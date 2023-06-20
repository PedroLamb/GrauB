from usuarios import *
from catalogo import Catalogo
from midia import *
from menus import *
import csv

catalogo_geral = Catalogo()
usuario_atual = []
perfis_atual = []

class Aplicacao:
    def __init__(self):
        self.tela = 0
        self.terminou = False
        self.carregarMidia()


    def criarUsuariosCSV(self):
        with open('./arquivos/Usuarios.csv', 'a') as criarusuarios: 
            pass 


    def executar(self):
        opcao = -1
        while not self.terminou:
            if self.tela == 0:
                self.telaInicial()

            elif self.tela == 1:
                self.telaPerfis()

            elif self.tela == 2:
                self.telaDois()



    def finalizar(self):
        print('Finalizando a aplicação...')
        input('Pressione ENTER para continuar...')

    def carregarMidia(self):
        arqMidia = open('./arquivos/catalogoGeral.csv')
        leitor = csv.reader(arqMidia, delimiter=';')
        listaMidia = list(leitor)
        arqMidia.close()
        for i in range(len(listaMidia)):
            if listaMidia[i][1] == 'Série':
                serie = Serie(listaMidia[i][0], listaMidia[i][1], listaMidia[i][2], listaMidia[i][3], listaMidia[i][4],
                            listaMidia[i][5], listaMidia[i][6])
                catalogo_geral.adicionarMidia(serie, 'Série')
            elif listaMidia[i][1] == 'Filme':
                filme = Filme(listaMidia[i][0], listaMidia[i][1], listaMidia[i][2], listaMidia[i][3], listaMidia[i][4],
                            listaMidia[i][5], listaMidia[i][7], listaMidia[i][8])
                catalogo_geral.adicionarMidia(filme, 'Filme')
            elif listaMidia[i][1] == 'Documentário':
                documentario = Documentario(listaMidia[i][0], listaMidia[i][1], listaMidia[i][2], listaMidia[i][3],
                                            listaMidia[i][4], listaMidia[i][5], listaMidia[i][9])
                catalogo_geral.adicionarMidia(documentario, 'Documentário')
            elif listaMidia[i][1] == 'Animação':
                animacao = Animacao(listaMidia[i][0], listaMidia[i][1], listaMidia[i][2], listaMidia[i][3], listaMidia[i][4],
                                    listaMidia[i][5], listaMidia[i][10])
                catalogo_geral.adicionarMidia(animacao, 'Animação')
            else:
                programadetv = ProgramaDeTV(listaMidia[i][0], listaMidia[i][1], listaMidia[i][2], listaMidia[i][3],
                                            listaMidia[i][4], listaMidia[i][5], listaMidia[i][6])
                catalogo_geral.adicionarMidia(programadetv, 'Programa de TV')



    def telaInicial(self):
        opcao = menuInicial()
        if opcao == '3':
            self.terminou = True
        elif opcao == '1':
            nome = input('Informe seu nome de usuário: ')
            senha = input('Informe sua senha: ')
            resultado = logarUsuario(nome, senha)
            if resultado is True:
                usuario_atual.append(nome)
                with open('./arquivos/perfis.csv', mode='r', newline='') as perfisArq:
                    reader = csv.reader(perfisArq, delimiter=';')
                    for row in reader:
                        if row[0] == nome:
                            perfil = Perfil(row[1], row[2])
                            perfil.lista_favoritos = row[3:13]
                            perfil.ultimos_assistidos = row[13:23]
                            perfis_atual.append(perfil)
                self.tela = 1
            else:
                print('Nome ou senha incorreto.')
                input('Pressione ENTER para retornar ao menu inicial...')
                return

        elif opcao == '2':
            novo_usuario = Usuario('', '', '', '')
            novo_usuario.cadastrarUsuario()


    def telaPerfis(self):
        os.system('cls')
        print('Olá {}!'.format(usuario_atual[0].nome))
        num = 1
        for perfil in perfis_atual:
            print('Perfil {}: {}'.format(num, perfil.nome))
            num+=1
        opcao = menuPerfis()
        if opcao == '3':
            os.system('cls')
            for perfil in perfis_atual:
                print('Perfil {}: {}'.format(num, perfil.nome))
                num+=1
            opcao = input('Selecione um perfil para editar: ')

        elif opcao == '6':
            usuario_atual.clear()
            perfis_atual.clear()
            self.tela = 0
        


def logarUsuario(nome, senha):
    with open('./arquivos/usuarios.csv', mode='r', newline='') as usuariosArq:
        reader = csv.reader(usuariosArq, delimiter=';')
        lista_usuarios = list(reader)
        for row in lista_usuarios:
            if row[1] == nome and row[2] == senha:
                usuario_login = Usuario(row[0], row[1], row[2], row[3])
                usuario_atual.append(usuario_login)
                return True
        return False