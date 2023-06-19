import os
import csv

class Usuario:
    def __init__(self, nome,senha,tipoAsinatura):
        self._nome= nome
        self._senha= senha
        self._tipoAsinatura= tipoAsinatura
   

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
        assinatura = input('Qual tipo de assinatura você deseja?(Simples/Premium)')
        if assinatura == 'Simples' or assinatura == 'Premium':
            with open('./arquivos/Usuarios.csv', mode='r') as usuariosArq:
                reader = csv.reader(usuariosArq)
                for row in reader:
                    if row[1] == nome:
                        print("Nome de usuário já existe.")
                        input('Pressione ENTER para voltar à tela inicial...')
                        return
                    else:
                        novo_usuario = (Usuario(nome, senha, assinatura))
                        with open('caminho_do_arquivo.csv', 'a', newline='') as arquivo_csv:
                            escritor = csv.writer(arquivo_csv, delimiter=';')
                            escritor.writerow([novo_usuario.id, novo_usuario.nome, novo_usuario.senha, novo_usuario.assinatura])
                    
                        print('Usuário cadastrado com sucesso!')
        else:
            print('Escolha um tipo válido de assinatura.')
            input('Pressione ENTER para retornar ao menu inicial...')
            return


    def adicionaPerfil(self,nome,idade):
        perfil=[]
        if self._tipoAsinatura == 'Simples' and len(perfil) < 3:
            perfil.append(nome,idade)
            return perfil
        elif  self._tipoAsinatura == 'Premium' and len(perfil) < 5:
            perfil.append(nome, idade)
            return perfil
        

         