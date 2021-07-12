from collections import namedtuple

import pandas as pd

from tablero.dashboard import is_main, is_develop, get_badge, get_dashboard, get_row_to_append

registro = namedtuple("registro", ["repo", "objetivo", "revision", "exitoso"])


def assert_dashboard_columns(tablero):
    columnas_esperadas = sorted(["repo", "objetivo", "develop", "main"])
    columnas_obtenidas = sorted(tablero)
    assert columnas_obtenidas == columnas_esperadas


def test_is_main():
    main_es_main = is_main(registro("repositorio", "reporte", "main", 0))
    master_es_main = is_main(registro("repositorio", "reporte", "master", 0))
    stable_es_main = is_main(registro("repositorio", "reporte", "stable", 0))
    assert main_es_main
    assert master_es_main
    assert not stable_es_main


def test_is_develop():
    dev_es_develop = is_develop(registro("repositorio", "reporte", "dev", 0))
    develop_es_develop = is_develop(registro("repositorio", "reporte", "develop", 0))
    development_es_develop = is_develop(registro("repositorio", "reporte", "development", 0))
    assert not dev_es_develop
    assert develop_es_develop
    assert development_es_develop


def test_get_badge():
    medalla_exito = "https://img.shields.io/badge/make-PASS-success.svg"
    medalla_fracaso = "https://img.shields.io/badge/make-FAIL-red.svg"
    medalla_na = "https://img.shields.io/badge/make-NA-lightgrey.svg"
    assert (
        get_badge(registro("repositorio", "reporte", "rama", pd.Series([0])), False) == medalla_na
    )
    assert (
        get_badge(registro("repositorio", "reporte", "rama", pd.Series([1])), False) == medalla_na
    )
    assert (
        get_badge(registro("repositorio", "reporte", "rama", pd.Series([0])), True)
        == medalla_fracaso
    )
    assert (
        get_badge(registro("repositorio", "reporte", "rama", pd.Series([1])), True) == medalla_exito
    )


def test_dashboard_columns_from_test_datafile():
    tablero = get_dashboard(log_name="data/testmake.test.csv")
    assert_dashboard_columns(tablero)


def test_dashboard_columns_from_empty_datafile():
    tablero = get_dashboard()
    assert_dashboard_columns(tablero)


def test_dashboard_size_from_test_datafile():
    tablero = get_dashboard(log_name="data/testmake.test.csv")
    tamano_esperado = (17, 4)
    tamano_obtenido = tablero.shape
    assert tamano_obtenido == tamano_esperado


def test_dashboard_size_from_empty_datafile():
    tablero = get_dashboard()
    n_cols_esperado = 4
    n_cols_obtenido = tablero.shape[1]
    assert n_cols_obtenido == n_cols_esperado


def test_develop0_developFail():
    registro = pd.DataFrame(
        {"repo": "repositorio", "objetivo": "reporte", "revision": "develop", "exitoso": [0]},
        columns=["repo", "objetivo", "revision", "exitoso"],
    )
    renglon = get_row_to_append(registro, "repositorio", "objetivo")
    assert "FAIL" in renglon["develop"]
    assert "NA" in renglon["main"]


def test_develop1_developPass():
    registro = pd.DataFrame(
        {"repo": "repositorio", "objetivo": "reporte", "revision": "develop", "exitoso": [1]},
        columns=["repo", "objetivo", "revision", "exitoso"],
    )
    renglon = get_row_to_append(registro, "repositorio", "objetivo")
    assert "PASS" in renglon["develop"]
    assert "NA" in renglon["main"]


def test_master0_masterFail():
    registro = pd.DataFrame(
        {"repo": "repositorio", "objetivo": "reporte", "revision": "master", "exitoso": [0]},
        columns=["repo", "objetivo", "revision", "exitoso"],
    )
    renglon = get_row_to_append(registro, "repositorio", "objetivo")
    assert "NA" in renglon["develop"]
    assert "FAIL" in renglon["main"]


def test_master1_masterPass():
    registro = pd.DataFrame(
        {"repo": "repositorio", "objetivo": "reporte", "revision": "master", "exitoso": [1]},
        columns=["repo", "objetivo", "revision", "exitoso"],
    )
    renglon = get_row_to_append(registro, "repositorio", "objetivo")
    assert "NA" in renglon["develop"]
    assert "PASS" in renglon["main"]
