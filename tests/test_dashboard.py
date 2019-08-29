from collections import namedtuple

import pandas as pd

from tablero.dashboard import *

registro = namedtuple('registro', ['repo', 'objetivo', 'revision', 'exitoso'])


def test_is_default():
    default_es_default = is_default(
        registro('repositorio', 'reporte', 'default', 0))
    master_es_default = is_default(
        registro('repositorio', 'reporte', 'master', 0))
    stable_es_default = is_default(
        registro('repositorio', 'reporte', 'stable', 0))
    assert default_es_default
    assert master_es_default
    assert not stable_es_default


def test_is_develop():
    dev_es_develop = is_develop(registro('repositorio', 'reporte', 'dev', 0))
    develop_es_develop = is_develop(
        registro('repositorio', 'reporte', 'develop', 0))
    development_es_develop = is_develop(
        registro('repositorio', 'reporte', 'development', 0))
    assert not dev_es_develop
    assert develop_es_develop
    assert development_es_develop


def test_get_badge():
    medalla_exito = "https://img.shields.io/badge/make-PASS-green.svg"
    medalla_fracaso = "https://img.shields.io/badge/make-FAIL-red.svg"
    medalla_na = "https://img.shields.io/badge/make-NA-lightgrey.svg"
    assert get_badge(registro('repositorio', 'reporte',
                              'rama', pd.Series([0])), False) == medalla_na
    assert get_badge(registro('repositorio', 'reporte',
                              'rama', pd.Series([1])), False) == medalla_na
    assert get_badge(registro('repositorio', 'reporte',
                              'rama', pd.Series([0])), True) == medalla_fracaso
    assert get_badge(registro('repositorio', 'reporte',
                              'rama', pd.Series([1])), True) == medalla_exito


def test_get_dashboard():
    tablero = get_dashboard(log_name="data/testmake.test.csv")
    columnas_obtenidas = sorted(tablero)
    columnas_eperadas = ['default', 'develop', 'objetivo', 'repo']
    assert columnas_obtenidas == columnas_eperadas
    tamano_obtenido = tablero.shape
    tamano_esperado = (17, 4)
    assert tamano_obtenido == tamano_esperado
