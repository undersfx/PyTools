class Enviador:
    def __init__(self):
        self.quantidade_emails_enviados = 0

    def enviar(self, remetente, distinatario, assunto, corpo):
        if '@' not in remetente:
            raise EmailInvalido(f'Email remetente {remetente} inválido.')
        self.quantidade_emails_enviados += 1
        return remetente


class EmailInvalido(Exception):
    pass
