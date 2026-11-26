---
date: 2026-11-24
---
# Daily Dumps
*24 November, 2026*

We make PeeringDB available through [an API](https://www.peeringdb.com/apidocs/) and [our website](https://www.peeringdb.com). But both of these are [rate limited](https://docs.peeringdb.com/howto/work_within_peeringdbs_query_limits/), which means you can only make so many queries. Of course, you can [run a local mirror](https://docs.peeringdb.com/howto/peeringdb-py/) and make all the queries you want. But some people just want the data without the server.

We publish daily dumps files for those people. You can download all the publicly available data in JSON files. There’s one file for each object type.

This is ideal for anyone doing research or analysis across large parts of the dataset. For instance, an academic researching exchanges might want to download the JSON file of all exchanges every day.

These files are what `peeringdb-py` uses to bootstrap itself. We’ve published the URLs in our [HOWTO document on mirroring PeeringDB](https://docs.peeringdb.com/howto/mirror/).

If you have an idea to improve PeeringDB you can share it on our low traffic [mailing lists](https://docs.peeringdb.com/#mailing-lists) or create an issue directly on [GitHub](https://github.com/peeringdb/peeringdb/issues). If you find a data quality issue, please let us know at [support@peeringdb.com](mailto:support@peeringdb.com).

---

PeeringDB is a freely available, user-maintained, database of networks, and the go-to location for interconnection data. The database facilitates the global interconnection of networks at Internet Exchange Points (IXPs), data centers, and other interconnection facilities, and is the first stop in making interconnection decisions.
