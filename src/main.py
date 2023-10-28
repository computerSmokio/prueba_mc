from api import main_api
from api.config import Config

if __name__ == '__main__':
    main_api.api.http.serve(no_documentation=True, display_intro=False, port=Config.PORT)
