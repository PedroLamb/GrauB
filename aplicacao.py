from usuarios import Usuario
from catalogo import Catalogo
from midia import *
from menus import *
import csv

catalogo_geral = Catalogo()


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
                self.telaUm()

            elif self.tela == 2:
                self.telaDois()

    def telaInicial(self):
        opcao = menuInicial()
        if opcao == '0':
            self.terminou = True



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
        if opcao == '0':
            self.terminou = True
