# Two Security Fixes

Our [November release](/release_notes/#release-2630) includes fixes for two security issues.

1. There is now a [limit on password length](https://github.com/peeringdb/peeringdb/issues/1707). It was previously possible to create a password of any length and that could be used to degrade the service. Passwords are now limited to 1,024 characters. 
2. You must now [verify your email address](https://github.com/peeringdb/peeringdb/issues/1708) before enabling MFA. Previously, you could sign up with a victim email address, establish MFA, and deny them an account using their address.

We are grateful to Mridul Vohra, who reported these issues to us. 

These reports were timely as we are working to [make MFA mandatory](https://github.com/peeringdb/peeringdb/issues/1634) for all PeeringDB users. The first step along this path was adding [support for Passkeys](https://github.com/peeringdb/peeringdb/issues/1584). We'll be communicating more about making MFA mandatory soon.

We welcome reports like those made by Mridul Vohra. If you notice an issue, please check our [HOWTO](/howto/make-a-security-report/) on making security reports.

We will do our best to resolve security issues in a timely fashion. We'll also send you a gift with the PeeringDB logo, and we'll recognize your contribution in a report like this.

--- 

If you have an idea to improve PeeringDB you can share it on our low traffic [mailing lists](https://docs.peeringdb.com/#mailing-lists) or create an issue directly on [GitHub](https://github.com/peeringdb/peeringdb/issues). If you find a data quality issue, please let us know at [support@peeringdb.com](mailto:support@peeringdb.com).

PeeringDB is a freely available, user-maintained, database of networks, and the go-to location for interconnection data. The database facilitates the global interconnection of networks at Internet Exchange Points (IXPs), data centers, and other interconnection facilities, and is the first stop in making interconnection decisions.
