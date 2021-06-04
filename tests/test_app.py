from ..api import app
from flask_testing import TestCase
import filecmp


class TestApp(TestCase):
    def create_app(self):
        """Flask knows that is in testing mode"""
        app.config["TESTING"] = True
        return app

    def test_add_new_record(self):
        self.client.post("/api/v1/records?analista=inspector")
        assert filecmp.cmp("data/testmake.log.tests.csv", "data/testmake.log.csv")
        self.client.post("/api/v1/records?analista=no_inspector")
        assert not filecmp.cmp("data/testmake.log.tests.csv", "data/testmake.log.csv")

    def test_get_dash(self):
        get_something = self.client.get("/api/v1/dashboard")
        self.assert200(get_something)
