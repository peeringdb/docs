# Glossary

This glossary focuses on terms that are specific to PeeringDB. Other organizations provide glossaries of a wide range of Internet infrastructure terminology. These include:

- [APNIC](https://www.apnic.net/about-apnic/a-z-glossary/) 
- [Euro-IX](https://www.euro-ix.net/en/services/glossary/)  
- [ICANN](https://www.icann.org/resources/en/glossary)
- [RIPE NCC](https://www.ripe.net/manage-ips-and-asns/db/support/documentation/glossary)

The first set of definitions describes object types and the second set defines the different kinds of contact. 

# PeeringDB Specific Terms

|  **Object Name**   | **Definition**    |
| --- | --- |
| `fac` | The name of the database object representing interconnection facilities. |
| Facility | A place where networks can connect with other networks. Some interconnection facilities are data centers or suites within data centers. Others are significantly smaller. |
| `facix` | The name of an object derived from the intersection of a `fac` and an `ix` object. This happens when an IXP has a presence at an interconnection facility. |
| `ix`  | The name of the database object representing IXPs. |
| ix-f | The Internet Exchange Federation is a group of four regional IXP Associations. In the context of PeeringDB, their name is applied to the import of JSON structured data that complies with the [IX-F Member Export Schema](https://github.com/euro-ix/json-schemas). |
| IXP | An infrastructure for interconnecting three or more Autonomous Systems. |
| `net` | The name of the database object representing networks. |
| `netix` | The name of an object derived from the intersection of a `net` and an `ix` object. This happens when a network is connected to an IXP. |
| Network | An Autonomous System, as defined in [RFC 1930](https://www.rfc-editor.org/rfc/rfc1930). |
| PeeringDB | PeeringDB is a freely available, user-maintained, database of networks, and the go-to location for interconnection data. The database facilitates the global interconnection of networks at Internet Exchange Points (IXPs), data centers, and other interconnection facilities, and is the first stop in making interconnection decisions. |
| `poc` | A Point of Contact for a specific functional role at an organization (see below). |

# Contact Role Types
Not all organizations will have all contact types. For example, an academic institution might not need a sales contact.

| **Role** | **Description** |
| --- | --- |
| Abuse | A contact address where reports of abuse can be submitted. |
| Maintenance | A contact address for the receipt of maintenance notifications, such as the scheduling of maintenance windows from peers. |
| NOC | A contact address for a Network Operations Center. This is the address to use when discussing network anomalies. |
| Policy | A contact address for peering and interconnection requests and questions. |
| Public Relations | A contact address for an organization’s PR or marketing team. |
| Sales | A contact address for an organization’s sales team. |
| Technical | A contact address for non-routine technical questions that aren't handled by the NOC. |