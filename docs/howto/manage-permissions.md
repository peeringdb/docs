# HOWTO: Manage User Permissions

## Do I need a PeeringDB account?
You only need a PeeringDB user account if you want to do one of three things:

* Access contact information
* Create, update, or delete entries in PeeringDB
* Use PeeringDB to login to external services, using the [PeeringDB OAuth service](/blog/oauth_users/).

If you just want to look up information about networks, exchanges, or facilities in PeeringDB, you can do that without an account using the web interface or [the API](/api_specs/).

## How can I manage permissions for users affiliated with my organization?
Unless you want your users to manage parts of the data your organization publishes, they don’t need to be affiliated with your organization.

When you allow a user account to affiliate with your organization, you can delegate some permissions to it. You can delegate them permissions related to exchanges, facilities, and networks. For each type of entry you can delegate permissions to create, update, or delete. 

The table below shows an example for an affiliated user who has only been delegated permission to update the organization’s `net` object.

|            | Create | Update | Delete |
|------------|--------|--------|--------|
| Campus  | No     | No     | No     |
| Carriers  | No     | No     | No     |
| Exchanges  | No     | No     | No     |
| Facilities | No     | No     | No     |
| Networks   | No     | Yes    | No     |

Admin users for an organization can do all these things and can delegate granular permissions to users based on the needs of their organization.

## How do I give permissions to a user who is already affiliated with other organizations?
User accounts can be associated with multiple organizations. For instance, a consultant could be associated with each of their client’s organizations. Similarly, a large organization composed of several operating companies could have a different organization for each operating company in PeeringDB and have some users affiliated with those instead of trying to centralize control.

The user just needs to request, and be granted affiliation with each organization whose data they will be updating in PeeringDB.

## How do I authenticate at external services using my PeeringDB account?
If your organization operates a network and has the Autonomous System registered with PeeringDB, your users can use their PeeringDB accounts to [authenticate at external services](/blog/oauth_users/) that have enabled PeeringDB’s OAuth service. 

In mid-2021 about 150 applications had enabled PeeringDB OAuth. It is used to facilitate peering requests, use network telemetry services, and more.
