#!/usr/bin/python3
# coding: utf-8
import numpy as np
import pandas as pd

from .io import get_last_record_per_revision


def get_dashboard(log_name="data/testmake.log.csv"):
    registro_ramas = get_last_record_per_revision(log_name)
    es_rama = is_develop(registro_ramas) | is_main(registro_ramas)
    tablero_ramas = registro_ramas[es_rama]
    tablero = pd.DataFrame(columns=["repo", "objetivo", "develop", "main"])
    for (repo, objetivo), registros_agrupados in tablero_ramas.groupby(by=["repo", "objetivo"]):
        tablero = append_row_to_dashboard(registros_agrupados, repo, objetivo, tablero)
    return tablero


def is_develop(registro):
    es_develop = (registro.revision == "develop") | (registro.revision == "development")
    return es_develop


def is_main(registro):
    es_main = (registro.revision == "main") | (registro.revision == "master")
    return es_main


def append_row_to_dashboard(registros_agrupados, repo, objetivo, tablero):
    renglon_concatenar_dict = get_row_to_append(registros_agrupados, repo, objetivo)
    renglon_concatenar = pd.DataFrame([renglon_concatenar_dict])
    tablero = pd.concat([tablero, renglon_concatenar], ignore_index=True)
    return tablero


def get_row_to_append(registros_agrupados, repo, objetivo):
    es_main = is_main(registros_agrupados)
    es_develop = is_develop(registros_agrupados)
    medalla_main = get_badge(registros_agrupados, es_main)
    medalla_develop = get_badge(registros_agrupados, es_develop)
    renglon_concatenar = {
        "repo": repo,
        "objetivo": objetivo,
        "develop": medalla_develop,
        "main": medalla_main,
    }
    return renglon_concatenar


def get_badge(registro, es_rama):
    medalla_exito = "https://img.shields.io/badge/make-PASS-success.svg"
    medalla_fracaso = "https://img.shields.io/badge/make-FAIL-red.svg"
    medalla_na = "https://img.shields.io/badge/make-NA-lightgrey.svg"
    if not np.any(es_rama):
        medalla = medalla_na
    elif registro.exitoso.values[es_rama][-1] == 1:
        medalla = medalla_exito
    else:
        medalla = medalla_fracaso
    return medalla
