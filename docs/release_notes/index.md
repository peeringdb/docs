# Release Notes

The release notes list the GitHub issues and a summary of what has changed in PeeringDB software releases.

Each new release has a one week beta test period on the [beta server](https://beta.peeringdb.com/) before it goes live.  The beta and new releases are announced on the [PeeringDB Announce Mailing List](https://lists.peeringdb.com/cgi-bin/mailman/listinfo/pdb-announce) and on [Twitter](https://twitter.com/PeeringDB), [LinkedIn](https://www.linkedin.com/company/peeringdb) and [Facebook](https://www.facebook.com/peeringdb).

## Release 2.38.0

Beta Announcement Date: 16 June 2022
Release Date: 24 June 2022

| **GitHub Issue** | **Summary** |
| ----------------- | ----------- |
| [#930 Admin user is missing the "Edit" button](https://github.com/peeringdb/peeringdb/issues/930) | Fixes a bug that prevented users from editing their entries. |
| [#963 Add the IX name and id to IX-F Import Emails](https://github.com/peeringdb/peeringdb/issues/963) | Addresses messages to exchange operators more clearly. |
| [#879 Add "Last login" to https://peeringdb.com/cp/peeringdb_server/user/](https://github.com/peeringdb/peeringdb/issues/879) | Let's the Admin Committee know who from an organization most recently logged in. |
| [#1057 Force users to provide input for first / last names when registering with PeeringDB](https://github.com/peeringdb/peeringdb/issues/1057) | Use the username instead of formal name in tickets when it's not registered. |
| [#660 Bug in renumbering tool ](https://github.com/peeringdb/peeringdb/issues/660) | Fixes a bug with the renubering tool. |
| [#1172 Ops: Exempt superusers (PeeringDB Admin Committee & Operations Committee admins) from throttling](https://github.com/peeringdb/peeringdb/issues/1172) | API and Melissa request throttling is no longer applied to authenticated admin users. |
| [#1177 Locale field update has uncaught exception](https://github.com/peeringdb/peeringdb/issues/1177) | Fixes a bug where a logged in user could send data that generated DataError and Internal Server Error. Exceptions are now caught appropriately and return relevant errors to users. |
| [#1174 Insecure Dependencies](https://github.com/peeringdb/peeringdb/issues/1174) | Upgrades three dependencies to newer versions that address known vulnerabilities. |
| [#1186 Browser caches OAuth2 application client secrets](https://github.com/peeringdb/peeringdb/issues/1186) | Fixes a bug that allowed browsers to cache the OAuth2 application details page. |
| [#1184 Tie CSRF token to session](https://github.com/peeringdb/peeringdb/issues/1184) | Fixes a bug by binding the session ID and the CSRF token together to reduce the risk that an old token is misused. |

## Release 2.37.0

Beta Announcement Date: 11 May 2022
Release Date: 17 May 2022

| **GitHub Issue** | **Summary** |
| ----------------- | ----------- |
| [#403 Notify a record holder when there is an automated change to the profile](https://github.com/peeringdb/peeringdb/issues/404) | Notifications are now sent when PeeringDB administrators make changes to records. |
| [#1155 Feature Request: Promote OAuth application to admin-level access?](https://github.com/peeringdb/peeringdb/issues/1155) | Adds organization level OAuth app management and allows organizations to transfer existing OAuth apps tied to their users to the organization. |
| [#942 Failure on Admin Organization Merge](https://github.com/peeringdb/peeringdb/issues/942) | Fixes a big that prevented PeeringDB Admins from merging organizations. |
| [#960 Change any "Primary ASN" to "ASN"](https://github.com/peeringdb/peeringdb/issues/960) | Replaces the phrase "Primary ASN" with "ASN" everywhere as the Primary ASN concept does not exist in PeeringDB 2.0. |
| [#986 Add link to release notes to the footer of www.peeringdb.com](https://github.com/peeringdb/peeringdb/issues/986) | Release notes are now linked from the footer, making them easier for all users to find. |

## Release 2.36.0

Beta Announcement Date: 13 April 2022
Release Date: 11 May 2022

| **GitHub Issue** | **Summary** |
| ----------------- | ----------- |
| [peeringdb-py #62 Support User & Org API keys](https://github.com/peeringdb/peeringdb-py/issues/62) | Adds API keys support for the peeringdb-py cacheing client. |
| [#1079 Normalize the names of states & provinces for various objects](https://github.com/peeringdb/peeringdb/issues/1079) | Normalizes names for states and provinces, improving search experience. |
| [#784 Do not show objects in status "pending" on the UI](https://github.com/peeringdb/peeringdb/issues/784) | Objects that do not have an OK status are no longer returned in search results. |
| [#996 500 Error during login for 2FA enabled accounts with unverified email address](https://github.com/peeringdb/peeringdb/issues/996) | Fixes a bug that generated a 500 error when logging in with an account whose e-mail address had not been verified. |
| [#845 Need consolidated app logs](https://github.com/peeringdb/peeringdb/issues/845) | Improvements to logging. |
| [#1119 Some command-line-tool executions are not logged](https://github.com/peeringdb/peeringdb/issues/1119) | Improves logging so AC tools can undo actions. |
| [#1120 Ops: response header X-Auth-ID to augment logging](https://github.com/peeringdb/peeringdb/issues/1120) | Logs the user for requested authenticated by API keys allowing them to be contacted. |
| [#1121 Ops: API throttling needs customizable messages](https://github.com/peeringdb/peeringdb/issues/1121) | API requests can now be throttled with custom return code (HTTP 429). |
| [#1122 Logging for melissa (geo-address normalization) queries](https://github.com/peeringdb/peeringdb/issues/1122) | Adds support for logging geosearch queries to the external API. |
| [#1124 Allow rate-limiting of melissa enabled api functionality.](https://github.com/peeringdb/peeringdb/issues/1124) | Adds support for rate-limiting the geosearch features that rely on an external API. |
| [#1126 Ops: API throttling of repeated requests](https://github.com/peeringdb/peeringdb/issues/1126) | Adds support for throttling repeated requests. |
| [#1096 Clicking on Facility history in AC GUI throws 500](https://github.com/peeringdb/peeringdb/issues/1096) | Fixes a bug that hid `fac` history. |
| [#1035 Django-Admin: adding a network with existing asn fails with internal error](https://github.com/peeringdb/peeringdb/issues/1035) | Fixes a bug that returned a 500 error when a user attempted to add a `net` with the same ASN as an existing object. It now returns a more helpful validation error. |

## Release 2.35.0

Beta Announcement Date: 8 March 2022
Release Date: 22 March 2022

| **GitHub Issue** | **Summary** |
| ----------------- | ----------- |
| [#506 Add "Management" search field to Advanced Search of Exchanges](https://github.com/peeringdb/peeringdb/issues/506) | Allows users to search for IXPs based on the organization that operates the IXP. |
| [#727 RS Peer Checkbox also visible on IX Site](https://github.com/peeringdb/peeringdb/issues/727) | Information about networks claiming to peer with the Route Server is now shown on the IXP's page. |
| [#512 New Field "Health Check"](https://github.com/peeringdb/peeringdb/issues/512) | Networks, IXPs, and Facilities can now link to a status dashboard page. |
| [#653 missing delete button for user](https://github.com/peeringdb/peeringdb/issues/653) | There is now a button to delete a user account directly through the web interface. |
| [#656 Sort user IDs in https://www.peeringdb.com/cp/peeringdb_server/userpermission/xxxxx numerically](https://github.com/peeringdb/peeringdb/issues/656) | Fixes the sorting order of user IDs, so they are now sorted in numerical order. |
| [#881 wrap correctly on mobile](https://github.com/peeringdb/peeringdb/issues/881) | The ASN column on mobile view will show seven digits before wrapping the number. |
| [#908 2FA Backup Tokens language doesn't seem correct](https://github.com/peeringdb/peeringdb/issues/908) | Fixes the backup tokens language for 2FA. |
| [#916 To force or not to force www, that is a question](https://github.com/peeringdb/peeringdb/issues/916) | Forces https://www.peeringdb.com as the URL for PeeringDB, enabling other improvements. Some clients will need to adjust their endpoints to use www.peeringdb.com. `curl` users will want to use the `-L` flag. |
| [#1042 Long caching of deleted entries](https://github.com/peeringdb/peeringdb/issues/1042) | Fixes a problem where deleted objects continued to be returned because of cacheing. |
| [#1117 Bad API keys need to return 401 just like a bad user/pass. Presently they return 200](https://github.com/peeringdb/peeringdb/issues/1117) | Fixes a problem where corrupt or expired or bogus API key simply resulted in an anonymous user session. |

## Release 2.34.0

Beta Announcement Date: 9 February 2022
Release Date: 16 February 2022

| **GitHub Issue** | **Summary** |
| ----------------- | ----------- |
| [#722 Create a validation tool for syntactically well defined fields](https://github.com/peeringdb/peeringdb/issues/722) | Introduces a tool to improve data quality by validating syntactically well defined fields. |
| [#853 substantially rate limit unauthenticated /api/ queries to encourage authenticated queries](https://github.com/peeringdb/peeringdb/issues/853) | Introduces rate limiting for unauthenticated API queries to reduce the possibility of service impacting queries. |
| [#620 Add organisations and registered users to "Global System Statistics" in footer](https://github.com/peeringdb/peeringdb/issues/620) | Adds the number of registered users to the footer, giving users a better idea of the size of the interconnection community. |

## Release 2.33.0

Beta Announcement Date: 12 January 2022
Release Date: 19 January 2022

| **GitHub Issue** | **Summary** |
| ----------------- | ----------- |
| [#1083 Nanog 83 Hackathon improvements to the PeeringDB Website](https://github.com/peeringdb/peeringdb/issues/1083) | When using simple search on the front page of www.peeringdb.com (or via the API) searches for numbers return the most relevant results. Key changes include: searching for a short ASN returns just that network, and searches for two segments of an IP address are required to return related `ix` and `net` objects. |
| [#1070 OpenID Connect integration](https://github.com/peeringdb/peeringdb/issues/1070) | Allows organizations using PeeringDB to enable an identity federation with a managed service. |
| [#692 Add FIDO U2F 2FA support](https://github.com/peeringdb/peeringdb/issues/692) | Adds support for FIDO U2F hardware tokens, allowing users to enable 2FA without relying on a TOTP app. |
| [#1033 Clicking "Add" to add a user api-key without providing a name for the key raises Internal Error](https://github.com/peeringdb/peeringdb/issues/1033) | Fixes a bug where unnamed user api-keys could not be added and there was just an internal error. |
| [#374 make URL required for new objects](https://github.com/peeringdb/peeringdb/issues/374) | A URL to a website is now required when adding new objects. |
| [#469 Add IXP to AS record / dropdown limited](https://github.com/peeringdb/peeringdb/issues/469) | Fixes a bug that limited the number of entries in the dropdown menu when adding an `ix` to a `net`. |
| [#284 global stats don't show up at login screen](https://github.com/peeringdb/peeringdb/issues/284) | Global stats are now shown at the login web page. |
| [#874 Better error message when entering the wrong password for email change](https://github.com/peeringdb/peeringdb/issues/874) | Improved the error message when entering the wrong password for an e-mail change. |
| [#365 Username retrieval non-existant email bug](https://github.com/peeringdb/peeringdb/issues/365) | Fixes a bug where we attempted to send mail to non-existant addresses. |
| [#735 Cascade delete when performed by superuser](https://github.com/peeringdb/peeringdb/issues/735) | Admin users can now cascade delete through the admin interface. |
| [#901 Creating a facility that matches the name of a soft-deleted facility will cause the entry to bypass the verification queue](https://github.com/peeringdb/peeringdb/issues/901) | Fixes a bug where `fac` creation could bypass the validation process. |
| [#921 irr source validator doesn't allow for hyphens in source](https://github.com/peeringdb/peeringdb/issues/921) | IRRs with a hyphen in the name, like ARIN-NONAUTH, are now supported. |
| [#1060 "HARAKIRI ON WORKER" issues need to be resolved](https://github.com/peeringdb/peeringdb/issues/1060) | Fixes an operational issue. |
| [#1062 Registering a new facility or exchange organization is broken](https://github.com/peeringdb/peeringdb/issues/1062) | Fixes a bug that prevented new `fac` and `ix` objects to be registered. |
| [#1077 Possible for "pending" exchange to have "deleted" ixlan](https://github.com/peeringdb/peeringdb/issues/1077) | Fixes a bug that allowed linked `ix` objects to jhave a different status, affecting API sync. |
| [#1088 Tweaks for empty organization clean up](https://github.com/peeringdb/peeringdb/issues/1088) | Fixes a bug that allowed sponsor organizations to be deleted by an automatic process when they should not be. |

## Older releases

* [2021 Release Notes](/release_notes/release_notes_2021/)
* [2020 Release Notes](/release_notes/release_notes_2020/)
