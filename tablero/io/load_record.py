#!/usr/bin/python3
# coding: utf-8
import numpy as np
import pandas as pd

def get_last_record(tabla):
    # `tabla` contiene los registros de todos los intentos de generar el
    # objetivo, de los cuales sólo nos interesa el más reciente
    return tabla.sort_values(by="timestamp").iloc[-1]

def get_last_record_per_revision(log_name="data/testmake.log.csv"):
    registro_testmake = pd.read_csv(log_name).sort_values(by="timestamp")
    registro_testmake["exito"] = registro_testmake.es_make_exitoso & (
        registro_testmake.es_phony | registro_testmake.existe_objetivo)
    registro_ramas = pd.DataFrame(
        columns=['repo', 'objetivo', 'revision', 'exitoso'])
    for (repo, objetivo, revision), tabla in registro_testmake.groupby(["repo", "objetivo", "revision"]):
        ultimo_registro = get_last_record(tabla)
        renglon_concatenar = {"repo": repo, "objetivo": objetivo,
                              "revision": revision, "exitoso": ultimo_registro.exito}
        registro_ramas = registro_ramas.append(
            renglon_concatenar, ignore_index=True)
    return registro_ramas
