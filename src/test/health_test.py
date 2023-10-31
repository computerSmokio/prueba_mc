from conftest import client

def test_health(client):
    resp = client.simulate_get('/health')
    assert resp.status == '200 OK'
    assert resp.json == {'message': "it's alive!"}