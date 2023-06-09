from usuarios import *
from catalogo import Catalogo
from midia import *
from menus import *
import csv

catalogo_geral = Catalogo()
usuario_atual = []
perfis_atual = []
perfil_acessado = []
midia_acessada = []
episodios = []
novo_favorito = []
novo_ultimo = []


class Aplicacao:
    def __init__(self):
        self.tela = 0
        self.terminou = False
        self.carregarMidia()
        self.carregarEpisodios()
        self.distribuirEpisodios()


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
                self.telaLogado()

            elif self.tela == 3:
                self.telaMidia()



    def finalizar(self):
        print('Finalizando a aplicação...')
        input('Pressione ENTER para continuar...')

    def carregarMidia(self):
        arqMidia = open('./arquivos/catalogoGeral.csv')
        leitor = csv.reader(arqMidia, delimiter=';')
        listaMidia = list(leitor)
        arqMidia.close()
        for i in range(len(listaMidia)):
            if listaMidia[i][1] == 'Serie':
                serie = Serie(listaMidia[i][0], listaMidia[i][1], listaMidia[i][2], listaMidia[i][3], listaMidia[i][4],
                            listaMidia[i][5], listaMidia[i][6])
                catalogo_geral.adicionarMidia(serie, 'Série')
            elif listaMidia[i][1] == 'Filme':
                filme = Filme(listaMidia[i][0], listaMidia[i][1], listaMidia[i][2], listaMidia[i][3], listaMidia[i][4],
                            listaMidia[i][5], listaMidia[i][7], listaMidia[i][8])
                catalogo_geral.adicionarMidia(filme, 'Filme')
            elif listaMidia[i][1] == 'Documentario':
                documentario = Documentario(listaMidia[i][0], listaMidia[i][1], listaMidia[i][2], listaMidia[i][3],
                                            listaMidia[i][4], listaMidia[i][5], listaMidia[i][9])
                catalogo_geral.adicionarMidia(documentario, 'Documentário')
            elif listaMidia[i][1] == 'Animacao':
                animacao = Animacao(listaMidia[i][0], listaMidia[i][1], listaMidia[i][2], listaMidia[i][3], listaMidia[i][4],
                                    listaMidia[i][5], listaMidia[i][10])
                catalogo_geral.adicionarMidia(animacao, 'Animação')
            else:
                programadetv = ProgramaDeTV(listaMidia[i][0], listaMidia[i][1], listaMidia[i][2], listaMidia[i][3],
                                            listaMidia[i][4], listaMidia[i][5], listaMidia[i][6])
                catalogo_geral.adicionarMidia(programadetv, 'Programa de TV')

    def carregarEpisodios(self):
        arqEpisodios = open('./arquivos/episodios.csv')
        leitor = csv.reader(arqEpisodios, delimiter=';')
        listaEpisodios = list(leitor)
        arqEpisodios.close()


        for i in range(1, len(listaEpisodios)):
            episodio = Episodio(listaEpisodios[i][0], listaEpisodios[i][1], listaEpisodios[i][2], listaEpisodios[i][3])
            episodios.append(episodio)

    def distribuirEpisodios(self):
        for episodio in episodios:
            for serie in catalogo_geral.lista_series:
                if episodio.serie == serie.titulo:
                    serie.lista_episodios.append(episodio)

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
        perfis_atual.clear()
        with open('./arquivos/perfis.csv', mode='r', newline='') as perfisArq:
            reader = csv.reader(perfisArq, delimiter=';')
            for row in reader:
                if row[0] == usuario_atual[0].nome:
                    perfil = Perfil(row[1], row[2])
                    perfil.lista_favoritos = row[3:13]
                    perfil.ultimos_assistidos = row[13:23]
                    perfis_atual.append(perfil)
        for perfil in perfis_atual:
            print('Perfil {}: {}'.format(num, perfil.nome))
            num += 1
            tamanho2 = len(perfis_atual) +1
        opcao = menuPerfis()
        if opcao == '1':
            escolha = input('Você gostaria de trocar sua assinatura? (Simples -> Premium | Premium -> Simples)(Sim/Não)')
            if escolha == 'Sim':
                usuario_atual[0].trocarAssinatura()
                return
            elif escolha == 'Não':
                print('Retornando ao menu principal...')
                input('Pressione ENTER para prosseguir...')
                return
            else:
                print('Escolha inválida, retornando ao menu principal...')
                input('Pressione ENTER para prosseguir.')
        if opcao == '2':
            if len(perfis_atual) == 0:
                print('É preciso criar um perfil para continuar, retornando ao menu inicial...')
                input('Pressione ENTER para continuar...')
            else:
                os.system('cls')
                num3 = 1
                tamanho = len(perfis_atual) + 1
                for perfil in perfis_atual:
                    print('Perfil {}: {}'.format(num3, perfil.nome))
                    num3+=1
                perfil_escolha = int(input('Escolha qual perfil acessar: '))
                if perfil_escolha > tamanho2:
                    print('Escolha um perfil válido...')
                    input('Pressione ENTER para retornar ao menu anterior...')
                    return
                else:
                    perfil_acessado.append(perfis_atual[perfil_escolha-1])
                    self.tela = 2
        elif opcao == '3':
            if len(perfis_atual) == 0:
                print('É preciso criar um perfil para continuar, retornando ao menu inicial...')
                input('Pressione ENTER para continuar...')
            else:            
                os.system('cls')
                num2 = 1
                tamanho = len(perfis_atual) + 1
                for perfil in perfis_atual:
                    print('Perfil {}: {}'.format(num2, perfil.nome))
                    num2 += 1
                perfil_editar = int(input('Selecione um perfil para editar: '))
                if perfil_editar > tamanho:
                    num2 = 1
                    print('Esse perfil não existe...')
                    return
                else:
                    num2 = 1
                    novo_nome = input('Escolha um novo nome para o perfil: ')
                    nova_idade = input('Escolha uma nova idade para o perfil: ')
                    nome_antigo = str(perfis_atual[perfil_editar - 1].nome)
                    perfis_atual[perfil_editar - 1].editarPerfil(novo_nome, nova_idade)
                    print('Perfil editado com sucesso.')
                    input('Pressione ENTER para continuar...')
                    rows = []
                    count = 0
                    with open('./arquivos/perfis.csv', mode='r', newline='') as perfisArq:
                        reader = csv.reader(perfisArq, delimiter=';')
                        rows = list(reader)

                    if perfil_editar < len(rows):
                        for perfil in rows:
                            count+=1
                            if perfil[1] == nome_antigo:
                                rows[count-1][1] = novo_nome
                                rows[count-1][2] = nova_idade
                        with open('./arquivos/perfis.csv', mode='w', newline='') as perfisArq:
                            writer = csv.writer(perfisArq, delimiter=';')
                            writer.writerows(rows)
                    else:
                        print('Esse perfil não existe no arquivo CSV.')

                    input('Pressione ENTER para continuar...')
        elif opcao == '4':
            if usuario_atual[0].tipoAssinatura == 'Simples' and len(perfis_atual) < 3 or usuario_atual[0].tipoAssinatura == 'Premium' and len(perfis_atual) < 5:           
                nome = input('Escolha um nome para o perfil: ')
                idade = input('Escolha uma idade para o perfil: ')
                perfil = usuario_atual[0].adicionarPerfil(nome, idade)
                usuario_atual[0].lista_perfis.append(perfil)
            else:
                print('Capacidade máxima de perfis alcançada, exclua um para adicionar outro.')
                input('Pressione ENTER para continuar...')
        elif opcao == '5':
            if len(perfis_atual) == 0:
                print('É preciso criar um perfil para continuar, retornando ao menu inicial...')
                input('Pressione ENTER para continuar...')
            else:            
                os.system('cls')
                print(perfis_atual)
                if len(perfis_atual) != 0:
                    num4 = 1
                    tamanho = len(perfis_atual) + 1
                    for perfil in perfis_atual:
                        print('Perfil {}: {}'.format(num4, perfil.nome))
                        num4+=1
                    perfil_escolha = int(input('Escolha qual perfil remover: '))
                    if perfil_escolha > tamanho2:
                        print('Escolha um perfil válido...')
                        input('Pressione ENTER para retornar ao menu anterior...')
                        return
                    else:
                        usuario_atual[0].removerPerfil(perfis_atual[perfil_escolha-1].nome)
                        perfis_atual.pop(perfil_escolha-1)
                        self.tela = 1
                
        elif opcao == '6':
            usuario_atual.clear()
            perfis_atual.clear()
            self.tela = 0
    
    def telaLogado(self):
        opcao = menuLogado()
        if opcao == '1':
            nome_procura = input('Escreva o nome da mídia que deseja procurar: ')
            for midia in catalogo_geral.lista_animacoes + catalogo_geral.lista_documentarios + catalogo_geral.lista_filmes + catalogo_geral.lista_programasdetv + catalogo_geral.lista_series:
                if midia.titulo == nome_procura:
                    if int(perfil_acessado[0].idade) >= 18 or midia.classificacao != '18':
                        midia_acessada.append(midia)
                        self.tela = 3
                    else:
                        print('Mídia +18 bloqueada.')
                        break
            input('Pressione ENTER para prosseguir...')
        elif opcao == '2':
            os.system('cls')
            print('---Últimos assistidos---')
            for midia in catalogo_geral.lista_animacoes + catalogo_geral.lista_documentarios + catalogo_geral.lista_filmes + catalogo_geral.lista_programasdetv + catalogo_geral.lista_series:
                for favorito in perfil_acessado[0].ultimos_assistidos:
                    if midia.id == favorito:
                        print (midia.titulo)
            input('Pressione ENTER para prosseguir...')
        elif opcao == '3':
            os.system('cls')
            print('---Favoritos---')
            for midia in catalogo_geral.lista_animacoes + catalogo_geral.lista_documentarios + catalogo_geral.lista_filmes + catalogo_geral.lista_programasdetv + catalogo_geral.lista_series:
                for favorito in perfil_acessado[0].lista_favoritos:
                    if midia.id == favorito:
                        print (midia.titulo)
            input('Pressione ENTER para prosseguir...')
        elif opcao == '4':
            os.system('cls')
            count_filme = 0
            print('---Filmes---')
            for midia in catalogo_geral.lista_filmes:
                    count_filme +=1
                    if int(perfil_acessado[0].idade) >= 18 or midia.classificacao != '18':
                        print('{} - {}'.format(count_filme, midia.titulo))
                    else:
                        print('Mídia +18 bloqueada.')
            escolha_filme = input('Digite o número do filme que deseja assistir ou 0 para retornar...')
            if escolha_filme == '0':
                return
            elif int(perfil_acessado[0].idade) < 18 and catalogo_geral.lista_filmes[escolha_filme].classificacao == '18':
                print('Mídia +18 bloqueada escolhida, retornando ao menu anterior...')
                input('Pressione ENTER para prosseguir...')
                return
            else:
                midia_acessada.append(catalogo_geral.lista_filmes[int(escolha_filme)-1])
                self.tela = 3

        elif opcao == '5':
            os.system('cls')
            count_series = 0
            print('---Séries---')
            for midia in catalogo_geral.lista_series:
                    count_series+=1
                    if int(perfil_acessado[0].idade) >= 18 or midia.classificacao != '18':
                        print('{} - {}'.format(count_series, midia.titulo))
                    else:
                        print('Mídia +18 bloqueada.')
            escolha_serie = input('Digite o número do filme que deseja assistir ou 0 para retornar...')
            if escolha_serie == '0':
                return
            elif int(perfil_acessado[0].idade) < 18 and catalogo_geral.lista_series[escolha_serie].classificacao == '18':
                print('Mídia +18 bloqueada escolhida, retornando ao menu anterior...')
                input('Pressione ENTER para prosseguir...')
                return
            else:
                midia_acessada.append(catalogo_geral.lista_series[int(escolha_serie)-1])
                self.tela = 3
        elif opcao == '6':
            os.system('cls')
            count_documentarios = 0
            print('---Documentários---')
            for midia in catalogo_geral.lista_documentarios:
                    count_documentarios+=1
                    if int(perfil_acessado[0].idade) >= 18 or midia.classificacao != '18':
                        print('{} - {}'.format(count_documentarios, midia.titulo))
                    else:
                        print('Mídia +18 bloqueada.')
            escolha_documentarios = input('Digite o número do filme que deseja assistir ou 0 para retornar...')
            if escolha_documentarios == '0':
                return
            elif int(perfil_acessado[0].idade) < 18 and catalogo_geral.lista_documentarios[escolha_documentarios].classificacao == '18':
                print('Mídia +18 bloqueada escolhida, retornando ao menu anterior...')
                input('Pressione ENTER para prosseguir...')
                return
            else:
                midia_acessada.append(catalogo_geral.lista_documentarios[int(escolha_documentarios)-1])
                self.tela = 3
        elif opcao == '7':
            os.system('cls')
            count_animacoes = 0
            print('---Animações---')
            for midia in catalogo_geral.lista_animacoes:
                    count_animacoes+=1
                    if int(perfil_acessado[0].idade) >= 18 or midia.classificacao != '18':
                        print('{} - {}'.format(count_animacoes, midia.titulo))
                    else:
                        print('Mídia +18 bloqueada.')
            escolha_animacao = input('Digite o número do filme que deseja assistir ou 0 para retornar...')
            if escolha_animacao == '0':
                return
            elif int(perfil_acessado[0].idade) < 18 and catalogo_geral.lista_animacoes[escolha_animacao].classificacao == '18':
                print('Mídia +18 bloqueada escolhida, retornando ao menu anterior...')
                input('Pressione ENTER para prosseguir...')
                return
            else:
                midia_acessada.append(catalogo_geral.lista_animacoes[int(escolha_animacao)-1])
                self.tela = 3
        elif opcao == '8':
            os.system('cls')
            count_programasdetv = 0
            print('---Programas de TV---')
            for midia in catalogo_geral.lista_programasdetv:
                    count_programasdetv+=1
                    if int(perfil_acessado[0].idade) >= 18 or midia.classificacao != '18':
                        print('{} - {}'.format(count_programasdetv, midia.titulo))
                    else:
                        print('Mídia +18 bloqueada.')
            escolha_programadetv = input('Digite o número do filme que deseja assistir ou 0 para retornar...')
            if escolha_programadetv == '0':
                return
            elif int(perfil_acessado[0].idade) < 18 and catalogo_geral.lista_programasdetv[escolha_programadetv].classificacao == '18':
                print('Mídia +18 bloqueada escolhida, retornando ao menu anterior...')
                input('Pressione ENTER para prosseguir...')
                return
            else:
                midia_acessada.append(catalogo_geral.lista_programasdetv[int(escolha_programadetv)-1])
                self.tela = 3            
        elif opcao == '9':
            novo_favorito = perfil_acessado[0].lista_favoritos
            novo_ultimo = perfil_acessado[0].ultimos_assistidos
            print(novo_favorito)
            print(novo_ultimo)
            count = 0
            with open('./arquivos/perfis.csv', mode='r', newline='') as perfisArq:
                reader = csv.reader(perfisArq, delimiter=';')
                rows = list(reader)
                for perfil in rows:
                    count += 1
                    if perfil[1] == perfil_acessado[0].nome:
                        rows[count - 1][3:12] = novo_favorito[0:9]
                        rows[count - 1][13:22] = novo_ultimo[0:9]

            with open('./arquivos/perfis.csv', mode='w', newline='') as perfisArq:
                writer = csv.writer(perfisArq, delimiter=';')
                writer.writerows(rows)

            input('Pressione ENTER para continuar...')
            perfil_acessado.clear()
            self.tela = 1



    def telaMidia(self):
        os.system('cls')
        midia_acessada[0].exibirInformacoes()
        if midia_acessada[0].tipo == 'Serie' or midia_acessada[0].tipo == 'Programa de TV':
            opcao = menuMidiaSeriePrograma()
            if opcao == '1':
                midia_acessada[0].listarEpisodios()
                escolha_episodio = input('Escolha um episódio para assistir: ')
                perfil_acessado[0].assistirSerie(midia_acessada[0], escolha_episodio)
                input('Pressione ENTER para prosseguir...')
            elif opcao == '2':
                perfil_acessado[0].favoritar(midia_acessada[0])
                input('Pressione ENTER para prosseguir...')
            elif opcao == '3':
                midia_acessada.clear()
                self.tela = 2
        else:
            opcao = menuMidiaNormal()
            if opcao == '1':
                perfil_acessado[0].assistir(midia_acessada[0])
                input('Pressione ENTER para prosseguir...')
                return
            elif opcao == '2':
                perfil_acessado[0].favoritar(midia_acessada[0])
                input('Pressione ENTER para prosseguir...')
            elif opcao == '3':
                midia_acessada.clear()
                self.tela = 2



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
