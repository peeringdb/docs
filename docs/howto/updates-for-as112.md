# HOWTO: What is AS112?

Many networks using private address space ([RFC 1918](https://www.rfc-editor.org/info/rfc1918)) leak the reverse DNS lookups instead of running a local DNS server to respond to them. To stop this traffic from overwhelming root nameservers, volunteers run [AS112 nameservers](https://www.as112.net), which provide authoritative, local answers.

# What is PeeringDB?

PeeringDB is a freely available, user-maintained, database of networks, and the go-to location for interconnection data. The database facilitates the global interconnection of networks at Internet Exchange Points (IXPs), data centers, and other interconnection facilities, and is the first stop in making interconnection decisions.

The database is a non-profit, community-driven initiative run and promoted by volunteers. It is a public tool for the growth and good of the Internet. Join the community and support the continued development of the Internet.

# How Does PeeringDB Visibility Help?

The listing for [AS112 in PeeringDB](https://www.peeringdb.com/net/10664) contains the peering LAN IP addresses of the routers for the network. This can be used as a source of configuration information for the peering routers of other networks at the same IXP.

# What you need to do

## IXPs sharing technical information using the [IX-F Member Export Schema](https://github.com/euro-ix/json-schemas)

When an IXP shares technical information about its infrastructure using the IX-F Member Export Schema the existence of the AS112 node, and its peering LAN address, will automatically be populated in PeeringDB. You, as the operators of the node do not need to do anything.

This is because AS112 has enabled the option to allow the IXPs' IX-F data to [automatically populate](/howto/get-started-operator/#database-records-to-create) its entry in PeeringDB.

## IXPs not sharing technical information using the IX-F Member Export Schema

If your IXP does not share technical information about its infrastructure using the IX-F Member Export Schema you can ask them to do so.

You can also reach out to ops@as112.net and the PeeringDB entry for AS112 will be manually updated.

## Improving this HOWTO

Please let us know how we could improve this article. Send a mail to the [Outreach Committee](mailto:outreachcom@lists.peeringdb.com).
