class Sessao:
    contador = 0
    usuarios = []

    def salvar(self, usuario):
        Sessao.contador += 1
        usuario.id = Sessao.contador
        Sessao.usuarios.append(usuario)

    def listar(self):
        return Sessao.usuarios

    def rollback(self):
        Sessao.usuarios.clear()

    def fechar(self):
        pass


class Conexao:
    def gerar_sessao(self):
        return Sessao()

    def fechar(self):
        pass


class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.id = None
