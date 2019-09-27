import requests


def buscar_usuario(username):
    """
    Busca perfil de um usuario no Github

    :param username: str com o nome de usuario no github
    :return: json com os dados do perfil do usuario
    """

    url = f'https://api.github.com/users/{username}'
    r = requests.get(url)
    return r.json()

if __name__ == '__main__':
    user = buscar_usuario('undersfx')
    print(user['avatar_url'])
