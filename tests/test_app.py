from ..api import app
from flask_testing import TestCase
import filecmp


class TestApp(TestCase):
    def create_app(self):
        """Flask knows that is in testing mode"""
        app.config["TESTING"] = True
        app.config["SECRET_KEY"] = "dummy_secret_key"
        return app

    def test_add_new_record(self):
        invalid_analyst = "inspector"
        invalid_token = "f9"
        valid_token = app.config["SECRET_KEY"]
        valid_analyst = "not_inspector"
        a_new_row_was_not_added = not self._was_added_a_new_row(invalid_analyst, invalid_token)
        assert a_new_row_was_not_added
        a_new_row_was_not_added = not self._was_added_a_new_row(invalid_analyst, valid_token)
        assert a_new_row_was_not_added
        a_new_row_was_not_added = not self._was_added_a_new_row(valid_analyst, invalid_token)
        assert a_new_row_was_not_added
        a_new_row_was_added = self._was_added_a_new_row(valid_analyst, valid_token)
        assert a_new_row_was_added

    def test_get_dash(self):
        get_something = self.client.get("/api/v1/dashboard")
        self.assert200(get_something)

    def _was_added_a_new_row(self, analista, token):
        self.client.post(f"/api/v1/records?analista={analista}", headers={"Authorization": token})
        return not filecmp.cmp("data/testmake.header.csv", "data/testmake.log.csv")
