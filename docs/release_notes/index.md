# Release Notes and Schedule

The release notes list the GitHub issues and a summary of what has changed in PeeringDB software releases.

Each new release has a one week beta test period on the [beta server](https://beta.peeringdb.com/) before it goes live.  The beta and new releases are announced on the [PeeringDB Announce Mailing List](https://lists.peeringdb.com/cgi-bin/mailman/listinfo/pdb-announce) and on [Twitter](https://twitter.com/PeeringDB), [LinkedIn](https://www.linkedin.com/company/peeringdb) and [Facebook](https://www.facebook.com/peeringdb).

## Release schedule

This schedule provides planned dates for PeeringDB’s future releases. We are sharing these dates to help PeeringDB users plan ahead for testing new and improved features in beta. We also want to help volunteer developers know the date on which their code changes are needed for internal testing before beta release.

We provide a rolling schedule. Dates can change, so if you have a question or request please contact us at: [support@peeringdb.com](mailto:support@peeringdb.com).

Our releases are generally deployed at around 04:00 UTC.

| **Release number** | **Internal testing** | **Beta release** | **Production release** |
| -------------- | ---------------- | ------------ | ------------------ |
| 2.44.0 | 2023-02-01 | 2023-02-15 | 2023-02-22 |
| 2.45.0 | 2023-03-08 | 2023-03-15 | 2023-03-22 |
| 2.46.0 | 2023-04-05 | 2023-04-12 | 2023-04-19 |
| 2.47.0 | 2023-05-10 | 2023-05-17 | 2023-05-24 |
| 2.48.0 | 2023-06-14 | 2023-06-21 | 2023-06-28 |

## Release 2.44.0

Beta Announcement Date: 15 February 2023
Release Date: 22 February 2023

| **GitHub Issue** | **Summary** |
| ----------------- | ----------- |
| [#1110 Add campus object](https://github.com/peeringdb/peeringdb/issues/1110) | Initial deployment of a Campus object  – a record to describe facilities where inter-facility cross connects are available as easily as intra-facility cross connects. |
| [#1191 OAuth logins with 2FA don't complete first time](https://github.com/peeringdb/peeringdb/issues/1191) | Fixes a bug that broke the OAuth flow when MFA was enabled. |
| [#668 Add "self" as an object identifier, for documentation purposes](https://github.com/peeringdb/peeringdb/issues/668) | Adds a "self" object identifier to API and views for GET requests. Authenticated users going to https://www.peeringdb.com/{net | ix | org}/self will redirect to URL for the first object of that type affiliated with the user. Unauthenticated users are taken to an example object. |

## Release 2.43.1

Release Date: 10 February 2023

| **GitHub Issue** | **Summary** |
| ----------------- | ----------- |
| [#1315 issues when accepting / denying carrier presence requests](https://github.com/peeringdb/peeringdb/issues/1315) | Fix permission issues when accepting or rejecting `carrier` `facility` presence requests and automatically approve them when they are from the same organization. |

## Release 2.43.0

Beta Announcement Date: 18 January 2023
Release Date: 25 January 2023

| **GitHub Issue** | **Summary** |
| ----------------- | ----------- |
| [#909 Add Carrier Record Type](https://github.com/peeringdb/peeringdb/issues/909) | Initial deployment of a Carrier record – a record to describe providers of high capacity links between facilities, running at [layers 1 or 2](https://en.wikipedia.org/wiki/OSI_model#Layer_1:_Physical_layer). |
| [#1140 API keys: disabling of user account by a PeeringDB admin does not disable access via a User API key. Also no disable mech, only revoke.](https://github.com/peeringdb/peeringdb/issues/1140) | Fixes a bug where user API Keys were not disabled when their account was disabled. |
| [#1220 API requests with invalid Authentication headers should notify users in some way](https://github.com/peeringdb/peeringdb/issues/1220) | Requests with an invalid API key now return appropriate error codes. |
| [#1130 Allow user to change account username](https://github.com/peeringdb/peeringdb/issues/1130) | Users can now change their account name. |
| [#970 Cache hints are needed for optimal CDN use](https://github.com/peeringdb/peeringdb/issues/970) | Adds cache hints to make CDN deployment more effective. |
| [#1278 Commandline tool "Run command" button gone](https://github.com/peeringdb/peeringdb/issues/1278) | Fixes a problem affecting Admins – a tool was hidden. |
| [#1279 RIR status gets deleted when changes are made to the network](https://github.com/peeringdb/peeringdb/issues/1279) | Improves the new process for validating networks against RIR data (see: [#1280](https://github.com/peeringdb/peeringdb/issues/1280)). |
| [#658 Improve MTU field](https://github.com/peeringdb/peeringdb/issues/658) | MTUs now default to 1500 and there's a new dropdown list of options to select from. |
| [#1282 Ops: Emails to OPERATIONS_EMAIL need to be rate-limited](https://github.com/peeringdb/peeringdb/issues/1282) | Introduces a rate limit for automatic mail sent to Operations. |
| [#1283 Footer "Global System Statistics" should be cached within django instance, not updated with every page load](https://github.com/peeringdb/peeringdb/issues/1283) | Global System Statistics are now generated periodically instead of on each page load. |
| [#1284 Ops: django needs lightweight healthcheck route that confirms database connectivity](https://github.com/peeringdb/peeringdb/issues/1284) | Introduces a lightweight health check for database availability. |
| [#1285 Ops: various indexes are needed](https://github.com/peeringdb/peeringdb/issues/1285) | Introduces new database indexes. |
| [#1288 Ops: Expose CSP_CONNECT_SRC to .env](https://github.com/peeringdb/peeringdb/issues/1288) | Add configuration options for ease of operations. |
| [#1296 CSRF cookie not set error from email confirmation view](https://github.com/peeringdb/peeringdb/issues/1296) | Fix a bug with CSRF cookies not being set. |

## Older releases

* [2022 Release Notes](/release_notes/release_notes_2022/)
* [2021 Release Notes](/release_notes/release_notes_2021/)
* [2020 Release Notes](/release_notes/release_notes_2020/)
