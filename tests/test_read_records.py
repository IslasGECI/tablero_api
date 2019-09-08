from tablero.io import get_last_record_per_revision

from tablero.io.read_records import import_data


def test_count_of_last_record_per_revision():
    registros = get_last_record_per_revision(
        log_name="data/testmake.test.csv")
    count_of_records_expected = 52
    count_of_records_obtained = len(registros.index)
    assert count_of_records_obtained == count_of_records_expected


def test_columns_of_last_record_per_revision():
    registros = get_last_record_per_revision(
        log_name="data/testmake.test.csv")
    columns_of_records_expected = sorted(
        ['repo', 'objetivo', 'revision', 'exitoso'])
    columns_of_records_obtained = sorted(registros)
    assert columns_of_records_obtained == columns_of_records_expected


def test_imported_data():
    registros_importados = import_data(log_name="data/testmake.test.csv")
    assert sum(registros_importados.exito == 0) == 197
    assert sum(registros_importados.exito == 1) == 156
    assert len(registros_importados.exito) == 353
