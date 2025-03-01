# Improvements for peeringdb-py

We just made installing `peeringdb-py` easier and updated [our documentation](/howto/peeringdb-py/). Now, you can install it with a single command and you can query it using our API.

`peeringdb-py` is the reference implementation for our local cache. You can keep it synchronized with our database but keep all your queries local.

This means it's ideal for testing out automation in a local environment. It also means you can use `peeringdb-py` as a data source for local services, instead of sending queries over the internet. So, you can integrate PeeringDB with other datasets. It also means lower latency and no need to work within our query limits.

You can synchronize it anonymously if you don't need contact information. If you want the contact information for entries then you should synchronize using an [API Key](/howto/api_keys/).

Give it a go and see how simple it is to install and keep in sync. 

If you have an idea to improve PeeringDB you can share it on our [low traffic mailing lists](https://docs.peeringdb.com/#mailing-lists) or create an issue directly on [GitHub](https://github.com/peeringdb/peeringdb/issues/). If you find a data quality issue, please let us know at [support@peeringdb.com](mailto:support@peeringdb.com).

--- 

PeeringDB is a freely available, user-maintained, database of networks, and the go-to location for interconnection data. The database facilitates the global interconnection of networks at Internet Exchange Points (IXPs), data centers, and other interconnection facilities, and is the first stop in making interconnection decisions.
