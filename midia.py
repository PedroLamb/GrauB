class Midia:
    def __init__(self, id, tipo, titulo, genero, ano_lancamento, classificacao) -> None:
        self.id = id
        self.tipo = tipo
        self.titulo = titulo
        self.genero = genero
        self.ano_lancamento = ano_lancamento
        self.classificacao = classificacao

    def exibirInformacoes(self) -> str:
        print('''ID: {}
        Tipo: {}
        Título: {}
        Gênero: {}
        Ano de Lançamento: {}
        Classificação: {}'''.format(self.id, self.tipo, self.titulo, self.genero, self.ano_lancamento, self.classificacao))


class Serie(Midia):
    def __init__(self, id, tipo, titulo, genero, ano_lancamento, classificacao, temporadas) -> None:
        super().__init__(id, tipo, titulo, genero, ano_lancamento, classificacao)
        self.temporadas = temporadas
        self.lista_episodios = []

    def exibirInformacoes(self) -> str:
        super().exibirInformacoes()
        print('''Número de temporadas: {}'''.format(self.temporadas))    

    def listarEpisodios(self):
        pass


class Filme(Midia):
    def __init__(self, id, tipo, titulo, genero, ano_lancamento, classificacao, diretor, produtor) -> None:
        super().__init__(id, tipo, titulo, genero, ano_lancamento, classificacao)
        self.diretor = diretor
        self.produtor = produtor

    def exibirInformacoes(self) -> str:
        super().exibirInformacoes()
        print('''Diretor: {}
        Produtor: {}'''.format(self.diretor, self.produtor))



class Documentario(Midia):
    def __init__(self, id, tipo, titulo, genero, ano_lancamento, classificacao, tema) -> None:
        super().__init__(id, tipo, titulo, genero, ano_lancamento, classificacao)
        self.tema = tema

    def exibirInformacoes(self) -> str:
        super().exibirInformacoes()
        print('Tema: {}'.format(self.tema))



class Animacao(Midia):
    def __init__(self, id, tipo, titulo, genero, ano_lancamento, classificacao, estudio) -> None:
        super().__init__(id, tipo, titulo, genero, ano_lancamento, classificacao)
        self.estudio = estudio

    def exibirInformacoes(self) -> str:
        super().exibirInformacoes()
        print('Estúdio: {}'.format(self.estudio))



class ProgramaDeTV(Midia):
    def __init__(self, id, tipo, titulo, genero, ano_lancamento, classificacao, nro_episodios) -> None:
        super().__init__(id, tipo, titulo, genero, ano_lancamento, classificacao)
        self.nro_episodios = nro_episodios
        self.lista_episodios = []

    def exibirInformacoes(self) -> str:
        super().exibirInformacoes()
        print('Número de episódios: {}'.format(self.nro_episodios))

    def listarEpisodios(self):
        pass