import hug
from json import dump as json_dump
from pathlib import Path
from dotenv import dotenv_values


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

# Declare the endpoint
@hug.post('/json', output=hug.output_format.json, versions=1)
def send_json(body: check_request, response):
    """Send JSON to the server"""
    # creates the json & check if the file already exists
    try:
        open('test-json/{}.json'.format(body['id']), 'x')
    except FileExistsError:
        response.status=hug.HTTP_409
        return {'errors': {'body': 'A file with this ID is already exists'}}
    # Write the file
    with open('test-json/{}.json'.format(body['id']), 'w') as f:
        json_dump(body['file'], f)
    return {'message': 'JSON received', 'id': id}

