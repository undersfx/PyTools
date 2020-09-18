import requests


def buscar_usuario(username: str) -> dict:
    """
    Busca perfil de um usuario no Github

    :param username: str com o nome de usuario no github
    :return: dict com os dados do perfil do usuario
    """

    url = f'https://api.github.com/users/{username}'
    r = requests.get(url)
    return r.json()['avatar_url']
