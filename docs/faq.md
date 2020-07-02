
# Frequently asked questions

## General
### What is PeeringDB?

PeeringDB is a freely available, user-maintained, database of networks, and the go-to location for interconnection data. The database facilitates the global interconnection of networks at Internet Exchange Points (IXPs), data centers, and other interconnection facilities, and is the first stop in making interconnection decisions.

The database is a non-profit, community-driven initiative run and promoted by volunteers. It is a public tool for the growth and good of the Internet. Join the community and support the continued development of the Internet. 

### How do I get started?

See our Quick Start guide: <http://docs.peeringdb.com/#quick-start>

### Affiliation requests 

Q: How does affiliation to an organization work?

A: After you have registered, go to your [profile](https://peeringdb.com/profile).

* If your organization owns a network (also called AS or ASN), type in the AS number into the field `ASN`. Then click on the button `Affiliate`.

* If your ASN already is in PeeringDB and your `org` record does not yet have an admin account this request will be sent to [PeeringDB Support](mailto:support@peeringdb.com)

* If your organisation already has one or more admins your request is forwarded to them. They will have to approve / deny your request

* If your ASN is not in PeeringDB this procedure will first try to retrieve information about this ASN via [RDAP](https://about.rdap.org/) to prepopulate the `net` record and the `org` record in case it also does not exist. We also use information from this query to auto approve your request if the email address in the RDAP record matches your email address. If this fails your request will be sent to [PeeringDB Support](mailto:support@peeringdb.com)

* You may also use the field `organisation`to request affiliation to an existing or new organisation. Start typing the name of your company and select from the popup or create a new organisation. Your request is sent to your admins if there is one or to [PeeringDB Support](mailto:support@peeringdb.com) otherwise

In any case you should get an answer either from your admin or [PeeringDB Support](mailto:support@peeringdb.com). If you don't get an answer within two working days, please mail [PeeringDB Support](mailto:support@peeringdb.com) providing necessary information (ASN, Organization).


## Technical
### How do I query by ASN?

You may type in the ASN in the search box, or for web:
`http://as42.peeringdb.com`
`https://peeringdb.com/net?asn=42`

For API:
`https://peeringdb.com/api/net?asn=42`


### Using /asn used to work, what happened?

Please see <http://lists.peeringdb.com/pipermail/pdb-announce/2016-March/000036.html> for details.

### How do the new permissions work?

Now there is an `org` entity which owns the records.  A record can be a facility, an exchange point, or a network.  Users are added to the org entity and can then be given access to any facility, any network, any exchange point, or anything the org itself owns.

### Authenticating via embedded user/pass in the URL

Support for this depends on the client and some browsers have stopped supporting embedded
authentication in the URL

So for example 

    https://<username>:<password>@peeringdb.com/api/net/1 
    
may work or it may not depending on the browser you are using.

### Why are dates represented as strings in the API?
Date strings are ISO 8601 to keep a standard format. Comparison operations such as `__gt`, `__lt`, etc all still work as expected. For fetching records against updated timestamp, you may also use `?since=<seconds since epoch>`

### How do I sync the whole database to my local machine?
You may make a full local copy with <https://github.com/peeringdb/peeringdb-py>, see docs at <http://peeringdb.github.io/peeringdb-py/cli/>

Initially it will perform full sync, then it will only do an incremental sync (only updates records that have changed), so you're free to run it as often as you want.

Alternatively [peeringdb-simplesync](https://git.2e8.dk/peeringdb-simplesync/about/) can be used to maintain a mirror in PostgreSQL.

### When syncing to MySQL I get 'Illegal mix of collations'

Such as:

    django.db.utils.OperationalError: (1267, "Illegal mix of collations (latin1_swedish_ci,IMPLICIT) and (utf8_general_ci,COERCIBLE) for operation '='")

We will fix that when time allows, for the time being, just run:

    alter database peeringdb default character set utf8 default collate utf8_unicode_ci;
    
### What does the `Never via route servers` flag mean and how does it work?
With release 2.18.0 a new feature `Never via route servers` (API field `info_never_via_route_servers`) has been introduced. There is a tick box in section "Protcols Supported" to set it. If set it is a hint for an IXP to use that information to block any BGP updates where the AS_PATH matches the regular expression _ASN_. Please make sure that the IXPs you are connected to are supporting this feature. I.e. they have to check PeeringDB regularly, evaluate this field and honour the setting.

## Governance and membership
### How does one become a PeeringDB member?

Your organization does not need to be a Member to have an active account at PeeringDB.com, but Membership is available to those that do. Per the Bylaws, Membership is determined by having an active PeeringDB.com account, and a subscription to the [pdb-gov](http://lists.peeringdb.com/cgi-bin/mailman/listinfo/pdb-gov) mailing list.

### What are the Terms and Conditions for PeeringDB membership?

Please see <http://docs.peeringdb.com/gov/#organizational-documents> for the legal aspects of PeeringDB. The Acceptable Use Policy is at <https://peeringdb.com/aup>.

### Are there any membership fees required for members?

No, there are no membership fees required. The organization welcomes sponsorships as its method of financial support. Please see <https://www.peeringdb.com/sponsors> for more information on supporting the PeeringDB.

### Are there any liabilities imposed on members?

No, there are not.

### To register network information in the PeeringDB, is an organization required to join as a member?

No, that isn't necessary. 
