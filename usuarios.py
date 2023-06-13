class Ususario:
    def __init__(self, nome,senha,tipoAsinatura):
        self._nome= nome
        self._senha= senha
        self._tipoAsinatura= tipoAsinatura
    def adicionaPerfil(self,nome,idade):
        perfil=[]
        if self._tipoAsinatura == 'SIMPLES' and len(perfil) < 3:
            perfil.append(nome,idade)
            return perfil
        elif  self._tipoAsinatura == 'PREMIUM' and len(perfil) < 5:
            perfil.append(nome, idade)
            return perfil
         