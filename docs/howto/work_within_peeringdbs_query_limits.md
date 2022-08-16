# HOWTO: Work Within PeeringDB’s Query Limits

PeeringDB implements query throttling to encourage efficiently formatted queries and/or local caching. Many popular tools have been upgraded to use PeeringDB more efficiently.

## Query limits
Duplicate queries

* Repeated anonymous identical requests with a response size above 100kb are being limited to 1/hour
* Repeated anonymous identical requests of any size are being limited to 2/minute

Query rate limit

* Anonymous queries limited to 10/minute per IP address
* Authenticated queries limited to 40/minute per user or organization (when an organizational [API key](https://docs.peeringdb.com/howto/api_keys/) is used)

## Efficient Queries
We encourage users to make fewer, larger queries instead of making many small queries.

Instead of sending each ASN you want to learn about as a separate query, create a list of ASNs and send them in a single query. The query element would look like this:

`asn__in=$list_of_ASN_separated_by_comma`

We encourage sending lists of up to 150 ASNs in a single query. We have a [HOWTO article](https://docs.peeringdb.com/howto/search) describing the basics of using our API using popular command line tools such as curl, Python, and jq.

Please use API Keys when automating queries to PeeringDB and set a User-Agent header that identifies the unique software you are using, rather than just a generic query library name.

We also encourage you to leave at least two seconds between queries.

## Local Cache
We encourage you to use a local cache and synchronize it every hour or less frequently in accordance with your organization's needs. When you use a local cache you will only be sent changes since the last sync.

We publish peeringdb-py, which can be used directly or as a reference implementation. [Code is here](https://github.com/peeringdb/peeringdb-py/) and [documentation is here](http://peeringdb.github.io/peeringdb-py/).

If you want to implement a local cache using different tools and would like advice, we are happy to talk. Contact us at [support@peeringdb.com](mailto:support@peeringdb.com).


## Tools
Popular tools, including [arouteserver](https://github.com/pierky/arouteserver) have been updated to include support for API Keys and to make more efficient queries. [We publish](https://docs.peeringdb.com/tools/) a list of tools that we know use PeeringDB. Check the list for tools that you use and upgrade old versions to take advantage of new features and improve everyone’s PeeringDB experience. 
