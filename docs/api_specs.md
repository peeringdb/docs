<A name="toc1-0" title="RESTFul API Endpoints and Specifications" />
# RESTFul API Endpoints and Specifications


**<a href="#toc2-5">*NOTE* Currently only read operations are enabled</a>**

**<a href="#toc2-8">Supported Auth Methods</a>**

**<a href="#toc2-13">Requests</a>**

**<a href="#toc2-31">Supported Renderers</a>**
&emsp;<a href="#toc3-34">JSON</a>

**<a href="#toc2-55">Operations</a>**
&emsp;<a href="#toc3-57">GET: multiple objects</a>
&emsp;<a href="#toc3-78">GET: single object</a>
&emsp;<a href="#toc3-98">POST: create new object</a>
&emsp;<a href="#toc3-112">PUT: edit object</a>
&emsp;<a href="#toc3-125">DELETE: delete object</a>

<A name="toc2-5" title="*NOTE* Currently only read operations are enabled" />
## *NOTE* Currently only read operations are enabled

<A name="toc2-8" title="Supported Auth Methods" />
## Supported Auth Methods

- Basic HTTP authorization

<A name="toc2-13" title="Requests" />
## Requests

**URL**

The URL base appended with `/api/`, appened with object type and optionally object primary key

Object type is case insensitive.

For example:

- https://beta.peeringdb.com/api/*OBJ*/*id*


To specify the output formatting, either use the `Accept:` HTTP header

    Accept: application/json

<A name="toc2-31" title="Supported Renderers" />
## Supported Renderers

<A name="toc3-34" title="JSON" />
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


<A name="toc2-55" title="Operations" />
## Operations
<A name="toc3-57" title="GET: multiple objects" />
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


<A name="toc3-78" title="GET: single object" />
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


<A name="toc3-98" title="POST: create new object" />
### POST: create new object

endpoint: POST /api/*OBJ*

required url parameters:

  - fields to post in either json obj "{}" or urlencoded field=value

curl:

    curl  -H "Accept: application/json" -X POST --data "{\""state"\":\"active\"}" https://guest:guest@beta.peeringdb.com/api/OBJ


<A name="toc3-112" title="PUT: edit object" />
### PUT: edit object

endpoint: PUT /api/*OBJ*/<id>

required parameters:

  - fields to put in either json obj "{}" or urlencoded field=value

curl:

    curl  -H "Accept: application/json" -X PUT --data "{\""state"\":\"active\"}" https://guest:guest@beta.peeringdb.com/api/OBJ/42

<A name="toc3-125" title="DELETE: delete object" />
### DELETE: delete object

endpoint: DELETE /api/*OBJ*/<id>

required parameters:

  - none

example:

    DELETE /api/ixp/42

curl:

    curl -H "Accept: application/json" -X DELETE https://guest:guest@beta.peeringdb.com/api/OBJ/42

