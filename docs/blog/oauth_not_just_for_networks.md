# OAuth isn’t just for networks

PeeringDB has provided an OAuth service for a long time. [It’s popular](https://docs.peeringdb.com/blog/oauth_users/) with networks who want to authenticate other networks but don’t want them to have to create a new account. Until recently, OAuth applications could only be created by organizations with a network.

But now, organizations that don’t run a network can create an OAuth application and get the benefits of authenticating PeeringDB users.

![Login to [bgproutes.io](http://bgproutes.io) with PeeringDB](images/bgproutes_io_peeringdb_preferred_login.png)  

We made this change based on a request from Thomas Holterbach and the [bgproutes.io](http://bgproutes.io) project. This is a project that collects and analyses BGP data. They need to authenticate the connection between the network and the data but don’t need a unique ASN for their service.

*“We run a BGP data collection platform and rely on PeeringDB’s strong authentication system, combined with its robust mapping between users, organizations, and the networks they operate, to confidently authenticate operators through its OAuth system and determine which ASNs they manage. This is essential for ensuring the integrity of the data we collect and for clearly identifying the source of each feed.*

*For this, we needed a new feature: the ability to use OAuth without being tied to a specific ASN. The PeeringDB Product Committee was very responsive in understanding our use case and adapting the system to support it. It is now working smoothly, and tens of operators have already connected to our platform using their PeeringDB accounts.”*  
Thomas Holterbach, bgproutes.io 

Initially, they planned to get access to contact data to authenticate users. This was a challenging way for PeeringDB to meet the project’s needs. The Product Committee didn’t want to change the conditions under which contact data is shared and adding an extra permission would have been complicated.

In the end, we decided to expand the scope of who could create an OAuth application. Each user is aware that they are using PeeringDB’s OAuth when they login with it. And now, organizations without networks in PeeringDB can take advantage of our OAuth service. This could include facility operators or carriers who decide not to run their own L3 network.

If you have an idea to improve PeeringDB you can share it on our low traffic [mailing lists](https://docs.peeringdb.com/#mailing-lists) or create an issue directly on [GitHub](https://github.com/peeringdb/peeringdb/issues). If you find a data quality issue, please let us know at [support@peeringdb.com](mailto:support@peeringdb.com).

--- 

PeeringDB is a freely available, user-maintained, database of networks, and the go-to location for interconnection data. The database facilitates the global interconnection of networks at Internet Exchange Points (IXPs), data centers, and other interconnection facilities, and is the first stop in making interconnection decisions.