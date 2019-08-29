from tablero.io import get_last_record_per_revision


def test_count_of_last_record_per_revision():
    registro_ramas = get_last_record_per_revision(
        log_name="data/testmake.test.csv")
    count_of_revisions_expected = 52
    count_of_revisions_obtained = len(registro_ramas.index)
    assert count_of_revisions_obtained == count_of_revisions_expected
