from os import environ
from fastapi.testclient import TestClient
from pytest import fixture


@fixture
def httpclient():
    from twitchybackend.app import app, mongodb
    db_name = mongodb.get_database().name
    assert db_name == environ["MONGODB_DB"]
    mongodb.drop_database(db_name)
    yield TestClient(app)
    mongodb.drop_database(db_name)

environ["PYTESTING"] = "true"
environ["MONGODB_DB"] = "unittesting"
