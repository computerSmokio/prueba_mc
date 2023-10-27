import hug
from dotenv import dotenv_values
import json_post

# Load the environment variables and set api config
envvars=dotenv_values('.env')
print(envvars)
if envvars and 'BASE_URL' in envvars and envvars['BASE_URL']:
    api = hug.API(__name__).http.base_url=envvars['BASE_URL']

# merge the json_post.py api this api.
@hug.extend_api()
def json_post():
    return [json_post]

