class Catalogo:
    def __init__(self):
        self.lista_series = []
        self.lista_filmes = []
        self.lista_documentarios = []
        self.lista_animacoes = []
        self.lista_programasdetv = []

    def adicionarMidia(self, midia, tipo):
        if tipo == 'Série':
            self.lista_series.append(midia)
        elif tipo == 'Filme':
            self.lista_filmes.append(midia)
        elif tipo == 'Documentário':
            self.lista_documentarios.append(midia)
        elif tipo == 'Animação':
            self.lista_animacoes.append(midia)
        elif tipo == 'Programa de TV':
            self.lista_programasdetv.append(midia)
        else:
            print('Tipo de mídia inválido.')

    def obterLista(self, tipo):
        if tipo == 'Série':
            return self.lista_series
        elif tipo == 'Filme':
            return self.lista_filmes
        elif tipo == 'Documentário':
            return self.lista_documentarios
        elif tipo == 'Animação':
            return self.lista_animacoes
        elif tipo == 'Programa de TV':
            return self.lista_programasdetv
        else:
            print('Tipo de mídia inválido.')
        