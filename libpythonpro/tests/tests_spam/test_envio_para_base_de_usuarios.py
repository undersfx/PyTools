import pytest
from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario
from unittest.mock import Mock

# Refactored with Mock class
# class EnviadorMock(Enviador):
#     def __init__(self):
#         super().__init__()
#         self.quantidade_emails_enviados = 0
#         self.parametros_de_envio = None

#     def enviar(self, remetente, distinatario, assunto, corpo):
#         self.quantidade_emails_enviados += 1
#         self.parametros_de_envio = (remetente, distinatario, assunto, corpo)
#         return remetente


def test_envio_de_spam(sessao):
    enviador_de_spam = EnviadorDeSpam(sessao, Enviador())
    enviador_de_spam.enviar_emails(
        'renzo@python.pro.br',
        'Curso Python Pro',
        'Novos Módulos'
    )


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Renzo', email='renzo@python.pro.br'),
            Usuario(nome='Luciano', email='luciano@python.pro.br')
        ],
        [
            Usuario(nome='Renzo', email='renzo@python.pro.br')
        ]
    ]
    )
def test_quantidade_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)  # Injeção de Dependências
    enviador_de_spam.enviar_emails(
        'renzo@python.pro.br',
        'Curso Python Pro',
        'Novos Módulos'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Renzo', email='renzo@python.pro.br')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'renzo@python.pro.br',
        'Curso Python Pro',
        'Novos Módulos'
    )
    enviador.enviar.assert_called_once_with('renzo@python.pro.br',
                                            'renzo@python.pro.br',
                                            'Curso Python Pro',
                                            'Novos Módulos')
