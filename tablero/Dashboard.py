#!/usr/bin/python3
# coding: utf-8
import numpy as np
import pandas as pd

from .io.load_record import get_records

def is_develop(rama):
    es_develop = ((rama == "develop") | (rama == "development"))
    return es_develop

def get_dashboard():
    registro_ramas = get_records()
    medalla_exito = "https://img.shields.io/badge/make-passing-green.svg"
    medalla_fracaso = "https://img.shields.io/badge/make-failing-red.svg"
    medalla_na = "https://img.shields.io/badge/make-NA-lightgrey.svg"
    es_rama = is_develop(registro_ramas.revision) | (registro_ramas.revision == "default")
    tablero_ramas = registro_ramas[es_rama]
    tablero = pd.DataFrame(columns=['repo', 'objetivo', 'develop', 'default'])
    for (repo, objetivo), tabla in tablero_ramas.groupby(by=["repo","objetivo"]):
        es_develop = is_develop(tabla.revision)
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
