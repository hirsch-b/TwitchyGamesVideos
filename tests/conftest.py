from fastapi.testclient import TestClient
from pytest import fixture

from twitchybackend.app import app


@fixture
def httpclient():
    yield TestClient(app)
