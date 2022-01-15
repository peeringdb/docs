# Get Started with Search in PeeringDB

## Introduction to PeeringDB
PeeringDB is a publicly available network database that is the go-to location for interconnection data. The database facilitates global network connections at Internet Exchange Points (IXPs), data centers, and other interconnection facilities, and it serves as a starting point for interconnection decisions.

This online database is a non-profit, community-driven effort that encourages the exchange of Peering-related information and is totally managed and maintained by volunteers. It's a tool for the Internet's growth and enhancement.

## Why use PeeringDB to search for Networks, Exchange and Data Centers.

There are a number of Autonomous System Numbers (ASNs) known as networks that use PeeringDB to store their interconnection information. Using PeeringDB, you'll be able to access and search for information about other networks requesting interconnection.  If you contribute your own data to PeeringDB it's also possible for them to find out about your own network details. 

There is no need to create an account in order to use the basic search functionality. But if you want to access private contact information and use advanced search features, like radius search, you'll need to sign up for an account.

By using PeeringDB, data centers referred to as Facilities and Internet exchange points (IXs) can increase their visibility to potential and existing customers by adding or updating their records in the database, making it significantly easier for networks to access information about their service.

## How to search for Exchanges, Facilities and Networks in PeeringDB
On the [front page](https://www.peeringdb.com/) of PeeringDB, you will see a simple search box which you can use to search for Exchanges, Facilities and Networks that are on PeeringDB by simply entering the desired name on the search. Let’s demonstrate with some examples to see how this works.

### Networks
For this example, we have this network **KENET** which is a non-profit operator for education and research and we want to search for it on PeeringDB. 
There are two ways to search for Networks in PeeringDB:

1. **Name search**

You can search for Networks by using the name of the networks by:
- Entering the name of the network as seen below.
- From the search result, under the Networks section, locate the network you have searched.
- It would be visible if it is in the PeeringDB database.

![name-search](https://github.com/fakela/docs-3/blob/master/docs/howto/images/name-search.png)

2. **ASN Search**

You can search for Networks using their ASN number by:
- Entering the name of the network as seen below. For the example below the ASN is (36914).
- From the search result, under the Networks section, locate the network you have searched.

![asn-search](https://github.com/fakela/docs-3/blob/master/docs/howto/images/asn-search.png)

**Note**: Either of the two methods will get the same search results. 

### Exchanges
For this example, let’s consider this Internet exchange points (IXs) **UNY-IX** which is an open internet exchange located in Universitas Negeri Yogyakarta.
 To search for an exchange:
- Enter the name of the Internet exchange points (IXs) as shown below.
- From the search result, under the Exchanges section, locate the Internet exchange points (IXs) you have searched.

![exchange-search](https://github.com/fakela/docs-3/blob/master/docs/howto/images/exchange-search.png)

### Facilities
Data centers are also referred to as Facilities. For this example, let’s consider this university **University of Oslo** which is an institution in Oslo
To search for an facilities:
- Enter the name of the Data center or Facilities as shown below.
- From the search result, under the Facilities section, locate the Facility or data center you have searched.

![facilites-search](https://github.com/fakela/docs-3/blob/master/docs/howto/images/facilites-search.png)

## How to use the Search in PeeringDB extension
The PeeringDB search extension is a free to use Google Chrome extension with which you can use to search for ASNs, Networks, and IXs on PeeringDB.

![search-extension](https://github.com/fakela/docs-3/blob/master/docs/howto/images/search-extension.png)

To get started, go to the [Chrome Web Store](https://chrome.google.com/webstore/detail/search-in-peeringdb/aogffgldgfjelpadabfbcngmndbceiad/related?hl=en) and download the extension, then enable it and add it to your extension bar. There are two ways to use the extension once it has been enabled:

- **Using the Extension Bar Icon**: Click the icon and type your search term into the box. The search will open in a new tab with the search result.

![extension-search-bar](https://github.com/fakela/docs-3/blob/master/docs/howto/images/extension-bar-icon.png)

Below is the result:

![extension-search-bar-result](https://github.com/fakela/docs-3/blob/master/docs/howto/images/extension-bar-icon-result.png)

- **Using the Context Menu**: Right-click on any text on a page and select "Search in PeeringDB". The search will open in a new tab with the search result.

![extension-context-menu](https://github.com/fakela/docs-3/blob/master/docs/howto/images/context-menu.png)

Below is the result:

![extension-context-menu-result](https://github.com/fakela/docs-3/blob/master/docs/howto/images/context-menu-result.png)

If the query or highlighted text contains a number, the extension will attempt to find an ASN. 

## How to search based on a partial name
You can search based on a partial name. When an organization, network, facility or exchange name has two parts, you can search for just the first or second part and then select from all the organizations that share that name. This makes it easier to find the organization you want. This can also be helpful in a situation where you can not remember the name of the organization in full. 

In the example below, we want to search for “internet archive”. We will search for it with a single part and not with the full name. In the search box, input “archive''. This brings out a search result that have similar parts in their names. 

![partial-name-search](https://github.com/fakela/docs-3/blob/master/docs/howto/images/partial-name-search.png)

You can now search through the results to find the what you want.

## What is an Advanced search
Advanced search in PeeringDB  lets you explicitly filter searches location, network presence, service level and a wide range of other features. You get the results you’re looking for and can export them in structured data formats (JSON or CSV), so you can import the data into tools that will help you make decisions. 

**Note**: You need to be logged in to PeeringDB in order to use some of the features of Advanced Search, including the radius search.

Let’s take a look at this example below to demonstrate how advanced search works. We are going to search for an exchange within a particular region.
On the front page of PeeringDB you will see the advanced search box which you can use to search for Exchanges, Facilities and Networks that are on PeeringDB.

![advanced-search](https://github.com/fakela/docs-3/blob/master/docs/howto/images/advanced-search-link.png)

- Click on the Advanced search link. This takes you to the Advanced search landing page. The search page shows the Exchanges, Networks, Facilities and organizations tabs. 

![advanced-search](https://github.com/fakela/docs-3/blob/master/docs/howto/images/advanced-search-interface.png)

- Go to the Exchange tab, in the country field select a country of your choice by scrolling through the different options.

![advanced-exchange-tab](https://github.com/fakela/docs-3/blob/master/docs/howto/images/advanced-exchange-tab.png)

- On the right hand side, in the network presence field, enter the name of the network. You can follow the example shown below and add KENET.
- Click on the drop down list that appears as you input the network name.

![network-name-dropdown](https://github.com/fakela/docs-3/blob/master/docs/howto/images/network-drop-down.png)

- Click on Search.
- Scroll down to view information regarding the exchange that you searched for.
- Click on JSON or CSV to download the information in a structured format.

![advanced-search-result](https://github.com/fakela/docs-3/blob/master/docs/howto/images/advanced-search-result.png)

## Geographic search
As new facilities are created in our database they will be linked to geographic coordinates. PeeringDB has improved search by changing the way it records data for location in its database. You can now search for facilities with a distance radius of a chosen coordinate. 

### How to search for facilities within a given radius
You can search for facilities within a given radius, using the Advanced Search interface. Users can search from a country and city, and select a radius in kilometers or miles. Of course, you can achieve the same results using the API or the web interface, which means you can integrate this feature into your own tools.

**Note**: You need to be logged in to PeeringDB in order to search for facilities within a given radius.

- Login in or Register an account on PeeringDB
- On the front page of PeeringDB, click on the Advanced search link
- Go to the Facilities Tab and in the city/postal field add a city or postal of your choice
- In the country field select a country of your choice.
- In the Within Distance field  add a specified distance of your choice 
- On the right hand side of the page, click on search
- Scroll down to view the information you searched for. The search result will bring up facilities which are in that country, city and state.
- You can download your information in a JSON or CSV format.

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/FzOUKhJjRRg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Querying with PeeringDB API

Throughout this article up to this point, we have been talking on how to use PeeringDB to find information about potential peers, and then after peering has been arranged, using PeeringDB to obtain the peering details.
The PeeringDB website is very helpful in these regards, but using the website still requires a lot of manual work. It’s also possible to use the PeeringDB API to automate some parts of this. Why use the PeeringDB API? _PeeringDB API makes it easy to integrate PeeringDB in your environment_

The PeeringDB database can be queried using a REST API. REST allows a client to request information from a server over HTTP or HTTPS. The server then returns the requested information in JSON format.


## Object Types
Each object has an associated shorthand tag you can use. Object types are not case sensitive and the output is an array.
For example: [https://peeringdb.com/api/OBJ](https://peeringdb.com/api/OBJ). The endpoint is: `/api/OBJ`.

Below are the categories of objects types(OBJ) in PeeringDB
- **Basic Objects**: org, fac, ix, net, poc 
- **Derived Objects**: ixlan, ixpfx, netixlan, netfac

### Basic Objects
Below is a description of what each of the object types mean and what information they return

- **org**: Root object for fac, ix, net, this holds information about organisation.  
- **fac**: Describes a facility / colocation record, more useful information are in derived records netfac.
- **ix**: Describes an Internet Exchange, more useful information are in derived records ixlan, ixpfx and netixlan.
- **net**: Describes a network / ASN, more useful information are in netfac and netixlan.
- **poc**: Describes various role accounts (point of contact), this is currently only for net objects.
- **as_set**: Array of all AS-SETs corresponding to a network / ASN, this was introduced recently.

### Derived Objects
Below is a description of what each of the object types mean and what information they return.

- **Ixlan**: Describes the LAN of an ix, one ix may have multiple ixlan. This feature may go away with PeeringDB 3.0.
- **ixpfx**: Describes the IP range (IPv4 and IPv6) for an ixlan, one ixlan may have multiple ixpfx.
- **netixlan**: Describes the presence of a network at an IX.
- **netfac**: Describes the presence of a network at a facility.

## Authentication
Authentication is done through basic HTTP authorization. People who are accessing the API as a guest do not need any authentication. For examples:

`curl -sG https://username:password@peeringdb.com/api/poc`

`curl -u username:password https://peeringdb.com/api/poc` 

**Note**: Access to contact information may be restricted if you are using the API as a guest without authentication.

## Making a Request
When making a request, the URL base is added with `/api/`, followed by the object type and, if applicable, the object primary key (if applicable).
For example:`https://peeringdb.com/api/OBJ/id`
If you want to select the output format, either use the Accept: HTTP header or use the extension type parameter.

Accept Header: `Accept: application/json`

Extension type:`https://peeringdb.com/api/network/42.json`

## Operations
Using the GET operation you can retrieve information from the PeeringDB database. You can retrieve both a single object and multiple objects in an array. Let’s look at each of them individually. 

### Single Object
To retrieve a single object you need to use this URL:`https://peeringdb.com/api/OBJ/ID` with this endpoint GET: `/api/OBJ/id`. The ID is a unique identifier and should be added to the URL when retrieving a single object. Let’s look at an example 

HTTP:`GET /api/OBJ/38` where 38 is the ID

curl: `curl -H "Accept: application/json" -X GET https://<username>:<password>@peeringdb.com/api/OBJ/38`

There are optional parameters you can add to your URL
- **str**: which retrieves a comma separated list of field names - only matching fields will be returned in the data.
- **int**: which retrieves two nested sets and objects. 

**Nested sets and objects**: A nested set or object is any field ending in the suffix: set. For example: net_set will hold network objects. The naming schema of the field will always tell you which type of object the set is holding and will correspond with the object's endpoint on the API <object_type>_set. So a set called '_net_set_' will hold Network objects (API endpoint /net)
**Note**: unlike GET multiple, 'depth' here will also expand single relationships in addition to sets. So 'net_id' would get expanded into a network object.

```unexpanded:
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
```
**Depth**
- 0: don't expand anything
- 1 to 4: expand all sets and related objects according to level of depth specified
- 2: it is default

### Multiple Object
To retrieve a single object you need to use this URL: `https://peeringdb.com/api/OBJ/` with this endpoint GET: `/api/OBJ/`. Let’s look at an example 

HTTP: `GET /api/OBJ/` which is the endpoint 

curl: `curl -X GET https://<username>:<password>@peeringdb.com/api/OBJ`

There are optional parameters you can add to your URL
- **limit** int limits rows in the result set
- **skip** int skips n rows in the result set
- **depth** int nested sets will be loaded (slow)
- **fields** str comma separated list of field names - only matching fields will be returned in the data
- **since** int retrieve all objects updated since specified time (unix timestamp, seconds)
- **[field_name]** int|string queries for fields with matching value

## Real world use cases
We will show you different usecases on how to use the PeeringDB API

## How do I query by ASN?
To query this ASN (asn=42) using PeeringDB API, you will need to use this URL
GET `https://peeringdb.com/api/net?asn=42`
Where `asn=42` is the query parameter. 

### Using Curl
Using Curl example to get this specific network. Copy and paste the following to your command line interface.
```
curl GET https://peeringdb.com/api/net/42
```

### Using Python 
To make use of this python code, first, you’ll have to first install [python](https://www.python.org/downloads/) if you don’t have it installed. Then, install [pip](https://pip.pypa.io/en/stable/cli/pip_install/) and [requests](https://docs.python-requests.org/en/latest/user/install/). After that create a python file and copy and paste the following code. 

```
import requests
r = requests.get('https://peeringdb.com/api/net?asn=42')
print(r.text)
 
with open('output.csv', 'w+') as f:
    f.write(r.text)
  ```
   
From the above code, we make a request to the API using the request module and print out the response which would be in a JSON format.However, reading a JSON file can be quite hectic and tasking so we convert the JSON file to a CSV file. Our CSV file will open in output.csv. 


### Using Jq
You can use Jq to make a request to your API and get your output in a CSV format
First, you need to install [Jq](https://stedolan.github.io/jq/download/) in your system.

Next, we use this curl command to prepare our JSON file. Cd to a directory and copy and paste this code on your terminal

```
curl https://peeringdb.com/api/net?asn=42 > test.json

```
This creates a new file named test.json To convert input JSON file to the CSV format, copy and paste the following code on your terminal.

```
jq -r '(.data[0] | keys_unsorted), (.data[] | to_entries | map(.value))|@csv' test.json
```

### Using online converter 
Alternatively you can use an online tool such as [https://www.convertcsv.com/json-to-csv.htm](https://www.convertcsv.com/json-to-csv.htm) to convert the raw json file to csv.

**Note**: For the purpose of this article we will focus on the python method but you can conveniently try out the other proposed methods.

## How to get all the objects owned by [https://www.peeringdb.com/net/961](https://www.peeringdb.com/net/961) and convert the data to CSV?

To get all the objects owned by this https://www.peeringdb.com/net/961 using the PeeringDB API. Copy and paste the following to your command line interface.
```
curl GET https://www.peeringdb.com/net/961
```

## I want the list of networks and their 'type' peering at MICE in Minneapolis
To get the list of networks and their type peering at Mice in Minneapolis, copy and paste the following code in your terminal
```
 curl -s -X GET https://www.peeringdb.com/api/net?ix=446&__in=Minneapolis | jq '.data[] 
```
## How to find all the ixps where my org has a presence.
Using Curl example. Copy and paste the following to your command line interface.
```
 curl -s -X GET https://www.peeringdb.com/api/netixlan\?ixlan_id=62 | jq '.data[]'
```
