import hug
from api import main_api
from dotenv import dotenv_values
from conftest import startup_function, teardown_function, endpoint_url, base_dir


def test_normal_path():
    result = hug.test.post(main_api, endpoint_url, {'id': 1, 'file': {'name': 'test'}})
    print(result)
    assert result.status == hug.HTTP_201
    assert result.data['message'] == 'JSON received'
    with open('{}/1.json'.format(base_dir), 'r') as f:
        assert f.read() == '{"name": "test"}'

def test_missing_id():
    result = hug.test.post(main_api, endpoint_url, {'file': {'name': 'test'}})
    assert result.status == hug.HTTP_400
    assert result.data['errors']['body'] == 'The ID key is missing'

def test_missing_file():
    result = hug.test.post(main_api, endpoint_url, {'id': 1})
    assert result.status == hug.HTTP_400
    assert result.data['errors']['body'] == 'The file key is missing'

def test_empty_id():
    result = hug.test.post(main_api, endpoint_url, {'id': '', 'file': {'name': 'test'}})
    assert result.status == hug.HTTP_400
    assert result.data['errors']['body'] == 'The ID must be a number'

def test_empty_file():
    result = hug.test.post(main_api, endpoint_url, {'id': 1, 'file': ''})
    assert result.status == hug.HTTP_400
    assert result.data['errors']['body'] == 'The file must be a JSON'

def test_wrong_id():
    result = hug.test.post(main_api, endpoint_url, {'id': 'test', 'file': {'name': 'test'}})
    assert result.status == hug.HTTP_400
    assert result.data['errors']['body'] == 'The ID must be a number'

def test_no_json_file():
    result = hug.test.post(main_api, endpoint_url, {'id': 1, 'file': '{"name": "test}'})
    assert result.status == hug.HTTP_400
    assert result.data['errors']['body'] == 'The file must be a JSON'

def test_used_id():
    hug.test.post(main_api, endpoint_url, {'id': 3, 'file': {'name': 'test'}})
    result = hug.test.post(main_api, endpoint_url, {'id': 3, 'file': {'name': 'test'}})
    assert result.status == hug.HTTP_409
    assert result.data['errors']['body'] == 'A file with this ID already exists'

