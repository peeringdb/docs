# HOWTO: Mirroring PeeringDB Data

## About PeeringDB
PeeringDB, as the name suggests, was set up to facilitate peering between networks and peering coordinators. In recent years, the vision of PeeringDB has developed to keep up with the speed and diverse manner in which the Internet is growing. The database is no longer just for peering and peering related information. It now includes all types of interconnection data for networks, clouds, services, and enterprise, as well as interconnection facilities that are developing at the edge of the Internet.

We believe in, and rely on the community to grow and improve the PeeringDB database. The volunteers who run the database are passionate about security, privacy, integrity, and validation of the data in the database. Even though PeeringDB is a freely available and public tool, users strictly adhere to the acceptable use policy, which prevents the database from being used for commercial purposes and discourages unsolicited communications. This is largely policed by the community and has been very effective since PeeringDB was launched.

## Query PeeringDB Locally
You can query PeeringDB locally using a containerized local tool called `peeringdb-py`. We have a HOWTO describing it and linking to detailed technical documentation for installation. Using `peeringdb-py` will ensure that your local source of PeeringDB data is always current. It can keep in sync at near to realtime with little effort. 

## Download PeeringDB over HTTPS
Each object type can be downloaded over HTTPS from [public.peeringdb.com](http://public.peeringdb.com). These bootstrap files are updated every day. 

 - [campus](https://public.peeringdb.com/campus-0.json)
 - [carrier](https://public.peeringdb.com/carrier-0.json)
 - [carrierfac](https://public.peeringdb.com/carrierfac-0.json)
 - [fac](https://public.peeringdb.com/fac-0.json)
 - [ix](https://public.peeringdb.com/ix-0.json)
 - [ixfac](https://public.peeringdb.com/ixfac-0.json)
 - [ixlan](https://public.peeringdb.com/ixlan-0.json)
 - [ixpfx](https://public.peeringdb.com/ixpfx-0.json)
 - [net](https://public.peeringdb.com/net-0.json)
 - [netfac](https://public.peeringdb.com/netfac-0.json)
 - [netixlan](https://public.peeringdb.com/netixlan-0.jso)
 - [org](https://public.peeringdb.com/org-0.json)

## Improving this HOWTO

Please let us know how we could improve this article. Send a mail to the [Outreach Committee](mailto:outreachcom@lists.peeringdb.com).