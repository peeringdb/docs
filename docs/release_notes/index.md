# Release Notes and Schedule

The release notes list the GitHub issues and a summary of what has changed in PeeringDB software releases.

Each new release has a one week beta test period on the [beta server](https://beta.peeringdb.com/) before it goes live.  The beta and new releases are announced on the [PeeringDB Announce Mailing List](https://lists.peeringdb.com/cgi-bin/mailman/listinfo/pdb-announce) and on [Facebook](https://www.facebook.com/peeringdb), [LinkedIn](https://www.linkedin.com/company/peeringdb) and [X](https://twitter.com/PeeringDB).

## Release schedule

This schedule provides planned dates for PeeringDB’s future releases. We are sharing these dates to help PeeringDB users plan ahead for testing new and improved features in beta. We also want to help volunteer developers know the date on which their code changes are needed for internal testing before beta release.

We provide a rolling schedule. Dates can change, so if you have a question or request please contact us at: [support@peeringdb.com](mailto:support@peeringdb.com).

Our releases are generally deployed at around 04:00 UTC.

| **Release number** | **Internal testing** | **Beta release** | **Production release** |
| -------------- | ---------------- | ------------ | ------------------ |
| 2.58.0 | 2024-05-21 | 2024-05-29 | 2024-06-05 |
| 2.59.0 | 2024-06-12 | 2024-06-19 | 2024-06-26 |
| 2.60.0 | 2024-07-10 | 2024-07-17 | 2024-07-24 |

## Release 2.58.0

Beta Announcement Date: 29 May 2024
Release Date: 5 June 2024

| **GitHub issue** | **Summary** |
| ----------------- | ----------- |
| [#1343 Inconsistent return results when querying facilities by state (Datafill)](https://github.com/peeringdb/peeringdb/issues/1343) | Enforces state naming on validation and normalize data.|
| [#1502 Create preview.peeringdb.com with updated web UI](https://github.com/peeringdb/peeringdb/issues/1502) | Preview site for new PeeringDB web design.|
| [#1414 Tooltip with Full IX Name on Mouse-Over IX-Abbreviation](https://github.com/peeringdb/peeringdb/issues/1414) | As title.|
| [#1115 Enhancement to Ownership Information Field](https://github.com/peeringdb/peeringdb/issues/1115) | Lessee tooltip now says "Leased or Rented".|
| [#1487 URL Referrer Behavior](https://github.com/peeringdb/peeringdb/issues/1487) | Clicking on a link now opens it in a new tab or window.|
| [#840 Add help text to "Traffic Levels"](https://github.com/peeringdb/peeringdb/issues/840) | Add tooltip "Total, self-classified traffic in/out to this network.".|
| [#1491 Add logo watermark and peeringdb.com URL to kmz](https://github.com/peeringdb/peeringdb/issues/1491) | As title.|
| [#975 "Incomplete data" complainer for Peering Policy even with General Policy "None" or "Open"](https://github.com/peeringdb/peeringdb/issues/975) | No longer show missing data warning for empty Peering Policy field if General Policy is set to "Open" or "No".|
| [#1580 Validator: Add validator for X usernames, were requirements](https://github.com/peeringdb/peeringdb/pull/1580) | Validator for usernames on the X social media network.|
| [#1481 Network Registration fail results in AC action and retry failure](https://github.com/peeringdb/peeringdb/issues/1481) | Improved network registration process where email address does not match RDAP output.|
| [#1500 pdb_stats needs to be updated to include Campuses, Carriers, etc. & possible bug with user counts](https://github.com/peeringdb/peeringdb/issues/1500) | Improvements to internal stats package.|
| [#1503 Is it possible to create an affiliation request even when the ASN (~Net) has been deleted? (But the ORG still exist)](https://github.com/peeringdb/peeringdb/issues/1503) | As title.|
| [#1038 add default for config key](https://github.com/peeringdb/peeringdb/issues/1038) | MELISSA_KEY now defaults to a blank string.|
| [#1048 TOTP devices sort is by id. However, only username is shown](https://github.com/peeringdb/peeringdb/issues/1048) | Fixes a UI bug with internal support tools.|
| [#85 DB sync fails due to duplicate entries](https://github.com/peeringdb/peeringdb-py/issues/85) | Fixes a [peeringdb-py](https://docs.peeringdb.com/howto/peeringdb-py/) data sync bug.|

## Release 2.57.0

Beta Announcement Date: 17 April 2024
Release Date: 24 April 2024

| **GitHub issue** | **Summary** |
| ----------------- | ----------- |
| [#1545 Feature request: Allow permissions to be given per user on Carrier](https://github.com/peeringdb/peeringdb/pull/1545) | As title.|
| [#1123 Make a Technical POC mandatory when enabling "Allow IXP Update"](https://github.com/peeringdb/peeringdb/pull/1123) | As title.|
| [#1231 Change ix-f to IX-F](https://github.com/peeringdb/peeringdb/pull/1231) | As title.|
| [#1577 Remove more clutter from KMZ Metadata](https://github.com/peeringdb/peeringdb/pull/1577) | Makes data easier to read and slims download size.|
| [#1475 KML Placemark/Point Meta Data Not Displaying Correctly](https://github.com/peeringdb/peeringdb/pull/1475) | Fixes a bug that broke the way metadata displayed for .KMZ pins.|
| [#1546 v2 search: 500 error when last character is a colon](https://github.com/peeringdb/peeringdb/pull/1546) | As title.|
| [#1530 missing search results when doing a city location search for facilities](https://github.com/peeringdb/peeringdb/pull/1530) | Fixes a bug that did not show `fac` entries located in a city in simple search.|
| [#1533 Exchange Advanced search fails and returns bad search data](https://github.com/peeringdb/peeringdb/pull/1533) | Fixes and intermittent Advanced Search failure.|
| [#1451 Cosmetic issue with affiliation emails and double-slash in URL](https://github.com/peeringdb/peeringdb/pull/1451) | Fixes a cosmetic bug in autogenerated support messages.|
| [#1416 Add (PeeringDB Support) after superuser name in public notifications](https://github.com/peeringdb/peeringdb/pull/1416) | Support messages now more clearly identified as coming from PeeringDB Support.|
| [#1415 Auto-CleanUp old pending "User to Organization Affiliation Request"](https://github.com/peeringdb/peeringdb/pull/1415) | Pending affiliation requests are now cleaned up after 3 months.|
| [#1494 drop any facilities without location data (PDB Example)](https://github.com/peeringdb/peeringdb/pull/1494) | No `fac` without a geocode is now listed in the .KMZ export.|
| [#1528 pdb_rir_status task errors on deskpro ticket creation](https://github.com/peeringdb/peeringdb/pull/1528) | Fixes a bug in an internal support tool.|
| [#1453 DELETION PREVENTED: Link is not formatted as <a> html element](https://github.com/peeringdb/peeringdb/pull/1453) | Fixes a bug in an internal support tool.|
| [#1484 Update ORG Social Media Option "Twitter" to "X"](https://github.com/peeringdb/peeringdb/pull/1484) | As title.|

## Release 2.56.1

Release Date: 27 March 2024

| **GitHub issue** | **Summary** |
| ----------------- | ----------- |
| [#1581 rdap to 1.5.2](https://github.com/peeringdb/peeringdb/pull/1581) | Merge third-party library needed for complete fix of [#1455](https://github.com/peeringdb/peeringdb/issues/1455).|

## Release 2.56.0

Beta Announcement Date: 13 March 2024
Release Date: 20 March 2024

| **GitHub issue** | **Summary** |
| ----------------- | ----------- |
| [#1447 v2 search - support for ISO 3166 alpha-2 country codes](https://github.com/peeringdb/peeringdb/issues/1447) | v2 search now has support for ISO 3166 alpha-2 codes.|
| [#1495 Enable .KMZ export for Advanced Search results](https://github.com/peeringdb/peeringdb/issues/1495) | As title.|
| [#1489 Remove unneeded fields from the KMZ](https://github.com/peeringdb/peeringdb/issues/1489) | Removes field clutter to optimize file size.|
| [#1490 Spelling fix for KMZ](https://github.com/peeringdb/peeringdb/issues/1490) |Fixes spelling of 'Latitude'.|
| [#1099 Expose authentication methods on outbound federation](https://github.com/peeringdb/peeringdb/issues/1099) |Adds Authentication Method Reference field to OAuth profile, with choices from [Section 2 of RFC8176](https://www.rfc-editor.org/rfc/rfc8176#section-2), documentation, and scope.|
| [#1133 Return auth error when multiple auth methods are used](https://github.com/peeringdb/peeringdb/issues/1133) |Now returns a 401 code with a helpful message when `Authorization: Basic` fails with corrupt base64 input. |
| [#1456 Duplicate AS-SET name](https://github.com/peeringdb/peeringdb/issues/1456) |Adds a tooltip suggesting hierarchical AS-SET names and a warning if a duplicate name is entered.|
| [#1331 BFD support field in Global and IX specific views](https://github.com/peeringdb/peeringdb/issues/1331) |Adds a boolean value for BFD support per IP address and a mouseover icon on the website when it's true.|
| [#1478 Social link controls showing up when not logged in](https://github.com/peeringdb/peeringdb/issues/1478) |Fixes a cosmetic bug that showed non-operational social media controls when not logged in.|
| [#1425 Update social media icons in footer](https://github.com/peeringdb/peeringdb/issues/1425) |Updates social media icons in the footer.|
| [#1152 Tab URLs don't work anymore](https://github.com/peeringdb/peeringdb/issues/1152) |Fixes tab URLs in the admin interface.|

## Release 2.55.0

Beta Announcement Date: 21 February 2024
Release Date: 28 February 2024

| **GitHub issue** | **Summary** |
| ----------------- | ----------- |
| [#1410 Adjust IPv4/6 prefix limits automatically](https://github.com/peeringdb/peeringdb/issues/1410) |Max prefix limit is now automatically adjusted based on the DFZ.|
| [#1455 Org name RIPE-NCC-END-MNT for new networks](https://github.com/peeringdb/peeringdb/issues/1455) |Fixes a bug that named orgs RIPE-NCC-END-MNT.|
| [#1468 translation refresh and dependency update](https://github.com/peeringdb/peeringdb/issues/1468) |translate.peeringdb.com updated to weblate 5.0 and other dependency updates.|
| [#1480 pdb_load_data no longer creates necessary org usergroups](https://github.com/peeringdb/peeringdb/issues/1480) |Fixes a bug with data sync tool.|

## Release 2.54.2

Release Date: 31 January 2024

| **GitHub issue** | **Summary** |
| ----------------- | ----------- |
| [#1536 Support 202311 rollback ux changes](https://github.com/peeringdb/peeringdb/issues/1536) | Reverted web UI changes that caused issues.|

## Release 2.54.1

Release Date: 30 January 2024

| **GitHub issue** | **Summary** |
| ----------------- | ----------- |
| [#1511 Non-obvious search box on the front page](https://github.com/peeringdb/peeringdb/issues/1511) | Search bar in header is now auto deployed.|
| [#1513 Mobile interface front page has lots of misaligned sections](https://github.com/peeringdb/peeringdb/issues/1513) | Fixes layout issues for some mobile devices.|
| [#1514 Two different search boxes on a network page information page in the same area](https://github.com/peeringdb/peeringdb/issues/1514) | As title.|
| [#1515 Bottom search box on some pages does not work correctly](https://github.com/peeringdb/peeringdb/issues/1515) | As title.|

## Release 2.54.0

Beta Announcement Date: 18 January 2024
Release Date: 24 January 2024

| **GitHub issue** | **Summary** |
| ----------------- | ----------- |
| [#1463 Update website to take advantage of wider screen and improve mobile device support](https://github.com/peeringdb/peeringdb/issues/1463) | As title.|
| [#1357 Clarifying the Network Type field](https://github.com/peeringdb/peeringdb/issues/1357) | Add multi-select for Network Type field.|
| [#1341 Only indicate availability of DC voltage for facilities](https://github.com/peeringdb/peeringdb/issues/1341) | Limits power options to non-standard voltages.|
| [#1476 v2 search not able to find organization and network - Marconi Solutions Srls](https://github.com/peeringdb/peeringdb/issues/1476) | Fixes a bug where bad search results are returned.|
| [#170 Add a "flag bad data" button on various places](https://github.com/peeringdb/peeringdb/issues/170) | Adds a box web users can click to report bad data.|
| [#1430 Changing ASN field on "Add Network" to be numbers only](https://github.com/peeringdb/peeringdb/issues/1430) | The text box is now restricted to numbers, reducing scope for data entry issues.|
| [#1455 Org name RIPE-NCC-END-MNT for new networks](https://github.com/peeringdb/peeringdb/issues/1455) | Fixes a bug tat set some networks' names to RIPE-NCC-END-MNT.|
| [#1280 Improve RIR Update Procedure](https://github.com/peeringdb/peeringdb/issues/1280) | Improves the process for removing stale networks from PeeringDB.|
| [#1065 api-cache improvements](https://github.com/peeringdb/peeringdb/issues/1065) | As title.|
| [#1303 Add headers to API requests](https://github.com/peeringdb/peeringdb/issues/1303) | Adds a mechanism to indicate that behavior/schema has changed to API consumers.|
| [#1410 Adjust IPv4/6 prefix limits automatically](https://github.com/peeringdb/peeringdb/issues/1410) | Now automatically sets the maximum to 25% of the DFZ.|
| [#410 Add a "last synced at $date" to beta.peeringdb.com](https://github.com/peeringdb/peeringdb/issues/410) | As title.|
| [#1468 translation refresh and dependency update](https://github.com/peeringdb/peeringdb/issues/1468) | As title.|
| [#1466 Analysis: Investigate use of ECS/Fargate](https://github.com/peeringdb/peeringdb/issues/1466) | As title.|
| [#1412 Improve performance by updating Python client code](https://github.com/peeringdb/peeringdb/issues/1412) | As title.|

## Older releases

* [2023 Release Notes](/release_notes/release_notes_2023/)
* [2022 Release Notes](/release_notes/release_notes_2022/)
* [2021 Release Notes](/release_notes/release_notes_2021/)
* [2020 Release Notes](/release_notes/release_notes_2020/)
