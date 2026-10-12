# What Networks Need to Check and Update 
*12 October 2026*

About half of all ASNs seen in BGP are registered in PeeringDB, which is a freely available, user-maintained, database of networks and more. That means it’s useful to regularly login and check that what is published is still current.

These are the three most important things to check on a regular basis, so you can update them when they change.

## Name and website

Your company’s ASN remains can often remain unchanged after a merger or acquisition but its name or website might change. 

Some organizations link to broken websites or sites that have been hijacked and are serving malware. 

## Contact Data

Make sure the addresses you list for Abuse and Technical, or NOC, roles are still current and working. People at other networks will want to contact you to let you know about scheduled maintenance, and help troubleshoot connectivity problems.

## Max Prefix Count

Other networks rely on the maximum number of prefixes you publish when configuring their networks. You don’t want to announce or transit more prefixes than you’ve published because that could lead to being filtered. You should make sure you’re publishing a realistic number for both IPv4 and IPv6.

If you have an idea to improve PeeringDB you can share it on our [low traffic mailing lists](https://docs.peeringdb.com/#mailing-lists) or create an issue directly on [GitHub](https://github.com/peeringdb/peeringdb/issues/). If you find a data quality issue, please let us know at [support@peeringdb.com](mailto:support@peeringdb.com).

--- 

PeeringDB is a freely available, user-maintained, database of networks, and the go-to location for interconnection data. The database facilitates the global interconnection of networks at Internet Exchange Points (IXPs), data centers, and other interconnection facilities, and is the first stop in making interconnection decisions.

