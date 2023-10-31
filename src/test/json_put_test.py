from conftest import setup_function, teardown_function, endpoint_url, base_dir, client
from falcon import HTTP_200, HTTP_400, HTTP_404

def test_normal_path(client):
    client.simulate_post(path=endpoint_url, json={'id': 1, 'file': {'name': 'test'}})
    result = client.simulate_put(path=endpoint_url+'/1', json={'name': 'test2'})
    assert result.status == HTTP_200
    assert result.json['message'] == 'JSON modified'
    with open('{}/1.json'.format(base_dir), 'r') as f:
        assert f.read() == '{"name": "test2"}'
    
def test_missing_id(client):
    result = client.simulate_put(path=endpoint_url+'//', json={'name': 'test2'})
    assert result.status == HTTP_404

def test_wrong_id(client):
    result = client.simulate_put(path=endpoint_url+'/test', json={'name': 'test2'})
    assert result.status == HTTP_404

def test_no_file(client):
    result = client.simulate_put(path=endpoint_url+'/666', json={'name': 'test2'})
    assert result.status == HTTP_404
    assert result.json['title'] == 'File not found'
