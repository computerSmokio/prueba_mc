import hug
import json
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

@hug.post('/json', output=hug.output_format.json)
def send_json(body: check_request):
    """Send JSON to the server"""
    id = body['id']
    with open('test-json/{}.json'.format(id), 'a') as f:
        json.dump(body['file'], f)
    return {'message': 'JSON received', 'id': id}