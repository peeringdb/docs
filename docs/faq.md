
# FAQ


### How do I query by ASN?

> You may type in the ASN in the search box
> `http://as12345.b.peeringdb.com` (subdomain because of HSTS, will go back to normal on release)
> `https://beta.peeringdb.com/asn/12345`
> For API
> `https://beta.peeringdb.com/api/asn/12345`

### How do I get a login?

Your original level 2 login should work. If your login only had level 1 access in version 1, it is not imported into the version 2 database because there is no difference between unvalidated and read only in version 1. If you want a read only login, you'll have to add it manually once version 2 is released.

Logins with level 2 access that are not working in beta should contact <support@peeringdb.com>.

### How do the new permissions work?

Now there is an 'org' entity which owns the records.  A record can be a facility, an exchange point, or a network.  Users are added to the org entity and can then be given access to any facility, any network, any exchange point, or anything the org itself owns.

### Authenticating via embedded user/pass in the URL

Support for this depends on the client and some browsers have stopped supporting embedded
authentication in the URL

So for example 

    https://<username>:<password>@beta.peeringdb.com/api/net/1 
    
may work or it may not depending on the browser you are using.

### Why are dates represented as strings in the API?
Date strings are ISO 8601 to keep a standard format. Comparison operations such as `__gt`, `__lt`, etc all still work as expected. For fetching records against updated timestamp, you may also use `?since=<seconds since epoch>`

### How do I sync the whole database to my local machine?
You may make a full local copy with <https://github.com/peeringdb/peeringdb-py>, see docs at <http://peeringdb.github.io/peeringdb-py/cli/>

Initially it will perform full sync, then it will only do an incremental sync (only updates records that have changed), so you're free to run it as often as you want.

