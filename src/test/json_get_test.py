import hug
from api import main_api
from dotenv import dotenv_values
from conftest import startup_function, teardown_function, endpoint_url

def test_normal_path():
    hug.test.post(main_api, endpoint_url, {'id': 1, 'file': {'name': 'test'}})
    result = hug.test.get(main_api, endpoint_url+'/1')
    assert result.status == hug.HTTP_200
    assert result.data['file']['name'] == 'test'
    
def test_missing_id():
    result = hug.test.get(main_api, endpoint_url+'//')
    assert result.status == hug.HTTP_400
    assert result.data['errors']['id'] == 'Invalid whole number provided'

def test_wrong_id():
    result = hug.test.get(main_api, endpoint_url+'/test')
    assert result.status == hug.HTTP_400
    assert result.data['errors']['id'] == 'Invalid whole number provided'

def test_no_file():
    result = hug.test.get(main_api, endpoint_url+'/666')
    assert result.status == hug.HTTP_404
    assert result.data['errors']['id'] == 'The file with this ID does not exist'

    