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
