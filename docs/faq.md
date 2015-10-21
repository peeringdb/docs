
# FAQ

## How do I query by ASN?

> You may type in the ASN in the search box
> `http://as12345.b.peeringdb.com` (subdomain because of HSTS, will go back to normal on release)
> `https://beta.peeringdb.com/asn/12345`
> For API
> `https://beta.peeringdb.com/api/asn/12345`

## How do I get a login?

> Your original login should work, if not please email support@peeringdb.com

## Authenticating via embedded user/pass in the URL

Support for this depends on the client and some browsers have stopped supporting embedded
authentication in the URL

So for example 

    https://<username>:<password>@beta.peeringdb.com/api/net/1 
    
may work or it may not depending on the browser you are using.
