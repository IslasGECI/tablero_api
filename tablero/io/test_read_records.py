from .read_records import get_last_record_per_revision

def test_count_of_last_record_per_revision():
    registro_ramas = get_last_record_per_revision(
        log_name="data/testmake.test.csv")
    length_expected = 52
    length_obtained = len(registro_ramas.index)
    assert length_obtained == length_expected
