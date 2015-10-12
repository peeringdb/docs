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

#### Nested data

Any field ending in the suffix **_set** is a list of objects in a relationship with the parent object, you can expand those lists with the 'depth' parameter as explained below.

The naming schema of the field will always tell you which type of object the set is holding and will correspond with the object's endpoint on the API

    <object_type>_set

So a set called 'net_set' will hold Network objects (api endpoint /net)

Note: unlike GET single, 'depth' here will **ONLY** expand sets, no single relationships will be expanded - this is by design

##### Depth

- 0: dont expand anything (default)
- 1: expand all first level sets to ids
- 2: expand all first level sets to objects

curl:

    curl -X GET https://guest:guest@beta.peeringdb.com/api/OBJ?depth=2
 
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
- \_\_in, value inside set of values (comma separated)

string fields:

- \_\_contains, field value contains this value
- \_\_startswith, field value starts with this value
- \_\_in, value inside set of values (comma separated)

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

#### Nested data

Any field ending in the suffix **_set** is a list of objects in a relationship with the parent object, you can expand those lists with the 'depth' parameter as explained below.

The naming schema of the field will always tell you which type of object the set is holding and will correspond with the object's endpoint on the API

    <object_type>_set

So a set called 'net_set' will hold Network objects (api endpoint /net)

Note: unlike GET multiple, 'depth' here will also expand single relationship in addition to sets. So 'net_id' would get expanded into a network object.

unexpanded:

    { 
      ...
      "net_id" : 1
    }

expanded:
    
    {
      ...
      "net_id" : 1
      "net" : {
         ... network object ...
      }
    }


##### Depth

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


