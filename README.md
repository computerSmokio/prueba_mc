
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

------------------------------------------------------------------------------------------
https://stackedit.io/app#