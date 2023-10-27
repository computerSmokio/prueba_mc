import os
from dotenv import load_dotenv

class ConfigEnvError(Exception):
    pass

class ConfigEnv:
    """ TAKES ENVIRONMENT VARIABLES FROM .env FILE or FROM OS 
        ACTS AS A SINGLE SOURCE OF TRUTH FOR ENVIRONMENT VARIABLES
    """
    BASE_URL: str = ""
    VERSION: str = "v1"
    JSON_DIR: str = "test-json"

    def __init__(self, env):
        for key in self.__annotations__:
            default=getattr(self, key, None)
            if default is None and key not in env:
                raise ConfigEnvError(f"Missing environment variable {key}")
            if key in env:
                try:
                    setattr(self, key, env[key])
                except ValueError:
                    raise ConfigEnvError(f"Invalid value for {key}")

    def __str__(self):
        return str(self.__dict__)
    def __repr__(self):
        return str(self.__dict__) 
    
Config = ConfigEnv(os.environ)