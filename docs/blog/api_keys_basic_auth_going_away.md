# API Keys: Basic Authentication is Going Away

If you authenticate when you query the PeeringDB API you'll soon need to use API Keys: we’re deprecating basic auth (username/password) for API calls. We expect to implement this change within six months.

![[Key and Keyboard by Everardo Sanchez on Unsplash]](images/key-keyboard-coffee-everardo-sanchez-550x824.jpg)

As a reminder, the API can be queried without any authentication, but will get lower [query limits](/howto/work_within_peeringdbs_query_limits/) and won't have access to contact information. You need to authenticate for higher query limits and contact information. Today you can do this with a username and password in the header, referred to in HTTP-land as “basic auth”, OR by passing your API key in the query string. When basic auth goes away, the only authentication method supported will be API Key.

The Product Committee has agreed to make [MFA mandatory](https://github.com/peeringdb/peeringdb/issues/1634) for all users. This follows a compromised user account and some defaced pages. No data was lost and the vandalism was rolled back, but it is worth preventing any future such issues proactively while adopting industry-accepted standards Since the UI will no longer be accessible with username and password alone, it makes sense to disable that functionality for API as well.

[Our HOWTO](/howto/api_keys/) describes how to create user or organizational API Keys.They can be created and changed by authenticated users via the web UI, and allow API access to be decoupled from user authentication.

If you use our API, please make sure that you authenticate with an API Key instead of a username and password. Don’t wait for your automation to fail before making this simple change. **Queries needing authentication must use an API Key or will fail when we remove support for basic authentication.**

If you have an idea to improve PeeringDB you can share it on our [low traffic mailing lists](https://docs.peeringdb.com/#mailing-lists) or create an issue directly [on GitHub](https://github.com/peeringdb/peeringdb/issues). If you find a data quality issue, please let us know at [support@peeringdb.com](mailto:support@peeringdb.com).

---

PeeringDB is a freely available, user-maintained, database of networks, and the go-to location for interconnection data. The database facilitates the global interconnection of networks at Internet Exchange Points (IXPs), data centers, and other interconnection facilities, and is the first stop in making interconnection decisions.
