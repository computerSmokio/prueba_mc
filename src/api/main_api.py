from wsgiref.simple_server import make_server
from api.resources.json_index import Json_index
from api.resources.json_root import Json_root
from api.logger import gLogger, LoggerMiddleware
from api.config import Config

def create_test():
    from falcon import API as falcon_api
    """Create falcon API for testing (it doesn't work with app object for some weird reason)"""
    api = falcon_api(middleware=[LoggerMiddleware()])
    api.add_route('/json', Json_root())
    api.add_route('/json/{id_file:int}', Json_index())
    return api

def create(): # pragma: no cover
    from falcon import App as falcon_app
    """Create falcon app"""
    gLogger.info('Starting server')
    api = falcon_app(middleware=[LoggerMiddleware()])
    api.add_route('/json', Json_root())
    api.add_route('/json/{id_file:int}', Json_index())
    return api