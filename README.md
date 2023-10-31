
#  JSON API

##  Install process

#### Install dependencies
        pip install -r requirements/{minimal|dev}.txt

#### if want to compile to cython
You need to install the dev requirements or minimal + Cython

        python3 src/setup.py build_ext --inplace
 
#### Start the server

        python3 {src|build}/main.py

------------------------------------------------------------------------------------------

## Environment Variables

| Name | Type | Required | Values | Default |
|--|--|--|--|--| 
| ENVIRON | str | :x: | 'dev\|prod' | prod |
| PORT | int | :x: | 1 to 65535 | 8080 |
| JSON_DIR | str | :x: | 'path/for/data' | data |
| LOG_LEVEL | str | :x: | DEBUG\|INFO\|ERROR\|CRITICAL\|WARNING | INFO |
| LOG_DIR | str | :x: | 'path/for/log' | /var/log |