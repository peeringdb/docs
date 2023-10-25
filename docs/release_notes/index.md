# Release Notes and Schedule

The release notes list the GitHub issues and a summary of what has changed in PeeringDB software releases.

Each new release has a one week beta test period on the [beta server](https://beta.peeringdb.com/) before it goes live.  The beta and new releases are announced on the [PeeringDB Announce Mailing List](https://lists.peeringdb.com/cgi-bin/mailman/listinfo/pdb-announce) and on [Twitter](https://twitter.com/PeeringDB), [LinkedIn](https://www.linkedin.com/company/peeringdb) and [Facebook](https://www.facebook.com/peeringdb).

## Release schedule

This schedule provides planned dates for PeeringDB’s future releases. We are sharing these dates to help PeeringDB users plan ahead for testing new and improved features in beta. We also want to help volunteer developers know the date on which their code changes are needed for internal testing before beta release.

We provide a rolling schedule. Dates can change, so if you have a question or request please contact us at: [support@peeringdb.com](mailto:support@peeringdb.com).

Our releases are generally deployed at around 04:00 UTC.

| **Release number** | **Internal testing** | **Beta release** | **Production release** |
| -------------- | ---------------- | ------------ | ------------------ |
| 2.52.0 | 2023-10-18 | 2023-10-25 | 2023-11-06 |
| 2.53.0 | 2023-11-22 | 2023-11-29 | 2023-12-01 |
| 2.54.0 | 2024-01-09 | 2024-01-16 | 2024-01-24 |
| 2.55.0 | 2024-02-07 | 2024-02-14 | 2024-02-21 |
| 2.56.0 | 2024-03-06 | 2024-03-13 | 2024-03-20 |


## Release 2.52.0

Beta Announcement Date: 25 October 2023
Release Date: 6 November 2023

| **GitHub issue** | **Summary** |
| ----------------- | ----------- |
| [#1328 Support web updates from a source of truth](https://github.com/peeringdb/peeringdb/issues/1328) | Internal sources of truth, like configuration management systems, can now propose PeeringDB updates that a web user can review and either accept or deny.|
| [#1374 Search to include new objects: Campus & Carrier](https://github.com/peeringdb/peeringdb/issues/1374) | Support for new `carrier` and `campus` objects in v2 search, which is now the default with v1 search linked for the time being.|
| [#1368 Facility data export into Google Earth KMZ](https://github.com/peeringdb/peeringdb/issues/1368) | PeeringDB facility data is now exported into a Google Earth KMZ file that includes the details of the facility fields and their contents (`ix`, `net`, `carrier`). It is linked from the web footer and generated every day.|
| [#1394 v2 search failing to find some names](https://github.com/peeringdb/peeringdb/issues/1394) | Fixes a bug where names with hyphens in them were not handled properly by v2 search.|
| [#1313 Improve email confirmation control - add 3 month option & maybe set new default value](https://github.com/peeringdb/peeringdb/issues/1313) | Improve the design of the periodic reconfirmation control for user email addresses and add a new 3 month value.|
| [#1257 Help text covers non-compliant email addresses](https://github.com/peeringdb/peeringdb/issues/1257) | Non-compliant email addresses of affiliated users are now shown, making it easier to know who to contact.|
| [#1164 better rdap error reporting](https://github.com/peeringdb/peeringdb/issues/1164) | Improved error handling and friendlier error reporting to users.|
| [#1260 Add Selenium Grid to CI testing](https://github.com/peeringdb/peeringdb/issues/1260) | Improve automated browser testing for website.|
| [#1380 Reset 'Social Media' to '{}' if field is null](https://github.com/peeringdb/peeringdb/issues/1380) | Fixes a bug with broken page rendering for backend admin users when a social media field was set to `null`.|


## Release 2.51.0

Beta Announcement Date: 13 September 2023
Release Date: 20 September 2023

| **GitHub issue** | **Summary** |
| ----------------- | ----------- |
| [#1364 IX Object Creation Per Policy](https://github.com/peeringdb/peeringdb/issues/1364) | Automates approval of new `ix` objects per [policy](https://docs.peeringdb.com/committee/admin/approval-guidelines/#approving-ixp-ix-objects).|
| [#1226 Add a "Delete Affiliation" button/option to the profile](https://github.com/peeringdb/peeringdb/issues/1226) | Users can now remove an affiliation from their account.|
| [#1431 add redis for caching](https://github.com/peeringdb/peeringdb/issues/1431) | Improves cacheing performance.|
| [#1382 Syntax checker for social media user names broken](https://github.com/peeringdb/peeringdb/issues/1382) | Fixes a bug that rejected social media names that incorporated a hyphen.|
| [#1401 Creating a new network not possible](https://github.com/peeringdb/peeringdb/issues/1401) | Fixes a bug that stopped `net` creation when social media fields were sent with request.|
| [#1419 replace missing Glyphicons](https://github.com/peeringdb/peeringdb/issues/1419) | Use Google's "Sort by Alpha" icon in table headers.|
| [#1182 Manual IX-F import request queue can get stuck](https://github.com/peeringdb/peeringdb/issues/1182) | Fixes a bug that allowed users to enable IX-F imports without setting a URL. The importers also discards imports without a URL.|
| [#1334 IX-F Importer: Cosmetic issue with "resolved" emails and double-slashes in URLs after the FQDN](https://github.com/peeringdb/peeringdb/issues/1334) | Fixes a cosmetic issue with IX-F notification messages.|

## Release 2.50.0

Beta Announcement Date: 16 August 2023
Release Date: 23 August 2023

| **GitHub issue** | **Summary** |
| ----------------- | ----------- |
| [#1352 Include carrier and campus objects in the API](https://github.com/peeringdb/peeringdb/issues/1352) | `carrier` and `campus` objects were not included in the main API at first as we did not know if users would use them. They are now part of the API, making them usable by tools that rely on the API.|
| [#1300 display website URL on all non-org objects](https://github.com/peeringdb/peeringdb/issues/1300) | The website from org objects is now inherited by all child objects. |
| [#1381 Add hover tip to describe meaning of routeserver icon](https://github.com/peeringdb/peeringdb/issues/1381) | As title. |
| [#1361 Add Campus and Carrier Tooltips](https://github.com/peeringdb/peeringdb/issues/1361) | As title. |
| [#1360 IX-F Importer: IX-F Member Data not being nullified after IX stops/changes import](https://github.com/peeringdb/peeringdb/issues/1360) | Fixes a bug where the IX and participants were being mailed about import issues after the import was turned of by the IX operator. |
| [#1239 Add a search field to all AC views](https://github.com/peeringdb/peeringdb/issues/1239) | Better search for support tools. |
| [#1027 Make the search field on cp/peeringdb_server/network/ aware of leading AS/ASN](https://github.com/peeringdb/peeringdb/issues/1027) | Improved handling of variant syntax in support tools. |
| [#1412 Improve performance by updating Python client code](https://github.com/peeringdb/peeringdb/issues/1412) | Replace old python2 sync code with python3 code. |


## Release 2.49.0

Beta Announcement Date: 12 July 2023
Release Date: 19 July 2023

| **GitHub issue** | **Summary** |
| ----------------- | ----------- |
| [#1344 Auto approval of new carrierfac objects](https://github.com/peeringdb/peeringdb/issues/1344) | `carrierfac` objects are now approved automatically, like [`netfac` objects](https://docs.peeringdb.com/howto/search/#querying-with-the-peeringdb-api). |
| [#1299 Alphabetize simple search results](https://github.com/peeringdb/peeringdb/issues/1299) | Exact match search now go at the top, with other results displayed alphabetically. |
| [#997 Allow organizations to require affiliated users to enable 2FA](https://github.com/peeringdb/peeringdb/issues/997) | Organizations can now require their users to turn on MFA. |
| [#1370 Facility Geocode not working](https://github.com/peeringdb/peeringdb/issues/1370) | Fixed a bug that meant some `fac`s did not have a geocode. |
| [#1225 Evaluate ways to reduce operational costs](https://github.com/peeringdb/peeringdb/issues/1225) | Operational work to support deployment directly on cloud provider infrastructure, instead of in a VM. |
| [#1219 Optimize Cacheing](https://github.com/peeringdb/peeringdb/issues/1219) | It is now easier to obtain and cache PeeringDB data. |
| [#1404 Upgrade the django-oauth-toolkit library](https://github.com/peeringdb/peeringdb/issues/1404) | Django update deferred from last month. Oauth application owners were given notice of this breaking change. |


## Release 2.48.0

Beta Announcement Date: 21 June 2023
Release Date: 28 June 2023

| **GitHub issue** | **Summary** |
| ----------------- | ----------- |
| [#1311 Update Dependencies](https://github.com/peeringdb/peeringdb/issues/1311) | Update all dependencies to new major releases. This year includes Django 4.2 LTS. |


## Release 2.47.0

Beta Announcement Date: 17 May 2023
Release Date: 24 May 2023

| **GitHub issue** | **Summary** |
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

| **GitHub issue** | **Summary** |
| ----------------- | ----------- |
| [#1336 Clearly show when a facility is part of a campus](https://github.com/peeringdb/peeringdb/issues/1336) | Adds a small icon to show that a `fac` is a part of a `campus`.  |
| [#387 Replace "website" element in API/UI with social media tags](https://github.com/peeringdb/peeringdb/issues/387) | Introduces the ability to include links to social media accounts from PeeringDB pages. |
| [#1333 Calling /api/carrier with parameters is broken](https://github.com/peeringdb/peeringdb/issues/1333) | Fixes a bug in the API support for the new `carrier` object. |
| [#1094 IX-F Importer: duplicate address(es) should result in rejection of JSON export and notification of IXP](https://github.com/peeringdb/peeringdb/issues/1094) | Fixes a bug in handling duplicate IP addresses in IX-F imports. |
| [#1249 Update MkDocs for docs.peeringdb.com](https://github.com/peeringdb/peeringdb/issues/1249) | Updates the software used by https://docs.peeringdb.com |


## Release 2.45.0

Beta Announcement Date: 15 March 2023
Release Date: 22 March 2023

| **GitHub issue** | **Summary** |
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

| **GitHub issue** | **Summary** |
| ----------------- | ----------- |
| [#1110 Add campus object](https://github.com/peeringdb/peeringdb/issues/1110) | Initial deployment of a Campus object  – a record to describe facilities where inter-facility cross connects are available as easily as intra-facility cross connects. |
| [#1191 OAuth logins with 2FA don't complete first time](https://github.com/peeringdb/peeringdb/issues/1191) | Fixes a bug that broke the OAuth flow when MFA was enabled. |
| [#668 Add "self" as an object identifier, for documentation purposes](https://github.com/peeringdb/peeringdb/issues/668) | Adds a "self" object identifier to API and views for GET requests. Authenticated users going to https://www.peeringdb.com/{net | ix | org}/self will redirect to URL for the first object of that type affiliated with the user. Unauthenticated users are taken to an example object. |

## Release 2.43.1

Release Date: 10 February 2023

| **GitHub issue** | **Summary** |
| ----------------- | ----------- |
| [#1315 issues when accepting / denying carrier presence requests](https://github.com/peeringdb/peeringdb/issues/1315) | Fix permission issues when accepting or rejecting `carrier` `facility` presence requests and automatically approve them when they are from the same organization. |

## Release 2.43.0

Beta Announcement Date: 18 January 2023
Release Date: 25 January 2023

| **GitHub issue** | **Summary** |
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
