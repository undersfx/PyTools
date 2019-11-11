class Enviador:
    def enviar(self, remetente, distinatario, assunto, corpo):
        if '@' not in remetente:
            raise EmailInvalido(f'Email remetente {remetente} inválido.')
        return remetente


class EmailInvalido(Exception):
    pass
