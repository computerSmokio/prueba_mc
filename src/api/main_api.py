from wsgiref.simple_server import make_server
from api.resources.json_index import Json_index
from api.resources.json_root import Json_root
from api.resources.health import HealthRoot
from api.logger import gLogger, LoggerMiddleware


def setup_routes(app):
    """Setup routes for the app"""
    app.add_route('/health', HealthRoot())
    app.add_route('/json', Json_root())
    app.add_route('/json/{id_file:int}', Json_index())



def create_test():
    from falcon import API as falcon_api
    
    """Create falcon API for testing (it doesn't work with app object for some weird reason)"""
    api = falcon_api(middleware=[LoggerMiddleware()])
    setup_routes(api)
    return api


def create(): # pragma: no cover
    from falcon import App as falcon_app
    from pathlib import Path
    from falcon_swagger_ui import register_swaggerui_app

    """Create falcon app"""
    gLogger.info('Starting server')
    api = falcon_app(middleware=[LoggerMiddleware()])
    setup_routes(api)
    # ADD static files and swagger config
    STATIC_PATH = Path(__file__).parent.parent / 'static'
    api.add_static_route('/static', str(STATIC_PATH))
    register_swaggerui_app(
        app=api,
        swagger_uri='/docs',
        api_url='/static/v1/swagger.json',
        page_title="JSON API DOCS",
        favicon_url='https://falconframework.org/favicon-32x32.png',
        config={'supportedSubmitMethods': ['get'], }
    )
    return api