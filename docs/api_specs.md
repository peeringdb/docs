# RESTFul API Endpoints and Specifications

.toc 2

## *NOTE* Currently only read operations are enabled

## Supported Auth Methods

- Basic HTTP authorization

## Requests

**URL**

The URL base appended with `/api/`, appened with object type and optionally object primary key

Object type is case insensitive.

For example:

- https://beta.peeringdb.com/api/*OBJ*/*id*


To specify the output formatting, either use the `Accept:` HTTP header

    Accept: application/json

## Supported Renderers

### JSON

all returns fit into object:

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

- data always array 


## Operations
### GET: multiple objects

endpoint: GET /api/*OBJ*

optional url parameters:

- limit `int` limits rows in the result set
- skip `int` skips n rows in the result set

returns:
  array of objects

example:
    GET /api/ixp

curl:

    curl -X GET https://guest:guest@beta.peeringdb.com/api/OBJ


### GET: single object

enpoint: GET /api/*OBJ*/`id`

required url parameters:

  1. id `int`

returns:
  single object in an array

example:
    GET /api/ixp/42

curl:

    curl -H "Accept: application/json" -X GET https://guest:guest@beta.peeringdb.com/api/OBJ/42


### POST: create new object

endpoint: POST /api/*OBJ*

required url parameters:

  - fields to post in either json obj "{}" or urlencoded field=value

curl:

    curl  -H "Accept: application/json" -X POST --data "{\""state"\":\"active\"}" https://guest:guest@beta.peeringdb.com/api/OBJ


### PUT: edit object

endpoint: PUT /api/*OBJ*/<id>

required parameters:

  - fields to put in either json obj "{}" or urlencoded field=value

curl:

    curl  -H "Accept: application/json" -X PUT --data "{\""state"\":\"active\"}" https://guest:guest@beta.peeringdb.com/api/OBJ/42

### DELETE: delete object

endpoint: DELETE /api/*OBJ*/<id>

required parameters:

  - none

example:

    DELETE /api/ixp/42

curl:

    curl -H "Accept: application/json" -X DELETE https://guest:guest@beta.peeringdb.com/api/OBJ/42

