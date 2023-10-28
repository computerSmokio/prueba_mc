
#  JSON API

  

##  Install process

  

    pip install -r requirements/minimal.txt
    hug -f src/api/main_api.py

## API Documentation
------------------------------------------------------------------------------------------

#### Send a JSON file

<details>
 <summary><code>POST</code> <code><b>/BASE_URL/v1/json</b></code> <code>Send a json file for the server to store</code></summary>

##### Body expected
`Content type='application/json'`
> | Key      |  type     | data type               | value description                                                           |
> |-----------|-----------|-------------------------|-----------------------------------------------------------------------|
> | ID      |  required | Number   | it'll be the number that identifies the file in the server  |
> | File     |  required | JSON   | The file to save  |

##### Responses

> | http code     | content-type                      | response                                                            |
> |---------------|-----------------------------------|---------------------------------------------------------------------|
> | `201`         | `application/json;charset=UTF-8`        | `{"message": "JSON received", "id": ?}`                                |
> | `400`         | `application/json;charset=utf-8`                | `{"errors": {"where": "Brief explanation"}}`                            |
> | `409`         | `application/json;charset=utf-8`         | `{"errors": {'body':  'A file with this ID already exists'}`|

##### Example cURL

> ```javascript
>  curl -XPOST -H "Content-type: application/json" -d '{ "id": 1, "file": {}}' 'http://HOST:PORT/BASE_URL/v1/json'
> ```
</details>


#### Retreive a JSON file

<details>
 <summary><code>GET</code> <code><b>/BASE_URL/v1/json/{id}</b></code> <code>retreive the JSON file identified by {id}</code></summary>

##### Parameters expected

> | Key      |  type     | data type               | value description                                                           |
> |-----------|-----------|-------------------------|-----------------------------------------------------------------------|
> | ID      |  required | Number   | the number that identifies the file in the server  |

##### Responses

> | http code     | content-type                      | response                                                            |
> |---------------|-----------------------------------|---------------------------------------------------------------------|
> | `200`         | `application/json;charset=UTF-8`        | `{"file": {file content}}`                                |
> | `400`         | `application/json;charset=utf-8`                | `{"errors": {"where": "Brief explanation"}}`                            |
> | `404`         | `application/json;charset=utf-8`         | `{"errors": {'body':  'The file with this ID does not exist'}`|

##### Example cURL

> ```javascript
>  curl -XGET 'http://HOST:PORT/BASE_URL/v1/json/ID'
> ```
</details>

#### Delete a JSON file

<details>
 <summary><code>DELETE</code> <code><b>/BASE_URL/v1/json/{id}</b></code> <code>Delete the JSON file identified by {id} from the server</code></summary>

##### Parameters expected

> | Key      |  type     | data type               | value description                                                           |
> |-----------|-----------|-------------------------|-----------------------------------------------------------------------|
> | ID      |  required | Number   | the number that identifies the file in the server  |

##### Responses

> | http code     | content-type                      | response                                                            |
> |---------------|-----------------------------------|---------------------------------------------------------------------|
> | `200`         | `application/json;charset=UTF-8`        | `{"message": "JSON deleted", "id": 1}`                                |
> | `400`         | `application/json;charset=utf-8`                | `{"errors": {"where": "Brief explanation"}}`                            |
> | `404`         | `application/json;charset=utf-8`         | `{"errors": {"id": "The file with this ID does not exist"}}`|

##### Example cURL

> ```javascript
>  curl -XDELETE 'http://HOST:PORT/BASE_URL/v1/json/ID'
> ```
</details>

#### Modify a JSON file

<details>
 <summary><code>PUT</code> <code><b>/BASE_URL/v1/json/{id}</b></code> <code>Modify the JSON file identified by {id} from the server</code></summary>

##### Parameters expected

> | Key      |  type     | data type               | value description                                                           |
> |-----------|-----------|-------------------------|-----------------------------------------------------------------------|
> | ID      |  required | Number   | the number that identifies the file in the server  |

##### Body expected
> `Content type='application/json'`

##### Responses

> | http code     | content-type                      | response                                                            |
> |---------------|-----------------------------------|---------------------------------------------------------------------|
> | `200`         | `application/json;charset=UTF-8`        | `{"message": "JSON modified", "id": 3}`                                |
> | `400`         | `application/json;charset=utf-8`                | `{"errors": {"where": "Brief explanation"}}`                            |
> | `404`         | `application/json;charset=utf-8`         | `{"errors": {"id": "The file with this ID does not exist"}}`|

##### Example cURL

> ```javascript
> curl -XPUT -H "Content-type: application/json" -d '{ "new": "content"}' 'http://HOST:PORT/BASE_URL/v1/json/ID'
> ```
</details>

------------------------------------------------------------------------------------------