from os import environ as os_environ
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

class ConfigEnvError(Exception):
    pass


class ConfigEnv:
    """ 
    TAKES ENVIRONMENT VARIABLES FROM .env FILE or FROM OS 
    ACTS AS A SINGLE SOURCE OF TRUTH FOR ENVIRONMENT VARIABLES
    """
# ALL ENVIRONMENT VARIABLES ARE DEFINED HERE
    PORT: int = 8080
    JSON_DIR: str = "data"
    ENVIRON: str = "prod"
    LOG_LEVEL: str = "INFO"
    LOG_DIR: str = "/var/log"

    def __init__(self, env):
        for key in self.__annotations__:
            default=getattr(self, key, None)
            if default is None and key not in env:
                raise ConfigEnvError(f"Missing environment variable {key}")
            if key in env:
                try:
                    if key == "LOG_LEVEL" and env[key] not in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]:
                        raise ConfigEnvError(f"Invalid value for {key}")
                    if self.__annotations__[key] == int:
                        setattr(self, key, int(env[key]))
                    else:
                        setattr(self, key, env[key])
                except ValueError:
                    raise ConfigEnvError(f"Invalid value for {key}")

    def __str__(self):
        return str(self.__dict__)
    def __repr__(self):
        return str(self.__dict__) 
    
Config = ConfigEnv(os_environ)