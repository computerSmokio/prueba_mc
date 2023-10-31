from api.config import Config
from api.logger import gLogger
from api.main_api import create as create_api
from wsgiref.simple_server import make_server

if __name__ == '__main__':
    with make_server('', Config.PORT, create_api()) as server:
        gLogger.info('Server started')
        server.serve_forever() 