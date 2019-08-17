#!/usr/bin/python3
# coding: utf-8
import numpy as np
import pandas as pd

from .io import get_last_record_per_revision


def is_default(registro):
    es_default = ((registro.revision == "default")
                  | (registro.revision == "master"))
    return es_default


def is_develop(registro):
    es_develop = ((registro.revision == "develop") |
                  (registro.revision == "development"))
    return es_develop


def get_badge(registro, es_rama):
    medalla_exito = "https://img.shields.io/badge/make-PASS-green.svg"
    medalla_fracaso = "https://img.shields.io/badge/make-FAIL-red.svg"
    medalla_na = "https://img.shields.io/badge/make-NA-lightgrey.svg"
    if not np.any(es_rama):
        medalla = medalla_na
    elif registro.exitoso.values[es_rama][-1] == 1:
        medalla = medalla_exito
    else:
        medalla = medalla_fracaso
    return medalla


def get_dashboard():
    registro_ramas = get_last_record_per_revision()
    es_rama = is_develop(registro_ramas) | is_default(registro_ramas)
    tablero_ramas = registro_ramas[es_rama]
    tablero = pd.DataFrame(columns=['repo', 'objetivo', 'develop', 'default'])
    for (repo, objetivo), registro in tablero_ramas.groupby(by=["repo", "objetivo"]):
        tablero = append_row_to_dashboard(registro, repo, objetivo, tablero)
    return tablero


def append_row_to_dashboard(registro, repo, objetivo, tablero):
    es_default = is_default(registro)
    es_develop = is_develop(registro)
    medalla_default = get_badge(registro, es_default)
    medalla_develop = get_badge(registro, es_develop)
    renglon_concatenar = {"repo": repo, "objetivo": objetivo,
                          "develop": medalla_develop, "default": medalla_default}
    tablero = tablero.append(renglon_concatenar, ignore_index=True)
    return tablero
