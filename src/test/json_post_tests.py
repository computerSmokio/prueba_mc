import hug
import main_api
from dotenv import dotenv_values

envvars=dotenv_values('.env')
BASE_URL= envvars['BASE_URL'] if envvars and 'BASE_URL' in envvars else ""
VERSION=envvars['VERSION'] if envvars and 'VERSION' in envvars else "v1"

endpoint_url = '{}/{}/json'.format(BASE_URL, VERSION)

def test_normal_path():
    result = hug.test.post(main_api, endpoint_url, {'id': 1, 'file': {'name': 'test'}})
    assert result.status == hug.HTTP_200
    assert result.data['message'] == 'JSON received'

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
    assert result.data['errors']['body'] == 'A file with this ID is already exists'