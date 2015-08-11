# RESTful API Endpoints and Specifications

!!! Warning
    Currently only **read** operations are enabled

## Requests

#### URL

:   The URL base appended with `/api/`, append with object type and optionally object primary key

    Object type is not case sensitive.

    For example:

    - https://beta.peeringdb.com/api/`OBJ`/`id`


#### Encoding

:   To specify the output format, either use the `Accept:` HTTP header

        Accept: application/json

    Or use extension `type`

        https://beta.peeringdb.com/api/network/42.json

JSON

:   all returns fit into object:

        {
        meta:
          {
          status:
          message:
          }
        data:
          [
          {},
          {}
          ]
        }

    - meta are optional
    - data always array 

    !!! Note
        Please let us know what serializers you'd like to see

#### Authentication

- Basic HTTP authorization

## Operations
### GET: multiple objects

endpoint: GET /api/`OBJ`

optional URL parameters
:   

    - limit `int` limits rows in the result set
    - skip `int` skips n rows in the result set
    - [field_name] `int|string` queries for fields with matching value

returns
:   array of objects

HTTP:

    GET /api/OBJ

curl:

    curl -X GET https://guest:guest@beta.peeringdb.com/api/OBJ

#### Querying examples

exact:

    curl -X GET https://guest:guest@beta.peeringdb.com/api/OBJ?name=something

modifier:

    curl -X GET https://guest:guest@beta.peeringdb.com/api/OBJ?name__contains=something

#### Querying modifiers

numeric fields:
    
- \_\_lt, less than
- \_\_lte, less than eqal
- \_\_gt, greater than
- \_\_gte, greater than equal

string fields:

- \_\_contains, field value contains this value
- \_\_startswith, field value starts with this value

### GET: single object

endpoint: GET /api/`OBJ`/`id`

required URL parameters
:   

  1. id `int`

returns
:   single object in an array

HTTP:

    GET /api/OBJ/42

curl:

    curl -H "Accept: application/json" -X GET https://guest:guest@beta.peeringdb.com/api/OBJ/42


### POST: create new object

endpoint: POST /api/`OBJ`

required URL parameters
:    

    - id `int`
    - fields to post in either JSON obj "{}" or urlencoded field=value

curl:

    curl  -H "Accept: application/json" -X POST --data "{\""state"\":\"active\"}" https://guest:guest@beta.peeringdb.com/api/OBJ


### PUT: edit object

endpoint: PUT /api/`OBJ`/`id`

required URL parameters
:    

    - id `int`
    - fields to post in either JSON obj "{}" or urlencoded field=value

HTTP:

    PUT /api/OBJ/42

curl:

    curl  -H "Accept: application/json" -X PUT --data "{\""state"\":\"active\"}" https://guest:guest@beta.peeringdb.com/api/OBJ/42

### DELETE: delete object

endpoint: DELETE /api/`OBJ`/`id`

required URL parameters
:    

    - id `int`

HTTP:

    DELETE /api/OBJ/42

curl:

    curl -H "Accept: application/json" -X DELETE https://guest:guest@beta.peeringdb.com/api/OBJ/42


