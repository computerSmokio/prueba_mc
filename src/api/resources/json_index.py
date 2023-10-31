from json import load as json_load, dump as json_dump
from pathlib import Path
from falcon import HTTPNotFound, HTTPInternalServerError, HTTPBadRequest
from api.config import Config

class Json_index():
    def on_get(self, req, res, id_file:int):
        """Get JSON from the server"""
        try:
            with open('{}/{}.json'.format(Config.JSON_DIR, id_file), 'r') as f:
                res.media={'file': json_load(f)}
        except FileNotFoundError:
            raise HTTPNotFound(
                title='File not found',
                description='The file with this ID does not exist')
        except PermissionError: # pragma: no cover
            raise HTTPInternalServerError(
                title='Permission error',
                description='The file with this ID cannot be read'
            )

    def on_delete(self, req, res, id_file:int):
        """Delete JSON from the server"""
        try:
            open('{}/{}.json'.format(Config.JSON_DIR, id_file), 'r')
        except FileNotFoundError:
            raise HTTPNotFound(
                title='File not found',
                description='The file with this ID does not exist')
        try:
            Path('{}/{}.json'.format(Config.JSON_DIR, id_file)).unlink()
        except PermissionError: # pragma: no cover
            raise HTTPInternalServerError(
                title='Permission error',
                description='The file with this ID cannot be deleted'
            )
    
        res.media={'message': 'JSON deleted', 'id': id_file}
    
    def on_put(self, req, res, id_file:int):
        """Modify JSON from the server"""
        # Check if the file exists
        try:
            open('{}/{}.json'.format(Config.JSON_DIR, id_file), 'r')
        except FileNotFoundError:
            raise HTTPNotFound(
                title='File not found',
                description='The file with this ID does not exist'
            )
        except PermissionError: # pragma: no cover
            raise HTTPInternalServerError( 
                title='Permission error',
                description='The file with this ID cannot be modified'
            )
        # Get the body
        raw_body=req.media
        # Write the file
        try:
            with open('{}/{}.json'.format(Config.JSON_DIR, id_file), 'w') as f:
                json_dump(raw_body, f)
        except PermissionError: # pragma: no cover
            raise HTTPInternalServerError(
                title='Permission error',
                description='The file with this ID cannot be modified'
            )
        except ValueError:
            raise HTTPBadRequest(
                'Invalid file',
                'The body must be a json file.'
            )
        res.media={'message': 'JSON modified', 'id': id_file}