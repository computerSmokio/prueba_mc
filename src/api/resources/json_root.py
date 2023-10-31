from json import dump as json_dump, load as json_load
from falcon import HTTPBadRequest, HTTPConflict, HTTPInternalServerError, HTTPNotFound, HTTP_201
from api.config import Config
from api.logger import gLogger


def process_json(raw_body):
    """Process the json body to check if it's valid"""
    # Check json body has required fields
    gLogger.debug(f'Checking json body {raw_body}')
    if 'id' not in raw_body:
        raise HTTPBadRequest(
            'Missing ID field',
            'An ID must be submitted in the request body.')
    if raw_body['id'] == '' or not isinstance(raw_body['id'], int):
        raise HTTPBadRequest(
            'Invalid ID',
            'The ID must be a non-empty integer.')
    if 'file' not in raw_body or raw_body['file'] == '':
        raise HTTPBadRequest(
            'Missing file field',
            'A file must be submitted in the request body.')
    return raw_body

class Json_root():
    def on_post(self, req, resp):
        """Send JSON to the server"""
        raw_body=req.media
        processed_body=process_json(raw_body)
        try:
            open('{}/{}.json'.format(Config.JSON_DIR, processed_body['id']), 'x')
        except FileExistsError:
            raise HTTPConflict(
                title='File already exists',
                description='A file with this ID already exists')
        except PermissionError:
            raise HTTPInternalServerError(
                title='Permission error',
                description='The file cannot be created'
            )
        # Write the file
        with open('{}/{}.json'.format(Config.JSON_DIR, processed_body['id']), 'w') as f:
            json_dump(processed_body['file'], f)
        resp.status=HTTP_201
        resp.media={'message': 'JSON received', 'id': processed_body['id']}
