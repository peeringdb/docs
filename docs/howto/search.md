# Get Started with Search in PeeringDB

## Introduction to PeeringDB
PeeringDB is a publicly available network database that is the go-to location for interconnection data. The database facilitates global network connections at Internet Exchange Points (IXPs), data centers, and other interconnection facilities, and it serves as a starting point for interconnection decisions.

This online database is a non-profit, community-driven effort that encourages the exchange of Peering-related information and is totally managed and maintained by volunteers. It's a tool for the Internet's growth and enhancement.

## Why use PeeringDB to search for Networks, Exchange and Data Centers.

There are a number of Autonomous System Numbers (ASNs) known as networks that use PeeringDB to store their interconnection information. Using PeeringDB, you'll be able to access and search for information about other networks requesting interconnection.  If you contribute your own data to PeeringDB it's also possible for them to find out about your own network details. 

There is no need to create an account in order to use the basic search functionality. But if you want to access private contact information and use advanced search features, like radius search, you'll need to sign up for an account.

By using PeeringDB, data centers referred to as Facilities and Internet exchange points (IXs) can increase their visibility to potential and existing customers by adding or updating their records in the database, making it significantly easier for networks to access information about their service.

## How to search for Exchanges, Facilities and Networks in PeeringDB
On the [front page](https://www.peeringdb.com/) of PeeringDB you will see a simple search box which you can use to search for Exchanges, Facilities and Networks that are on PeeringDB by simply entering the desired name on the search. Let’s demonstrate with some examples to see how this works.

### Networks
For this example, we have this network **KENET** which is a non-profit operator for education and research and we want to search for it on PeeringDB. 
There are two ways to search for Networks in PeeringDB:

1. **Name search**

You can search for Networks by using the name of the networks by:
- Entering the name of the network as seen below.
- From the search result, under the Networks section, locate the network you have searched.
- It would be visible if it is in the PeeringDB database.

2. **ASN Search**

You can search for Networks using their ASN number by:
- Entering the name of the network as seen below. For the example below the ASN is (36914).
- From the search result, under the Networks section, locate the network you have searched.

Either of the two methods will get the same search results. 

### Exchanges
For this example, let’s consider this Internet exchange points (IXs) **UNY-IX** which is an open internet exchange located in Universitas Negeri Yogyakarta.
 To search for an exchange:
- Enter the name of the Internet exchange points (IXs) as shown below.
- From the search result, under the Exchanges section, locate the Internet exchange points (IXs) you have searched.

### Facilities
Data centers are also referred to as Facilities. For this example, let’s consider this university **University of Oslo** which is an institution in Oslo
To search for an facilities:
- Enter the name of the Data center or Facilities as shown below.
- From the search result, under the Facilities section, locate the Facility or data center you have searched.


## How to use the Search in PeeringDB extension
The PeeringDB search extension is a free to use Google Chrome extension with which you can use to search for ASNs, Networks, and IXs on PeeringDB.

To get started, go to the [Chrome Web Store](https://chrome.google.com/webstore/detail/search-in-peeringdb/aogffgldgfjelpadabfbcngmndbceiad/related?hl=en) and download the extension, then enable it and add it to your extension bar. There are two ways to use the extension once it has been enabled:

- **Using the Extension Bar Icon**: Click the icon and type your search term into the box. The search will open in a new tab with the search result.
- **Using the Context Menu**: Right-click on any text on a page and select "Search in PeeringDB". The search will open in a new tab with the search result.

If the query or highlighted text contains a number, the extension will attempt to find an ASN. 

## How to search based on a partial name
You can search based on a partial name. When an organization, network, facility or exchange name has two parts, you can search for just the first or second part and then select from all the organizations that share that name. This makes it easier to find the organization you want. This can also be helpful in a situation where you can not remember the name of the organization in full. 

In the example below, we want to search for “internet Archive”. We will search for it with a single part and not with the full name. 
In the search box, input “archive''. This brings out a search result that have similar parts in their names. 

You can now search through the results to find the what you want.

## What is an Advanced search
Advanced search in PeeringDB  lets you explicitly filter searches location, network presence, service level and a wide range of other features. You get the results you’re looking for and can export them in structured data formats (JSON or CSV), so you can import the data into tools that will help you make decisions. 
> **Note**: You need to be logged in to PeeringDB in order to use some of the features of Advanced Search, including the radius search.

Let’s take a look at this example below to demonstrate how advanced search works. We are going to search for an exchange within a particular region.
On the front page of PeeringDB you will see the advanced search box which you can use to search for Exchanges, Facilities and Networks that are on PeeringDB.

- Click on the Advanced search link. This takes you to the Advanced search landing page. The search page shows the Exchanges, Networks, Facilities and organizations tabs. 
- Go to the Exchange tab, in the country field select a country of your choice by scrolling through the different options.
- On the right hand side, in the network presence field, enter the name of the network. You can follow the example shown below and add KENET.
- Click on the drop down list that appears as you input the network name.
- Click on Search.
- Scroll down to view information regarding the exchange that you searched for.
- Click on JSON or CSV to download the information in a structured format.

## Geographic search
As new facilities are created in our database they will be linked to geographic coordinates. PeeringDB has improved search by changing the way it records data for location in its database. You can now search for facilities with a distance radius of a chosen coordinate. 

### How to search for facilities within a given radius
You can search for facilities within a given radius, using the Advanced Search interface. Users can search from a country and city, and select a radius in kilometers or miles. Of course, you can achieve the same results using the API or the web interface, which means you can integrate this feature into your own tools.
> Note: You need to be logged in to PeeringDB in order to search for facilities within a given radius.
- Login in or Register an account on PeeringDB
- On the front page of PeeringDB, click on the Advanced search link
- Go to the Facilities Tab and in the city/postal field add a city or postal of your choice
- In the country field select a country of your choice.
- In the Within Distance field  add a specified distance of your choice 
- On the right hand side of the page, click on search
- Scroll down to view the information you searched for. The search result will bring up facilities which are in that country, city and state.
- You can download your information in a JSON or CSV format.


## Querying with PeeringDB API

Throughout this article up to this point, we have been talking on how to use PeeringDB to find information about potential peers, and then after peering has been arranged, using PeeringDB to obtain the peering details.
The PeeringDB website is very helpful in these regards, but using the website still requires a lot of manual work. It’s also possible to use the PeeringDB API to automate some parts of this. Why use the PeeringDB API? _PeeringDB API makes it easy to integrate PeeringDB in your environment_

The PeeringDB database can be queried using a REST API. REST allows a client to request information from a server over HTTP or HTTPS. The server then returns the requested information in JSON format.


## Object Types
Each object has an associated shorthand tag you can use. Object types are not case sensitive and the output is an array.
For example: https://peeringdb.com/api/OBJ. The endpoint is: `/api/OBJ`.

Below are the categories of objects types(OBJ) in PeeringDB
- **Basic Objects**: org, fac, ix, net, poc 
- **Derived Objects**: ixlan, ixpfx, netixlan, netfac

