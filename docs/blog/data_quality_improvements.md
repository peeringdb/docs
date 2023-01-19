# Data Quality Improvements Rolled Out

Each year we run a user survey. Users keep telling us that network configuration data in PeeringDB is a top priority.

![[Photo by Elena Koycheva on Unsplash]](images/elena-koycheva-fortune-cookie-unsplash.jpg)

We have recently added some automation to improve our data quality for networks. We now track the status of each ASN registered in PeeringDB at the RIRs and NIRs. When a network is no longer in the RIR or NIR database we can remove it.

[Release 2.41.0](/release_notes/) completes the deployment of this feature. It will remove about 150 networks, which is only about 0.5%. But over time, it should help us maintain the highest quality data possible.

If you have an idea to improve PeeringDB you can share it on our [low traffic mailing lists](https://docs.peeringdb.com/#mailing-lists) or create an issue directly on [GitHub](https://github.com/peeringdb/peeringdb). If you find a data quality issue, please let us know at <support@peeringdb.com>.

---

PeeringDB is a freely available, user-maintained, database of networks, and the go-to location for interconnection data. The database facilitates the global interconnection of networks at Internet Exchange Points (IXPs), data centers, and other interconnection facilities, and is the first stop in making interconnection decisions.
