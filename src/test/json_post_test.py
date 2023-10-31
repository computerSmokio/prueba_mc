from conftest import setup_function, teardown_function, endpoint_url, base_dir, client
from falcon import HTTP_201, HTTP_400, HTTP_409

def test_normal_path(client):
    result = client.simulate_post(path=endpoint_url, json={'id': 1, 'file': {'name': 'test'}})
    assert result.status == HTTP_201
    assert result.json['message'] == 'JSON received'
    with open('{}/1.json'.format(base_dir), 'r') as f:
        assert f.read() == '{"name": "test"}'

def test_missing_id(client):
    result = client.simulate_post(path=endpoint_url, json={'file': {'name': 'test'}})
    assert result.status == HTTP_400
    assert result.json['title'] == 'Missing ID field'

def test_missing_file(client):
    result = client.simulate_post(path=endpoint_url, json={'id': 1})
    assert result.status == HTTP_400
    assert result.json['title'] == 'Missing file field'

def test_empty_id(client):
    result = client.simulate_post(path=endpoint_url, json={'id': '', 'file': {'name': 'test'}})
    assert result.status == HTTP_400
    assert result.json['title'] == 'Invalid ID'

def test_wrong_id(client):
    result = client.simulate_post(path=endpoint_url, json={'id': 'test', 'file': {'name': 'test'}})
    assert result.status == HTTP_400
    assert result.json['title'] == 'Invalid ID'


def test_used_id(client):
    client.simulate_post(path=endpoint_url, json={'id': 3, 'file': {'name': 'test'}})
    result = client.simulate_post(path=endpoint_url, json={'id': 3, 'file': {'name': 'test'}})
    assert result.status == HTTP_409
    assert result.json['title'] == 'File already exists'

