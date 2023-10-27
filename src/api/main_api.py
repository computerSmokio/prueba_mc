import hug
from dotenv import dotenv_values
import json_api
from config import Config

# Load the environment variables and set api config
api = hug.API(__name__).http.base_url=Config.BASE_URL

# merge the json_post.py api this api.
@hug.extend_api('/json')
def json_post():
    return [json_api]

@hug.not_found()
def not_found():
    return {'errors': {'url': 'The API call you tried to make was not defined'}}