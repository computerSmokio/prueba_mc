import hug
import json_api
from config import Config
from logger import GlobalLogger as gLogger
# Load the environment variables and set api config
api = hug.API(__name__)
api.http.base_url=Config.BASE_URL

# merge the json_api.py api this api.
@hug.extend_api('/json')
def json_post():
    return [json_api]

@hug.not_found()
def not_found():
    return {'errors': {'url': 'The API call you tried to make was not defined'}}
api.http.add_middleware(gLogger())
#gLogger.logger.debug(f"Config: {Config}")
#gLogger.logger.info(f"API started on {Config.BASE_URL}")
hug.API(__name__).http.serve(display_intro=False, no_documentation=True, port=Config.PORT)
