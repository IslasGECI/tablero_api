from .Dashboard import is_default
from collections import namedtuple

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
