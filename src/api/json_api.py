import hug
from json import dump as json_dump
from pathlib import Path
from dotenv import dotenv_values
from config import Config


# Declare a type to validate request body
@hug.type(extend=hug.types.json)
def check_request(request):
    """Check the request"""
    if 'id' not in request:
        raise ValueError('The ID key is missing')
    if 'file' not in request:
        raise ValueError('The file key is missing')
    if request['id'] == '' or not isinstance(request['id'], (int, float)) :
        raise ValueError('The ID must be a number')
    try:
        hug.types.json(request['file'])
    except ValueError:
        raise ValueError('The file must be a JSON')
    return request


# Declare post json endpoint
@hug.post('/', output=hug.output_format.json, versions=1)
def send_json(body: check_request, response):
    """Send JSON to the server"""
    # creates the json & check if the file already exists
    id = body['id']
    try:
        open('{}/{}.json'.format(Config.JSON_DIR, id), 'x')
    except FileExistsError:
        response.status=hug.HTTP_409
        return {'errors': {'body': 'A file with this ID already exists'}}
    # Write the file
    with open('{}/{}.json'.format(Config.JSON_DIR, id), 'w') as f:
        json_dump(body['file'], f)
    response.status=hug.HTTP_201
    return {'message': 'JSON received', 'id': id}


# Declare get json by id endpoint
@hug.get('/{id}', output=hug.output_format.json, versions=1)
def get_json(id: hug.types.number, response):
    """Get JSON from the server"""
    try:
        with open('{}/{}.json'.format(Config.JSON_DIR, id), 'r') as f:
            return {'file': hug.types.json(f.read())}
    except FileNotFoundError:
        response.status=hug.HTTP_404
        return {'errors': {'id': 'The file with this ID does not exist'}}


# Declare delete json by id endpoint
@hug.delete('/{id}', output=hug.output_format.json, versions=1)
def delete_json(id: hug.types.number, response):
    """Delete JSON from the server"""
    try:
        Path('{}/{}.json'.format(Config.JSON_DIR, id)).unlink()
    except FileNotFoundError:
        response.status=hug.HTTP_404
        return {'errors': {'id': 'The file with this ID does not exist'}}
    return {'message': 'JSON deleted', 'id': id}


# Declare modify json by id endpoint
@hug.put('/{id}', output=hug.output_format.json, versions=1)
def modify_json(body: hug.types.json, id:hug.types.number, response):
    """Modify JSON from the server"""
    # Check if the file exists
    try:
        open('{}/{}.json'.format(Config.JSON_DIR, id), 'r')
    except FileNotFoundError:
        response.status=hug.HTTP_404
        return {'errors': {'id': 'The file with this ID does not exist'}}
    # Write the file
    with open('{}/{}.json'.format(Config.JSON_DIR, id), 'w') as f:
        json_dump(body, f)
    return {'message': 'JSON modified', 'id': id}


