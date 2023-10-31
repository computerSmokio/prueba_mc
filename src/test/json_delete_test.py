from conftest import setup_function, teardown_function, endpoint_url
from falcon import HTTP_200, HTTP_404

def test_normal_path(client):
    client.simulate_post(path=endpoint_url, json={'id': 1, 'file': {'name': 'test'}})
    result = client.simulate_delete(path=endpoint_url+'/1')
    assert result.status == HTTP_200
    assert result.json['message'] == 'JSON deleted'

def test_missing_id(client):
    result = client.simulate_delete(path=endpoint_url+'//')
    assert result.status == HTTP_404

def test_wrong_id(client):
    result = client.simulate_delete(path=endpoint_url+'/test')
    assert result.status == HTTP_404

def test_no_file(client):
    result = client.simulate_delete(path=endpoint_url+'/666')
    assert result.status == HTTP_404
    assert result.json['title'] == 'File not found'
