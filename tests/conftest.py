from pytest import fixture
from fastapi.testclient import TestClient

from twitchybackend.app import app

@fixture
def httpclient():
    yield TestClient(app)
