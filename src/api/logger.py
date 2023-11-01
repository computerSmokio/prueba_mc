import logging
import logging.handlers
from api.config import Config
from json import dumps as json_dumps
from pathlib import Path


if Config.ENVIRON != 'test': # pragma: no cover
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
    logfile=Path(Config.LOG_DIR+'/api.log')
    if not logfile.parent.exists():
        try:
            logfile.parent.mkdir()
        except PermissionError:
            raise Exception('Cannot create log folder due to lack of permissions')
    try:
        open(logfile, 'x').close()
    except PermissionError:
        raise Exception('Cannot create log file due to lack of permissions')
    except FileExistsError:
        pass

    fh = logging.FileHandler(Config.LOG_DIR+'/api.log')
    fh.setLevel(log_levels[Config.LOG_LEVEL])
    fh.setFormatter(formatter)
    gLogger.addHandler(fh)

    # Terminal handler
    terminal_handler = logging.StreamHandler()
    terminal_handler.setLevel(log_levels[Config.LOG_LEVEL] if Config.ENVIRON != 'dev' else logging.DEBUG)
    terminal_handler.setFormatter(formatter)
    gLogger.addHandler(terminal_handler)

class LoggerMiddleware(): # pragma: no cover
    def process_response(self, req, resp, resource, req_succeeded):
        """Log the response"""
        log = {
            'host': req.host,
            'method': req.method,
            'path': req.path,
            'status': resp.status,
            'remote_addr': req.remote_addr,
            'user_agent': req.user_agent,
            'Success': req_succeeded
        }
        gLogger.info(json_dumps(log))
        debug_log={
            'query_string': req.query_string,
            'uri_template': req.uri_template,
            'cookies': req.cookies,
            'params': req.params,
            
        }
        gLogger.debug(json_dumps(debug_log))
