from ..api import app
import flask
from flask_testing import TestCase
import filecmp


class Request:
    def __init__(self):
        self.arg = {"analista": "inspector", "repo": "repo_1"}


def test_add_new_record(mocker):
    request = Request()
    post = app.post("/api/v1/records", data=dict(analista="inspecto", repo="repo_1"))
    print(post)
    app.get("/api/v1/records", query_string=dict(arg1="data1", arg2="data2"))
    with app.test_request_context("/?analista=inspecto"):
        assert flask.request.args["analista"] == "inspecto"


class TestApp(TestCase):
    def create_app(self):
        """Flask knows that is in testing mode"""
        app.config["TESTING"] = True

        return app

    def test_add_new_record(self):
        request = Request()
        post = self.client.post("/api/v1/records?analista=inspector")
        self.assert200(post)
        assert filecmp.cmp("data/testmake.log.tests.csv", "data/testmake.log.csv")

    def test_get_dash(self):
        get_something = self.client.get("/api/v1/dashboard")
        self.assert200(get_something)
