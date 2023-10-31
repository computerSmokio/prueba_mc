# startup and teardown functions
import sys
import os
sys.path.append('src')
from api.config import Config
from api.main_api import create_test
from falcon import testing
import pytest


endpoint_url = '{}/json'.format(Config.BASE_URL)
base_dir=Config.JSON_DIR

@pytest.fixture()
def client():
    return testing.TestClient(create_test())

def setup_function():
    files = os.listdir(base_dir)
    for file in files:
        os.remove(base_dir+'/'+file)

def teardown_function():
    files = os.listdir(base_dir)
    for file in files:
        os.remove(base_dir+'/'+file)

