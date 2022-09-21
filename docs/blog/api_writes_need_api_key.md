# API writes now need an API Key
You now need to use an API key if you want to update PeeringDB using the API. PeeringDB will continue to support HTTP Basic Authentication (HBA) for queries with the existing API, but transitioning to an API key is strongly recommended for users and organizations who have not already done so, since it is a more secure operational practice.

We encourage all users to enable Multi-Factor Authentication (MFA) and to use that when accessing our website from a browser. We encourage anyone that wants to use our API to do so using API keys.

We made this change because there is no way to perform MFA with HBA. Removing the ability to update PeeringDB via the API without API keys conforms to security best practices.

We support both user and organizational API keys. We have a [HOWTO guide](https://docs.peeringdb.com/howto/api_keys/) for creating API keys and using them.

We have also introduced some [organizational policy features](https://docs.peeringdb.com/howto/organizational_policy) this month. Organizations can now require users: 

* to enable MFA
* to have an email address from a specific domain 
* to revalidate their account on a schedule set by the organization

We made this change because of an internal security analysis. We accept security reports to [security@peeringdb.com](mailto:security@peeringdb.com). We have published a [HOWTO article](https://docs.peeringdb.com/howto/make-a-security-report/) for making security reports. 

--- 

If you have questions about PeeringDB security, please write to [security@peeringdb.com](mailto:security@peeringdb.com). If you need help configuring API keys, please write to [support@peeringdb.com](mailto:support@peeringdb.com).