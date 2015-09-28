# RESTful API Endpoints and Specifications

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
    - depth `int` nested sets will be loaded (slow)
    - fields `str` comma separated list of field names - only matching fields will be returned in the data
    - [field_name] `int|string` queries for fields with matching value

returns
:   array of objects

HTTP:

    GET /api/OBJ

curl:

    curl -X GET https://guest:guest@beta.peeringdb.com/api/OBJ

#### Depth

- 0: dont expand anything (default)
- 1: expand all first level sets to ids
- 2: expand all first level sets to objects
 
#### Querying examples

exact:

    curl -X GET https://guest:guest@beta.peeringdb.com/api/OBJ?name=something

modifier:

    curl -X GET https://guest:guest@beta.peeringdb.com/api/OBJ?name__contains=something

#### Querying modifiers

numeric fields:
    
- \_\_lt, less than
- \_\_lte, less than equal
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

optional URL parameters
:    

  1. depth `int` nested sets and objects will be expanded 
  2. fields `str` comma separated list of field names - only matching fields will be returned in the data

returns
:   single object in an array

HTTP:

    GET /api/OBJ/42

curl:

    curl -H "Accept: application/json" -X GET https://guest:guest@beta.peeringdb.com/api/OBJ/42

#### Depth
     
- 0: dont expand anything (default)
- 1 to 4: expand all sets and related objects according to level of depth specified

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


