def test_heartbeat(httpclient):
    response = httpclient.get("/monitoring/heartbeat")
    assert response.status_code == 200
    assert "now" in response.json()


def test_status(httpclient):
    response = httpclient.get("/monitoring/status")
    assert response.status_code == 200
    body = response.json()
    assert body["mongodb"] is not None
    assert body["redis"] is not None
