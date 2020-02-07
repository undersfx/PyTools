from libpythonpro import github_api
from unittest.mock import Mock

def test_buscar_avatar():
    resp_mock = Mock()
    resp_mock.json.return_value = {'login':'undersfx', 'avatar_url': 'https://avatars2.githubusercontent.com/u/7119450?v=4'}
    github_api.requests.get = Mock(return_value=resp_mock)
    url = github_api.buscar_usuario('undersfx')
    assert 'https://avatars2.githubusercontent.com/u/7119450?v=4' == url