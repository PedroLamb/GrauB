import os
import csv

class Usuario:
    def __init__(self,id, nome,senha,tipoAssinatura):
        self.id = id
        self.nome= nome
        self.senha= senha
        self.tipoAssinatura= tipoAssinatura
        self.lista_perfis = []
   

    def cadastrarUsuario(self):
        nome = input('Informe o nome de usuário que deseja utilizar: ')
        senha = input('Informe a senha que deseja utilizar: ')
        os.system('cls')
        print('''--- Assinatura Simples ---
    Direito a 3 perfis.
    Propagandas entre mídias assistidas.
    Custo: R$ 29,90/mês

    --- Assinatura Premium ---
    Direito a 5 perfis.
    Sem propagandas.
    Custo: R$ 49,90/mês''')
        tipoAssinatura = input('Qual tipo de assinatura você deseja? (Simples/Premium)')
        if tipoAssinatura == 'Simples' or tipoAssinatura == 'Premium':
            with open('./arquivos/Usuarios.csv', mode='r') as usuariosArq:
                reader = csv.reader(usuariosArq, delimiter=';')
                for row in reader:
                    if row[1] == nome:
                        print("Nome de usuário já existe.")
                        input('Pressione ENTER para voltar à tela inicial...')
                        return
            
            with open('./arquivos/Usuarios.csv', mode='r') as usuariosArq:
                reader = csv.reader(usuariosArq, delimiter=';')
                next(reader) 
                id = sum(1 for _ in reader)
            
            novo_usuario = Usuario(id, nome, senha, tipoAssinatura)
            with open('./arquivos/Usuarios.csv', 'a', newline='') as arquivo_csv:
                escritor = csv.writer(arquivo_csv, delimiter=';')
                escritor.writerow([novo_usuario._id, novo_usuario._nome, novo_usuario._senha, novo_usuario._tipoAssinatura])
            
            print('Usuário cadastrado com sucesso!')
            input('Pressione ENTER para retornar ao menu inicial...')
        else:
            print('Escolha um tipo válido de assinatura.')
            input('Pressione ENTER para retornar ao menu inicial...')


    def adicionarPerfil(self,nome,idade):
        perfil=[]
        if self._tipoAsinatura == 'Simples' and len(perfil) < 3:
            perfil.append(nome,idade)
            return perfil
        elif  self._tipoAsinatura == 'Premium' and len(perfil) < 5:
            perfil.append(nome, idade)
            return perfil
        
class Perfil:
    def __init__(self, nome, idade):
         self.nome = nome
         self.idade = idade
         self.lista_favoritos = []
         self.ultimos_assistidos = []

    def adicionarFavorito(self, midia):
        self.lista_favoritos.append(midia)

    def removerFavorito(self, midia):
        self.lista_favoritos.remove(midia)

    def editarPerfil(self, novo_nome, nova_idade):
        self.nome = novo_nome
        self.idade = nova_idade

    def ultimoAssistidoCheio(self):
        return len(self.ultimos_assistidos) == 10

    def listarMidiasApropriadas(self):
        pass

    def assistir(self, midia):
        count = 0
        print('{} está sendo exibido.'.format(midia.titulo))
        for conteudo in self.ultimos_assistidos:
            if conteudo == '-':
                pass
            else:
                count+=1
        if midia.id in self.ultimos_assistidos:
            return
        if count == 9:
            self.ultimos_assistidos[9] = self.ultimos_assistidos[8]
            self.ultimos_assistidos[8] = self.ultimos_assistidos[7]
            self.ultimos_assistidos[7] = self.ultimos_assistidos[6]
            self.ultimos_assistidos[6] = self.ultimos_assistidos[5]
            self.ultimos_assistidos[4] = self.ultimos_assistidos[3]
            self.ultimos_assistidos[3] = self.ultimos_assistidos[2]
            self.ultimos_assistidos[2] = self.ultimos_assistidos[1]
            self.ultimos_assistidos[1] = self.ultimos_assistidos[0]
            self.ultimos_assistidos[0] = midia.id
            print (self.ultimos_assistidos)

        else:
            self.ultimos_assistidos.append(midia.id)
            print(self.ultimos_assistidos)

    def assistirSerie(self, midia, episodio):
        count = 0
        print('{} - Episódio {} está sendo exibido.'.format(midia.titulo, episodio))
        for conteudo in self.ultimos_assistidos:
            if conteudo == '-':
                pass
            else:
                count+=1
        if midia.id in self.ultimos_assistidos:
            return
        if count == 9:
            self.ultimos_assistidos[9] = self.ultimos_assistidos[8]
            self.ultimos_assistidos[8] = self.ultimos_assistidos[7]
            self.ultimos_assistidos[7] = self.ultimos_assistidos[6]
            self.ultimos_assistidos[6] = self.ultimos_assistidos[5]
            self.ultimos_assistidos[4] = self.ultimos_assistidos[3]
            self.ultimos_assistidos[3] = self.ultimos_assistidos[2]
            self.ultimos_assistidos[2] = self.ultimos_assistidos[1]
            self.ultimos_assistidos[1] = self.ultimos_assistidos[0]
            self.ultimos_assistidos[0] = midia.id
            print(self.ultimos_assistidos)
        else:
            self.ultimos_assistidos.append(midia.id)
            print(self.ultimos_assistidos)
    def favoritar(midia):
        pass

    def buscarPorTitulo(titulo, catalogo):
        pass