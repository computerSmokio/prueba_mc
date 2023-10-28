import hug
import json_api
from config import Config
from logger import gLogger

# Create an API
api = hug.API(__name__)
api.http.base_url=Config.BASE_URL

# merge the json_api.py api this api.
@hug.extend_api('/json')
def json_post():
    return [json_api]

# Change 404 default response
@hug.not_found()
def not_found():
    return {'errors': {'url': 'The API call you tried to make was not defined'}}

# Add logger middleware
gMLogger = hug.middleware.LogMiddleware(gLogger)
api.http.add_middleware(gMLogger)

gLogger.debug(f"Config: {Config}")
gLogger.info(f"API started on {Config.PORT}:{Config.BASE_URL}")
hug.API(__name__).http.serve(display_intro=False, no_documentation=True, port=Config.PORT)
