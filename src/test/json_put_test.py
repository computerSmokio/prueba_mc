import hug
from api import main_api
from dotenv import dotenv_values
import pytest
from conftest import startup_function, teardown_function, endpoint_url, base_dir

def test_normal_path():
    hug.test.post(main_api, endpoint_url, {'id': 1, 'file': {'name': 'test'}})
    result = hug.test.put(main_api, endpoint_url+'/1', {'name': 'test2'})
    assert result.status == hug.HTTP_200
    assert result.data['message'] == 'JSON modified'
    with open('{}/1.json'.format(base_dir), 'r') as f:
        assert f.read() == '{"name": "test2"}'
    
def test_missing_id():
    result = hug.test.put(main_api, endpoint_url+'//', {'name': 'test2'})
    assert result.status == hug.HTTP_400
    assert result.data['errors']['id'] == 'Invalid whole number provided'

def test_wrong_id():
    result = hug.test.put(main_api, endpoint_url+'/test', {'name': 'test2'})
    assert result.status == hug.HTTP_400
    assert result.data['errors']['id'] == 'Invalid whole number provided'

def test_no_file():
    result = hug.test.put(main_api, endpoint_url+'/666', {'name': 'test2'})
    assert result.status == hug.HTTP_404
    assert result.data['errors']['id'] == 'The file with this ID does not exist'
