"""
Arquivo de configuração do pytest para disponibilizar as fixtures para mais de um teste.

Todos os arquivos no mesmo nível de árvore que conftest.py poderão utilizar as fixtures de seu conteúdo.
"""

import pytest
from libpythonpro.spam.db import Conexao


@pytest.fixture(scope='session')  # Can be 'function' (Default), 'module' or 'session'
def conexao():
    conexao_obj = Conexao()
    yield conexao_obj
    conexao_obj.fechar()


@pytest.fixture
def sessao(conexao):
    # Setup
    sessao_obj = conexao.gerar_sessao()
    yield sessao_obj
    # Tear Down
    sessao_obj.rollback()
    sessao_obj.fechar()
