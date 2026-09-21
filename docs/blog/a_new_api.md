# A new API for PeeringDB
*21 September, 2026*

We want to improve the speed and efficiency of your PeeringDB queries. We also want to serve PeeringDB out of multiple locations, lowering network latency and improving resilience. To do this properly we need to update [our API](https://www.peeringdb.com/apidocs/).

We’ve published a document explaining the key changes we anticipate for [this new API](../../api_v3/). 

A key element is separating the read and write functions. As most traffic is queries, not updates, that would mean we could have widely distributed query servers. All reads would be cacheable. 

And there would be support for efficient, `curl`-able one liners: “*a network with its exchange presences, an exchange with its members, or a facility with its occupants.*”

Of course, we need your input on the API, especially if you maintain software that uses it. So we’ve created [a mailing list for this discussion](https://lists.peeringdb.com/cgi-bin/mailman/listinfo/pdb-apiv3-discuss). You’re welcome to sign up and let us know what you like, what you’d change, and why.

We’ll use your input to improve the design and publish that.

We also need your input on the transition period, if we choose to retire our current API, which will initially remain for updates.

If you have an idea to improve PeeringDB you can share it on our [low traffic mailing lists](https://docs.peeringdb.com/#mailing-lists) or create an issue directly on [GitHub](https://github.com/peeringdb/peeringdb/issues/). If you find a data quality issue, please let us know at [support@peeringdb.com](mailto:support@peeringdb.com).

--- 

PeeringDB is a freely available, user-maintained, database of networks, and the go-to location for interconnection data. The database facilitates the global interconnection of networks at Internet Exchange Points (IXPs), data centers, and other interconnection facilities, and is the first stop in making interconnection decisions.
