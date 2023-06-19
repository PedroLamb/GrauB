from usuarios import Usuario
from catalogo import Catalogo
from midia import *
import csv

catalogo_geral = Catalogo()


class Aplicacao:
    def __init__(self):
        self.tela = 0
        self.terminou = False
        self.carregarMidia()

    def executar(self):
        opcao = -1
        while not self.terminou:
            if self.tela == 0:
                self.telaInicial()

            elif self.tela == 1:
                self.telaUm()

            elif self.tela == 2:
                self.telaDois()


    def finalizar(self):
        print('Finalizando a aplicação...')
        input('Pressione ENTER para continuar...')


    def carregarMidia(self):
        arqMidia = open('./arquivos/catalogoGeral.csv')
        leitor = csv.reader(arqMidia, delimitir = ';')
        listaMidia = list(leitor)
        arqMidia.close()

        for i in range(len(listaMidia)):
            if listaMidia[i][1] == 'Série':
                serie = (Serie(listaMidia[i][0], listaMidia[i][1], listaMidia[i][2], listaMidia[i][3], listaMidia[i][4], listaMidia[i][5], listaMidia[i][6]))
                catalogo_geral.lista_series.append(serie)


aplicacao1 = Aplicacao()

aplicacao1.carregarMidia()
print (catalogo_geral.lista_series)