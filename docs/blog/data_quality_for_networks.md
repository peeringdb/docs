# Data Quality for Networks
*July 1, 2026*

Over 34,000 organizations have data in PeeringDB, so we try to automate improvements to data quality. For instance, we’ve recently automated changes to normalize country and city names for facilities using external geolocation databases. When we improve data quality we make PeeringDB more valuable for users. 

A conversation at RIPE 92 led to suggestions for improvements in how we publish data about AS-SETs.

An AS-SET describes your ‘customer cone’ to networks you peer with. It indicates which prefixes should be accepted by their BGP neighbors.

Not all networks use an AS-SET named with their AS Number and some of those are published in more than one IRR. When this happens, organizations can’t fully automate sign-up and service delivery because an employee needs to work out which AS-SET to use.

We’ll be making a series of changes to help improve data quality for AS-SETs.

First, we’ve removed the less preferred option for indicating which IRR an AS-SET uses. We automatically converted the few networks using an @IRR suffix to the preferred prefix format. 

A network whose setname was AS64496 might have used AS64496@IRR to show which IRR its AS-SET was published in. We’ve converted this to IRR::AS64496.

Next, where a listed AS-SET name is unique, we’ll automatically prefix the IRR it’s published in. Sadly, not all AS-SETs are unique, so we’ll contact those networks and ask them to update their data.

We’ll also update the editor for listing an AS-SET. It will check that the set name exists in the selected IRR so users can’t accidentally save a typo.

Finally, we know that we’ll need to monitor to ensure that data quality is being maintained and improved. So we’ll generate regular reports to let us know if the situation changes. 

These changes were discussed [on GitHub](https://github.com/peeringdb/peeringdb/issues) following conversations with users. We’ll be attending over 40 events this year, so there’s plenty of opportunity to discuss the improvements you need by chatting to us there. But you can also discuss issues on our [low volume discussion lists](https://docs.peeringdb.com/#mailing-lists), or open an issue directly in GitHub.

--- 

PeeringDB is a freely available, user-maintained, database of networks, and the go-to location for interconnection data. The database facilitates the global interconnection of networks at Internet Exchange Points (IXPs), data centers, and other interconnection facilities, and is the first stop in making interconnection decisions.