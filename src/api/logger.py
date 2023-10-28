import hug
import logging
from config import Config

class GlobalLogger(hug.middleware.LogMiddleware):
    def __init__(self):
        super().__init__()
        f_log_handler = logging.FileHandler('api.log')
        self.logger.setLevel(logging.DEBUG)
        f_log_handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        f_log_handler.setFormatter(formatter)
        self.logger.addHandler(f_log_handler)
    
    def _generate_combined_log(self, request, response):
        """Generate a combined log message for the given request and response"""
        return "{0} - - {1} {2} {3} {4}".format(
            request.remote_addr,
            request.method,
            request.relative_uri,
            response.status,
            request.user_agent,
        )
    
    def process_response(self, request, response, resource, req_succeeded):
        """Log the request and response"""
        self.logger.info(self._generate_combined_log(request, response))
    
    def process_exception(self, request, response, exception):
        """Log the request and exception"""
        self.logger.error(self._generate_combined_log(request, response))
        self.logger.exception(exception)
    
    def process_request(self, request, response):
        """Log the request"""
        self.logger.info(
            'Requested: {0} {1} {2}'.format(
                request.method,
                request.relative_uri,
                request.content_type
            )
        )
    