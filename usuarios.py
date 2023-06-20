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


    def adicionarPerfil(self, nome, idade):
        perfil = Perfil(nome, idade)
        with open('./arquivos/perfis.csv', 'a', newline='') as arquivo_csv:
            escritor = csv.writer(arquivo_csv, delimiter=';')
            escritor.writerow([self.nome, nome, idade, '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'])
            return perfil
          
        
    def trocarAssinatura(self):
        if self.tipoAssinatura == 'Premium' and len(self.lista_perfis) > 3:
            print('Remova um perfil para prosseguir...')
            input('Pressione ENTER para prosseguir.')
        elif self.tipoAssinatura == 'Premium' and len(self.lista_perfis) <= 3:
            self.tipoAssinatura = 'Simples'
            with open('./arquivos/usuarios.csv', 'r', newline='') as arquivo_csv:
                reader = csv.reader(arquivo_csv, delimiter=';')
                rows = list(reader)

            for perfil in rows:
                if perfil[1] == self.nome:
                    perfil[3] = 'Simples'

            with open('./arquivos/usuarios.csv', 'w', newline='') as arquivo_csv:
                writer = csv.writer(arquivo_csv, delimiter=';')
                writer.writerows(rows)            
            print('Assinatura trocada de Premium para Simples com sucesso.')
            input('Pressione ENTER para prosseguir.')
        elif self.tipoAssinatura == 'Simples':
            with open('./arquivos/usuarios.csv', 'r', newline='') as arquivo_csv:
                reader = csv.reader(arquivo_csv, delimiter=';')
                rows = list(reader)

            for perfil in rows:
                if perfil[1] == self.nome:
                    perfil[3] = 'Premium'

            with open('./arquivos/usuarios.csv', 'w', newline='') as arquivo_csv:
                writer = csv.writer(arquivo_csv, delimiter=';')
                writer.writerows(rows)   
            self.tipoAssinatura = 'Premium'
            print('Assinatura trocada de Simples para Premium com sucesso.')
            input('Pressione ENTER para prosseguir...')   


    def removerPerfil(self,nome_perfil):
        with open('./arquivos/perfis.csv', 'r', newline='') as arquivo_csv:
            reader = csv.reader(arquivo_csv, delimiter=';')
            rows = list(reader)

        for i, perfil in enumerate(rows):
            if perfil[1] == nome_perfil:
                rows.pop(i)
                break

        with open('./arquivos/perfis.csv', 'w', newline='') as arquivo_csv:
            writer = csv.writer(arquivo_csv, delimiter=';')
            writer.writerows(rows)

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
            count2 = 0
            for conteudo in self.ultimos_assistidos:
                if conteudo == '-':
                    pass
                else:
                    count2+=1
            self.ultimos_assistidos[count2] = midia.id

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
        elif count == 10:
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
            count2 = 0
            for conteudo in self.ultimos_assistidos:
                if conteudo == '-':
                    pass
                else:
                    count2+=1
            self.ultimos_assistidos[count2] = midia.id

    def favoritar(self, midia):
        count = 0
        for conteudo in self.lista_favoritos:
            if conteudo == '-':
                pass
            else:
                count+=1
        if midia.id in self.lista_favoritos:
                self.lista_favoritos.pop(midia.id)
                print('Item removido dos favoritos com sucesso...')
                pass
        elif count == 10:
            self.lista_favoritos[9] = self.lista_favoritos[8]
            self.lista_favoritos[8] = self.lista_favoritos[7]
            self.lista_favoritos[7] = self.lista_favoritos[6]
            self.lista_favoritos[6] = self.lista_favoritos[5]
            self.lista_favoritos[5] = self.lista_favoritos[4]
            self.lista_favoritos[4] = self.lista_favoritos[3]
            self.lista_favoritos[3] = self.lista_favoritos[2]
            self.lista_favoritos[2] = self.lista_favoritos[1]
            self.lista_favoritos[0] = midia.id
        else:
            count2 = 0
            for conteudo in self.lista_favoritos:
                if conteudo == '-':
                    pass
                else:
                    count2+=1
            self.lista_favoritos[count2] = midia.id
                


    def buscarPorTitulo(titulo, catalogo):
        pass