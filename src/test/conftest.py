# startup and teardown functions
import sys
import os
sys.path.append('src/api')
from config import Config


endpoint_url = '{}/{}/json'.format(Config.BASE_URL, Config.VERSION)
base_dir=Config.JSON_DIR

def startup_function():
    files = os.listdir('test-json')
    for file in files:
        os.remove('test-json/'+file)

def teardown_function():
    files = os.listdir('test-json')
    for file in files:
        os.remove('test-json/'+file)

