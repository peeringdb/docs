# HOWTO: Work Within PeeringDB’s Query Limits

PeeringDB implements query throttling to encourage efficiently formatted queries and/or local caching. Many popular tools have been upgraded to use PeeringDB more efficiently.

## Query limits

Duplicate queries:

* Repeated anonymous identical requests with a response size above 100kb are being limited to 1/hour
* Repeated anonymous identical requests of any size are being limited to 2/minute

Query rate limit:

* Anonymous queries limited to 20/minute per IP address
* Authenticated queries limited to 40/minute per user or organization (when an organizational [API key](/howto/api_keys) is used)

## Efficient queries

We encourage users to make fewer, larger queries instead of making many small queries.

Instead of sending each ASN you want to learn about as a separate query, create a list of ASNs and send them in a single query. The query element would look like this:

`asn__in=$list_of_ASN_separated_by_comma`

We encourage sending lists of up to 150 ASNs in a single query. We have a [HOWTO article](/howto/search) describing the basics of using our API using popular command line tools such as curl, Python, and jq.

Please use API Keys when automating queries to PeeringDB and set a User-Agent header that identifies the unique software you are using, rather than just a generic query library name.

We also encourage you to leave at least two seconds between queries.

## Local cache – `peeringdb-py`

We encourage you to use local cache `peeringdb-py` and synchronize it at least once a day, possibly as frequently as once per hour. Please use a random time – [examples](https://peeringdb.github.io/peeringdb-py/cli/#sync) – for each sync to avoid pulling from the servers at the same time as others. Synchronizing at least once a day minimizes the chance that you'll hit query limits. This is because `peeringdb-py` will only be sent changes since the last sync.

`peeringdb-py`, can be used directly or as a reference implementation. [Code is here](https://github.com/peeringdb/peeringdb-py/), [documentation is here](http://peeringdb.github.io/peeringdb-py/), and [install HOWTO is here](/howto/peeringdb-py).

We highly recommend using an API key with `peeringdb-py`.

If you want to implement a local cache using different tools and would like advice, we are happy to talk. Contact us at [support@peeringdb.com](mailto:support@peeringdb.com).


## Tools

Popular tools, including [arouteserver](https://github.com/pierky/arouteserver) have been updated to include support for API Keys and to make more efficient queries. [We publish](/tools/) a list of tools that we know use PeeringDB. Check the list for tools that you use and upgrade old versions to take advantage of new features and improve everyone’s PeeringDB experience. 

## Improving this HOWTO

Please let us know how we could improve this article. Send a mail to the [Outreach Committee](mailto:outreachcom@lists.peeringdb.com).
