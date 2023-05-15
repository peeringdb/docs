# Release Notes and Schedule

The release notes list the GitHub issues and a summary of what has changed in PeeringDB software releases.

Each new release has a one week beta test period on the [beta server](https://beta.peeringdb.com/) before it goes live.  The beta and new releases are announced on the [PeeringDB Announce Mailing List](https://lists.peeringdb.com/cgi-bin/mailman/listinfo/pdb-announce) and on [Twitter](https://twitter.com/PeeringDB), [LinkedIn](https://www.linkedin.com/company/peeringdb) and [Facebook](https://www.facebook.com/peeringdb).

## Release schedule

This schedule provides planned dates for PeeringDB’s future releases. We are sharing these dates to help PeeringDB users plan ahead for testing new and improved features in beta. We also want to help volunteer developers know the date on which their code changes are needed for internal testing before beta release.

We provide a rolling schedule. Dates can change, so if you have a question or request please contact us at: [support@peeringdb.com](mailto:support@peeringdb.com).

Our releases are generally deployed at around 04:00 UTC.

| **Release number** | **Internal testing** | **Beta release** | **Production release** |
| -------------- | ---------------- | ------------ | ------------------ |
| 2.47.0 | 2023-05-10 | 2023-05-17 | 2023-05-24 |
| 2.48.0 | 2023-06-14 | 2023-06-21 | 2023-06-28 |
| 2.49.0 | 2023-07-05 | 2023-07-12 | 2023-07-19 |
| 2.50.0 | 2023-08-09 | 2023-08-16 | 2023-08-23 |
| 2.51.0 | 2023-09-06 | 2023-09-13 | 2023-09-20 |
| 2.52.0 | 2023-10-18 | 2023-10-25 | 2023-11-06 |
| 2.53.0 | 2023-11-22 | 2023-11-29 | 2023-12-01 |

## Release 2.47.0

Beta Announcement Date: 17 May 2023
Release Date: 24 May 2023

| **GitHub Issue** | **Summary** |
| ----------------- | ----------- |
| [#1204 Improve Search Functionality](https://github.com/peeringdb/peeringdb/issues/1204) | Significant improvements to search via a new backend. |
| [#1290 Add permission 'manage peering sessions'](https://github.com/peeringdb/peeringdb/issues/1290) | Adds a permission for managing peering sessions, that is useful for portal enabling PeeringDB OAuth. |
| [#1241 Don't allow the first and last addresses being assigned](https://github.com/peeringdb/peeringdb/issues/1241) | Added a validation check to fail on network and broadcast addresses. |
| [#1238 Put an Icon next to user name on https://www.peeringdb.com/org/nnnn#users if the user is using U2F](https://github.com/peeringdb/peeringdb/issues/1238) | Added a U2F badge next to user name in organization user listing if the user has set up U2F 2FA  |
| [#1339 Tie TOTP devices and Webauthn Security Keys to the user account](https://github.com/peeringdb/peeringdb/issues/1339) | Tie TOTP devices and Webauthn Security Keys to the user account so the AC can see this information. |
| [#1291 Show all e-mail addresses associated with a username](https://github.com/peeringdb/peeringdb/issues/1291) | All e-mail addresses associated with a user are now shown in the users tab. |
| [#1372 Facility history still broken](https://github.com/peeringdb/peeringdb/issues/1372) | Fixes an issue with `fac` history for AC use. |


## Release 2.46.0

Beta Announcement Date: 12 April 2023
Release Date: 19 April 2023

| **GitHub Issue** | **Summary** |
| ----------------- | ----------- |
| [#1336 Clearly show when a facility is part of a campus](https://github.com/peeringdb/peeringdb/issues/1336) | Adds a small icon to show that a `fac` is a part of a `campus`.  |
| [#387 Replace "website" element in API/UI with social media tags](https://github.com/peeringdb/peeringdb/issues/387) | Introduces the ability to include links to social media accounts from PeeringDB pages. |
| [#1333 Calling /api/carrier with parameters is broken](https://github.com/peeringdb/peeringdb/issues/1333) | Fixes a bug in the API support for the new `carrier` object. |
| [#1094 IX-F Importer: duplicate address(es) should result in rejection of JSON export and notification of IXP](https://github.com/peeringdb/peeringdb/issues/1094) | Fixes a bug in handling duplicate IP addresses in IX-F imports. |
| [#1249 Update MkDocs for docs.peeringdb.com](https://github.com/peeringdb/peeringdb/issues/1249) | Updates the software used by https://docs.peeringdb.com |


## Release 2.45.0

Beta Announcement Date: 15 March 2023
Release Date: 22 March 2023

| **GitHub Issue** | **Summary** |
| ----------------- | ----------- |
| [#1295 Allow anonymous users to change languages](https://github.com/peeringdb/peeringdb/issues/1295) | It is now possible to select a PeeringDB translation without logging in to the website. |
| [#1281 better <title\> tags](https://github.com/peeringdb/peeringdb/issues/1281) | The HTML <title\> tag of pages on www.peeringdb.com now shows key information from the page, like a network name or search term. |
| [#749 Rename Private Peering Facilities to Interconnection Facilities in the UI](https://github.com/peeringdb/peeringdb/issues/749) | Private Peering Facilities have been renamed to Interconnection Facilities in the UI. |
| [#1308 Deploy Google Analytics on www and docs](https://github.com/peeringdb/peeringdb/issues/1308) | We have deployed Google Analytics to measure website traffic. |
| [#1271 Implement auto-removal of stale networks according to DOTF recommendations](https://github.com/peeringdb/peeringdb/issues/1271) | Stay networks are now automatically removed as per the [DOTF recommendations](https://docs.peeringdb.com/taskforce/dataownership/). |
| [#389 It should be impossible to save an active entity under an entity that is marked as deleted.](https://github.com/peeringdb/peeringdb/issues/389) | It is no longer possible to save an object under one that's marked as deleted. |

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
