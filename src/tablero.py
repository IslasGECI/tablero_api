#!/usr/bin/python3
# coding: utf-8
import numpy as np
import pandas as pd

def get_records(log_name="~/.testmake/testmake.log.csv"):
    registro_testmake = pd.read_csv(log_name)
    registro_testmake.timestamp = pd.to_datetime(registro_testmake.timestamp)
    registro_testmake = registro_testmake.sort_values(by="timestamp")
    registro_testmake["exito"] = registro_testmake.es_make_exitoso & (registro_testmake.es_phony | registro_testmake.existe_objetivo)
    registro_ramas = pd.DataFrame(
        columns=['repo', 'objetivo', 'revision', 'exitoso'])
    for (repo, objetivo, revision), tabla in registro_testmake.groupby(["repo", "objetivo", "revision"]):
        ultimo_renglon = tabla.iloc[-1]
        renglon_concatenar = {"repo": repo, "objetivo": objetivo,
                            "revision": revision, "exitoso": ultimo_renglon.exito}
        registro_ramas = registro_ramas.append(renglon_concatenar, ignore_index=True)
    return registro_ramas

def get_dashboard():
    registro_ramas = get_records()
    medalla_exito = "https://img.shields.io/badge/make-passing-green.svg"
    medalla_fracaso = "https://img.shields.io/badge/make-failing-red.svg"
    medalla_na = "https://img.shields.io/badge/make-NA-lightgrey.svg"
    es_rama = ((registro_ramas.revision == "develop") | (registro_ramas.revision == "development")) | (registro_ramas.revision == "default")
    tablero_ramas = registro_ramas[es_rama]
    tablero = pd.DataFrame(columns=['repo', 'objetivo', 'develop', 'default'])
    for (repo, objetivo), tabla in tablero_ramas.groupby(by=["repo","objetivo"]):
        es_develop = ((tabla.revision == "develop") | (tabla.revision == "development"))
        if not np.any(es_develop):
            es_exitoso_develop = medalla_na
        elif tabla.exitoso.values[es_develop][0] == 1:
            es_exitoso_develop = medalla_exito
        else:
            es_exitoso_develop = medalla_fracaso
        es_default = tabla.revision == "default"
        if not np.any(es_default):
            es_exitoso_default = medalla_na
        elif tabla.exitoso.values[es_default][0] == 1:
            es_exitoso_default = medalla_exito
        else:
            es_exitoso_default = medalla_fracaso
        renglon_concatenar = {"repo": repo, "objetivo": objetivo, "develop": es_exitoso_develop, "default": es_exitoso_default}
        tablero = tablero.append(renglon_concatenar, ignore_index=True)
    return tablero.values.tolist()
