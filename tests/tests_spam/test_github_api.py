import pytest
from libpythonpro import github_api
from unittest.mock import Mock


@pytest.fixture
def avatar_url(mocker):
    # Criação do objeto resposta (Mock da resposta da API)
    resp_mock = Mock()
    url = 'https://avatars.githubusercontent.com/u/3457115?v=4'
    resp_mock.json.return_value = {'login': 'renzon', 'avatar_url': url}

    # request_original = github_api.requests.get
    # github_api.requests.get = Mock(return_value=resp_mock)
    # yield url
    # github_api.requests.get = request_original

    # Substituição do método "get" da lib requests com mocker (pytest-mock)
    get_mock = mocker.patch('libpythonpro.github_api.requests.get')
    get_mock.return_value = resp_mock
    return url


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_usuario('undersfx')
    assert avatar_url == url


def test_buscar_avatar_integracao():
    url = github_api.buscar_usuario('renzon')
    assert 'https://avatars.githubusercontent.com/u/3457115?v=4' == url
