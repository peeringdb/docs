# HOWTO: Get Started with PeeringDB as a Facility (and Campus) Operator 

## About PeeringDB
PeeringDB, as the name suggests, was set up to facilitate peering between networks and peering coordinators. In recent years, the vision of PeeringDB has developed to keep up with the speed and diverse manner in which the Internet is growing. The database is no longer just for peering and peering related information. It now includes all types of interconnection data for networks, clouds, services, and enterprise, as well as interconnection facilities that are developing at the edge of the Internet.

We believe in, and rely on the community to grow and improve the PeeringDB database. The volunteers who run the database are passionate about security, privacy, integrity, and validation of the data in the database. Even though PeeringDB is a freely available and public tool, users strictly adhere to the acceptable use policy, which prevents the database from being used for commercial purposes and discourages unsolicited communications. This is largely policed by the community and has been very effective since PeeringDB was launched.

## Why?
PeeringDB is the interconnection database. Registering information about your facility in PeeringDB makes it visible to network operators who want to connect to exchanges or other networks in your facility. 

## Getting Started
Routine use of PeeringDB can be automated using [our API](https://www.peeringdb.com/apidocs) but this document is intended to help new facility administrators get started. Facilities are set up using the web interface. Once this is done you can use the API to automate things that change regularly. This document focuses on the key steps for establishing your facility's presence in PeeringDB and assumes you are using the web interface, which is available in 14 languages.

If you need additional help getting started, please contact us at: [support@peeringdb.com](mailto:support@peeringdb.com).

## Information Required
You will need to create several database records, known as objects, to establish your presence in PeeringDB. 

Database objects organize relevant information. Your facility’s current participants can add their presence in your facility, making it attractive to others. Most information is optional but sharing all the relevant information maximizes the benefit you get from listing in PeeringDB. 

You can create your entry with the minimum required data and add and update the information you share over time. To maximize the value of your entry in PeeringDB you’ll probably want to include more than the minimum required information. This information is required:

* Company Name
* Full street address

This information is not required but is useful:

* AKA - If your facility has an alternative name you can show it here to improve visibility in searches
* Long name - If your facility has a long name, you can show it here to improve visibility in searches
* Floor - If your facility does not fill an entire building
* Suite - If your facility does not fill an entire building
* CLLI - this is a location code used in parts of the US telecommunications industry and is most useful to facilities located in the USA
* Notes - this field, which supports [Markdown](https://daringfireball.net/projects/markdown/), can be used to describe the characteristics of your facility that would be most useful to PeeringDB users

You can look at the information shared by other facility managers to work out what your organization should be sharing.

## Database Records to Create
### User
The `org` is the parent for the facility but you will need to start the process by creating a user account. If you use a role account for a PeeringDB user you should update the password when people who had access to the role account leave your organization. If you use a ticketing system, please make sure it does not auto-respond in a way that generates a slew of new tickets.

### Org
The `org` object is your organization’s core record in PeeringDB. All it needs is an organization name but you can add extra value by including information about where your organization is located. You could specify as little as a country name or as much as a full postal address.

Your `org` object will be assigned a numeric identifier, called its `id`. This is what will be referenced by any child facility object.

![Excellent Example Org Object](images/excellent-example-org.png)

### Facility
Once you have created your organization you may add the `facility` object. You do this by using the Add Facility tab in the “Manage” menu below your organization.

![Excellent Example Facility Object](images/excellent-example-fac.png)

### Campus
A `campus` is two or more facilities owned by the same organization where customers can get inter-facility cross-connects.

When you have two facilities you can create a `campus` using the Add Campus tab in the “Manage” menu below your organization.

![Add Campus](images/add_campus.png)


## Next Steps
This short document describes the first steps for getting set up in PeeringDB. Once you have established your presence you should consider sharing information that would be helpful to potential new participants. Things to consider sharing:

* Encourage the networks and Internet Exchanges to also register with PeeringDB, and to indicate their presence in your facility. Thus making their presence visible to others and so increasing the possibility of interconnection with other networks. 

## More Information
The [PeeringDB Data Ownership Policy](https://docs.peeringdb.com/gov/misc/2020-04-06_PeeringDB_Data_Ownership_Policy_Document_v1.0.pdf) describes all the objects in PeeringDB.
