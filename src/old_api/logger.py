import logging
import logging.handlers
from api.config import Config

# Dict of log levels
log_levels = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "ERROR": logging.ERROR,
    "CRITICAL": logging.CRITICAL
}

# Create a logger
gLogger = logging.getLogger('api')
gLogger.setLevel(log_levels[Config.LOG_LEVEL])
# Format logs
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
# File handler
fh = logging.FileHandler(Config.LOG_DIR+'/api.log')
fh.setLevel(log_levels[Config.LOG_LEVEL])
fh.setFormatter(formatter)
gLogger.addHandler(fh)