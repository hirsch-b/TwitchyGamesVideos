def test_heartbeat(httpclient):
    response = httpclient.get("/monitoring/heartbeat")
    assert response.status_code == 200
    assert "now" in response.json()
