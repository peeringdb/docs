# HOWTO: Get Started with API Keys

PeeringDB, as the name suggests, was set up to facilitate peering between networks and peering coordinators. In recent years, the vision of PeeringDB has developed to keep up with the speed and diverse manner in which the Internet is growing. The database is no longer just for peering and peering related information. It now includes all types of interconnection data for networks, clouds, services, and enterprise, as well as interconnection facilities that are developing at the edge of the Internet. We believe in, and rely on the community to grow and improve the PeeringDB database. 

The volunteers who run the database are passionate about security, privacy, integrity, and validation of the data in the database. Even though PeeringDB is a freely available and public tool, users strictly adhere to the acceptable use policy, which prevents the database from being used for commercial purposes and discourages unsolicited communications. This is largely policed by the community and has been very effective since PeeringDB was launched.

## API

### What is our API?

An Application Programming Interface (API) is a way for computer software to communicate with other computers software. Our API allows PeeringDB users to query and update PeeringDB programmatically. That means they can automate work instead of using the website.

### What Are API keys?

An API key is a secret token for identifying and authenticating a user. That user can be an individual or an organization. That’s why we support both user and organizational API keys.

PeeringDB offers API keys for authenticating API requests. There are two main forms of API keys:

* User-level 
* Organizational-level

### User-level API keys

These API keys are tied to an individual user account and can be created from the user profile page. 

There are only two permission levels: a normal key will mirror the same permissions of the user, while a readonly key will have read only permissions to all the same namespaces as the user.

!["form to add user api key"](images/user-key-add.png)

### Organization-level API keys

These API keys are created and revoked from the organization admin panel. Each key gets its own custom permissions, which can be modified from the API Key Permissions panel.

Each key must have an email attached to it. This is because keys may be allowed to create and modify data in PeeringDB, and we need a contact to reach out to in case of questions.

You should use an organization-level API key for automation that should not be tied to individual users.

!["api key creation"](images/org-key-added.png)

!["manage organization api key permissions"](images/org-key-permissions.png)

### Copy or write down keys immediately

The full API key string is only ever exposed to the user or organization **at its moment of creation**. If this string is lost, then the user or organization should revoke that key and create and permission a new one.

## Command line example using Python and requests

API keys allow developers to interact with their PeeringDB account programmatically, rather than through the website. Here is an example script in Python. It uses the module Requests to GET data about a particular Facility, and then sends a PUT request to modify that data.

This example assumes we have an environment variable set with our API key. To do that from the command line, we can run:

```sh
export API_KEY="[created api key string]"
```

Then the Python script would look like the following. First we get the API key from the environment:

```py
import os

import requests

API_KEY = os.environ.get("API_KEY")
```

We set the url for the Facility we want to interact with. Note the `/api` in the URL, which signals we are making calls to the REST API.

```py
URL = "https://www.peeringdb.com/api/fac/1"
```

We set the headers to include our API key as authorization. Printing the `headers` variable should allow us to see the API key.

```py
headers = {"Authorization": "Api-Key " + API_KEY}
print(headers)
```

First we make a GET request, to simply get data about example Facility number 1

```py
response = requests.get(URL, headers=headers)
data = response.json()["data"][0]
print(data)
```

Printing this data allows us to see what fields we would like to change. Let's say we decide to change the name of this facility. We overwrite the value for key "name"

```py
data["name"] = "Newly decided name"
```

Then we use a PUT request to send that modified data back to PeeringDB.
Note that this time, we must provide data to the API, using the keyword argument "data"

```py
put_response = requests.put(URL, headers=headers, data=data)
```

We can print the status code to see if our request was successful.

```py
print(put_response.status_code)
```

This will return a code 200 to signal success.

Additionally the content of the request should include data for the now modified Facility

```py
print(put_response.json())
```

Would return a dictionary of the values of the now modified Facility.

## Command line example using curl

API keys provide a cleaner way to authenticate API requests. PeeringDB recommends the command line user creates a API_KEY variable like so

```sh
export API_KEY="[created api key string]"
```
then requests can be made with Curl like in the following examples:

### GET
The following request would return JSON data coresponding to the [ChiX](https://www.peeringdb.com/ix/239) Internet Exchange.

```sh
curl -H "Authorization: Api-Key $API_KEY" -H "Content-Type: application/json" -X GET https://www.peeringdb.com/api/ix/239
```

### POST

The following request would create a new Network under the organization [United IX](https://www.peeringdb.com/org/10843).

```sh
curl -H "Authorization: Api-Key $API_KEY" -H "Content-Type: application/json" -X POST --data "{\""org_id"\":\"10843\", \""name"\":\"Brand New Network\", \""asn"\":\"63311\"}" https://www.peeringdb.com/api/net
```

### PUT

The following request would update the data about a particular Network, [ChIX Route Servers](https://www.peeringdb.com/net/7889), in particular changing the name to "Edited Name".

```sh
curl -H "Authorization: Api-Key $API_KEY" -H "Content-Type: application/json" -X PUT --data "{\""org_id"\":\"10843\", \""name"\":\"Edited Name\", \""asn"\":\"33713\"}" https://www.peeringdb.com/api/net/7889
```

### DELETE
The following request would delete the [ChiX](https://www.peeringdb.com/ix/239) Internet Exchange. The API key holder would need delete privileges to that particular Exchange.

```sh
curl -H "Authorization: Api-Key $API_KEY" -H "Content-Type: application/json" -X DELETE https://www.peeringdb.com/api/ix/239
```
