#!/usr/bin/python3
# coding: utf-8
import numpy as np
import pandas as pd

from .io import get_records


def is_default(tabla):
    es_default = ((tabla.revision == "default") | (tabla.revision == "master"))
    return es_default


def is_develop(tabla):
    es_develop = ((tabla.revision == "develop") | (tabla.revision == "development"))
    return es_develop


def is_successful(tabla, es_rama):
    medalla_exito = "https://img.shields.io/badge/make-passing-green.svg"
    medalla_fracaso = "https://img.shields.io/badge/make-failing-red.svg"
    medalla_na = "https://img.shields.io/badge/make-NA-lightgrey.svg"
    if not np.any(es_rama):
        es_exitoso = medalla_na
    elif tabla.exitoso.values[es_rama][-1] == 1:
        es_exitoso = medalla_exito
    else:
        es_exitoso = medalla_fracaso
    return es_exitoso


def get_dashboard():
    registro_ramas = get_records()
    es_rama = is_develop(registro_ramas) | is_default(registro_ramas)
    tablero_ramas = registro_ramas[es_rama]
    tablero = pd.DataFrame(columns=['repo', 'objetivo', 'develop', 'default'])
    for (repo, objetivo), tabla in tablero_ramas.groupby(by=["repo", "objetivo"]):
        es_default = is_default(tabla)
        es_develop = is_develop(tabla)
        es_exitoso_default = is_successful(tabla, es_default)
        es_exitoso_develop = is_successful(tabla, es_develop)
        renglon_concatenar = {"repo": repo, "objetivo": objetivo,
                              "develop": es_exitoso_develop, "default": es_exitoso_default}
        tablero = tablero.append(renglon_concatenar, ignore_index=True)
    return tablero
