
# Frequently Asked Questions

## General
### What is the PeeringDB?

It's a database for peering and peering related information. PeeringDB will let you see information about Networks you might want to peer with, where and how you can peer with them, as well as publish information about your own Organization's peering information.

### How do I get started?

See our Quick Start guide: <http://docs.peeringdb.com/#quick-start>

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

### When syncing to MySQL I get 'Illegal mix of collations'

Such as:

    django.db.utils.OperationalError: (1267, "Illegal mix of collations (latin1_swedish_ci,IMPLICIT) and (utf8_general_ci,COERCIBLE) for operation '='")

We will fix that when time allows, for the time being, just run:

    alter database peeringdb default character set utf8 default collate utf8_unicode_ci;

## Governance/Membership
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