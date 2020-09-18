import pytest
from libpythonpro import github_api
from unittest.mock import Mock


@pytest.fixture
def avatar_url():
    resp_mock = Mock()
    url = 'https://avatars2.githubusercontent.com/u/7119450?v=4'
    resp_mock.json.return_value = {'login': 'undersfx', 'avatar_url': url}
    request_original = github_api.requests.get
    github_api.requests.get = Mock(return_value=resp_mock)
    yield url
    github_api.requests.get = request_original


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_usuario('undersfx')
    assert avatar_url == url


def test_buscar_avatar_integracao():
    url = github_api.buscar_usuario('renzon')
    assert 'https://avatars3.githubusercontent.com/u/3457115?v=4' == url
