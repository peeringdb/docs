# Release Notes and Schedule

The release notes list the GitHub issues and a summary of what has changed in PeeringDB software releases.

Each new release has a one week beta test period on the [beta server](https://beta.peeringdb.com/) before it goes live.  The beta and new releases are announced on the [PeeringDB Announce Mailing List](https://lists.peeringdb.com/cgi-bin/mailman/listinfo/pdb-announce) and on [Facebook](https://www.facebook.com/peeringdb), [LinkedIn](https://www.linkedin.com/company/peeringdb) and [X](https://twitter.com/PeeringDB).

## Release schedule

This schedule provides planned dates for PeeringDB’s future releases. We are sharing these dates to help PeeringDB users plan ahead for testing new and improved features in beta. We also want to help volunteer developers know the date on which their code changes are needed for internal testing before beta release.

We provide a rolling schedule. Dates can change, so if you have a question or request please contact us at: [support@peeringdb.com](mailto:support@peeringdb.com).

Our releases are generally deployed at around 04:00 UTC.

| **Release number** | **Internal testing** | **Beta release** | **Production release** |
| -------------- | ---------------- | ------------ | ------------------ |
| 2.70.0 | 2025-07-16 | 2025-07-23 | 2025-07-30 |
| 2.71.0 | 2025-08-13 | 2025-08-20 | 2025-08-27 |
| 2.72.0 | 2025-09-10 | 2025-09-17 | 2025-09-24 |
| 2.73.0 | 2025-10-08 | 2025-10-15 | 2025-10-29 |
| 2.70.0 | 2025-11-05 | 2025-11-12 | 2025-11-19 |

## Release 2.70.0

Beta Announcement Date: 23 July 2025
Release Date: 30 July 2025

| **GitHub issue** | **Summary** |
| ----------------- | ----------- |
| [#1574 Add comparison function to assess datacenter connectivity attractiveness.](https://github.com/peeringdb/peeringdb/issues/1574) | New feature to compare `fac`s.|
| [#1697 IPv6 addresses are overlapping with the new IX-Port location information.](https://github.com/peeringdb/peeringdb/issues/1697) | Fixed bug is data table display.|
| [#1788 Sorting "Public Peering Exchange Points" of a "net" by "RS Peer" column actually sorts by "Speed" column.](https://github.com/peeringdb/peeringdb/issues/1788) | Fixed bug as per title.|
| [#1642 Advanced Search Fails on Address Search.](https://github.com/peeringdb/peeringdb/issues/1642) | Fixed bug where address searches failed.|
| [#1655 Advanced search doesn't find DC in Turin.](https://github.com/peeringdb/peeringdb/issues/1655) | Fixed bug where some `fac` results were missing.|
| [#1748 Social Media links - Add Bluesky, Youtube, Others?.](https://github.com/peeringdb/peeringdb/issues/1748) | Added support for links to a wide range of social media platforms.|
| [#804 [beta] Add ixf_ixp_import_enabled to object ixlan API.](https://github.com/peeringdb/peeringdb/issues/804) | As title.|
| [#1791 Unable to change netmask for ixlan when the network address is unchanged.](https://github.com/peeringdb/peeringdb/issues/1791) | Fixed bug preventing `ix`s from expanding a peering LAN prefix from e.,g. a /24 to a /23.|
| [#1790 New WebUI - I can't modify "Public Peering Exchange Points" details.](https://github.com/peeringdb/peeringdb/issues/1790) | Fixed bug as per title.|
| [#1771 UI - Runaway window close control .](https://github.com/peeringdb/peeringdb/issues/1771) | Fixed a bug as per title.|
| [#1802 Search results and sponsorships badges.](https://github.com/peeringdb/peeringdb/issues/1802) | Sponsor badges no appear for `org` objects only in search results.|
| [#926 Unit test performance degradation.](https://github.com/peeringdb/peeringdb/issues/926) | Tests now run at the normal speed again.|

## Release 2.69.0

Beta Announcement Date: 18 June 2025
Release Date: 25 June 2025

| **GitHub issue** | **Summary** |
| ----------------- | ----------- |
| [#1634 Force MFA on all users.](https://github.com/peeringdb/peeringdb/issues/1634) | Preparations for enforcing MFA mandate.|
| [#1630 Allow facilties to be added from facility page directly.](https://github.com/peeringdb/peeringdb/issues/1630) | As title.|
| [#1756 Update "operational" ⚠ indicator with mouseover tooltip.](https://github.com/peeringdb/peeringdb/issues/1756) | Fixed broken tooltip.|

## Release 2.68.0

Beta Announcement Date: 14 May 2025
Release Date: 21 May 2025

| **GitHub issue** | **Summary** |
| ----------------- | ----------- |
| [#1705 Start moving users to new web UI.](https://github.com/peeringdb/peeringdb/issues/1705) | Phased introduction of new webUI: volunteers first, then a randomly selected 20% (with opt-out), then everyone.|
| [#1737 Normalization for street addresses.](https://github.com/peeringdb/peeringdb/issues/1737) | Street address formatting g is now normalized.|
| [#1682 The IX {sales,tech}_phone field is not E.164 checked/formatted.](https://github.com/peeringdb/peeringdb/issues/1682) | E.164 formatting is now enforced.|
| [#1614 IX-F importer ignores changes in connection speed.](https://github.com/peeringdb/peeringdb/issues/1614) | Connection speed updates are now processed when "Allow IXP Update" is configured.|
| [#1639 IX-F Importer: Enhance error message.](https://github.com/peeringdb/peeringdb/issues/1639) | Error message now includea a reference to the key_id of the object failing validation.|
| [#1757 ipaddr4 ixpfx mismatch.](https://github.com/peeringdb/peeringdb/issues/1757) | Fixed bug so they now match.|
| [#1145 NetworkFacility local_asn complete transition to read-only property.](https://github.com/peeringdb/peeringdb/issues/1145) | As title.|
| [#1719 Allowed Origins field not visible when clicking "edit" in OAuth application view.](https://github.com/peeringdb/peeringdb/issues/1719) | Fixed bug, field is now editable.|
| [#1732 Firefox always shows the scroll bar in dark colors.](https://github.com/peeringdb/peeringdb/issues/1732) | Fixed bug for Firefox scrollbars.|

## Release 2.67.0

Beta Announcement Date: 23 April 2025
Release Date: 30 April 2025

| **GitHub issue** | **Summary** |
| ----------------- | ----------- |
| [#1534 Enable Regular Beta Data Refresh.](https://github.com/peeringdb/peeringdb/issues/1534) | Data is now synced to beta.peeringdb.com more regularly, making beta more attractive for searching and testing.|
| [#1726 Port Advanced Search to v2.](https://github.com/peeringdb/peeringdb/issues/1726) | Advanced Search now uses the v2 search code.|
| [#1711 Rename capacity to speed within Advanced Search in UI.](https://github.com/peeringdb/peeringdb/issues/1711) | As title.|
| [#1739 Port speed is corrupted when editing multiple ports.](https://github.com/peeringdb/peeringdb/issues/1739) | Fixed bug as per title.|
| [#1720 Users with email-based 2FA do not show the 2FA label in the organization user view.](https://github.com/peeringdb/peeringdb/issues/1720) | Label is now added to users relying on mail for 2FA.|
| [#1729 Add affiliation at affiliation request/denial.](https://github.com/peeringdb/peeringdb/issues/1729) | User and org are both listed in affiliation requests now.|
| [#1733 Sponsorship level font colors are wrong on the search page vs. the record page.](https://github.com/peeringdb/peeringdb/issues/1733) | As title.|
| [#1658 Net and ixlan keys missing in netixlan API response.](https://github.com/peeringdb/peeringdb/issues/1658) | As title.|
| [#1116 Intermittent json errors with cached api responses.](https://github.com/peeringdb/peeringdb/issues/1116) | Fixed bug as per title.|
| [#1730 Server error on getting ixf_ixp_member_list_url.](https://github.com/peeringdb/peeringdb/issues/1730) | Fixed bug as per title.|
| [#1678 remove PeeringDB v1 password hashers.](https://github.com/peeringdb/peeringdb/issues/1678) | Remove legacy hashers from v1.|
| [#972 Clean up facilities and ixes in verification queue.](https://github.com/peeringdb/peeringdb/issues/972) | As title.|
| [#1710 Fix/update org merger tool.](https://github.com/peeringdb/peeringdb/issues/1710) | As title.|

## Release 2.66.1

Release Date: 3 April 2025

| **GitHub issue** | **Summary** |
| ----------------- | ----------- |
| [#1753 fix anon user search autocomplete error.](https://github.com/peeringdb/peeringdb/pull/1753) | As title.|

## Release 2.66.0

Beta Announcement Date: 12 March 2025
Release Date: 19 March 2025

| **GitHub issue** | **Summary** |
| ----------------- | ----------- |
| [#1701 Continuously enforce place name normalization.](https://github.com/peeringdb/peeringdb/issues/1701) | Normalization of place names is now enforced.|
| [#1689 Profile setting: hide IXs where fac_count == 0.](https://github.com/peeringdb/peeringdb/issues/1689) | Users can now hide exchanges without a `facix` from search results by selecting a profile setting.|
| [#1547 Enable non-disclosure of the number of "IPv4 Prefixes" and/or "IPv6 Prefixes" in the net object.](https://github.com/peeringdb/peeringdb/issues/1547) | Networks can now indicate that they do not share their prefix count.|
| [#1708 Web search > API query link.](https://github.com/peeringdb/peeringdb/issues/1709) | Click a link to put the API query for a web search into your copy buffer.|
| [#1727 new search is not using AKA field.](https://github.com/peeringdb/peeringdb/issues/1727) | Fixes a bug, so search uses AKA field again.|
| [#1689 Integrate 2FA methods into a single web UI.](https://github.com/peeringdb/peeringdb/issues/1689) | Improved web interface for managing 2FA settings.|
| [#1680 POC for Internet Exchange Point IX-F Import Errors.](https://github.com/peeringdb/peeringdb/issues/1680) | Adds a new point of contact type for exchange operators. They can now add a contact to be notified about problems with their [IX-F JSON](https://github.com/euro-ix/json-schemas) imports.|

## Release 2.65.0

Beta Announcement Date: 12 February 2025
Release Date: 19 February 2025

| **GitHub issue** | **Summary** |
| ----------------- | ----------- |
| [#1713 IX-F Importer previews are timing out after 5 seconds.](https://github.com/peeringdb/peeringdb/issues/1713) | Bug fix: as per title.|
| [#1660 IX-F import requested in the Beta instance remains in the Queued state](https://github.com/peeringdb/peeringdb/issues/1660) | Fixes a bug that stopped IX-F imports to beta completing.|
| [#1663 Display issue: approved by text in approval email](https://github.com/peeringdb/peeringdb/issues/1663) | The name of the approver is now included in approval mails.|
| [#1718 Delete Affiliation uses the wrong dropdown](https://github.com/peeringdb/peeringdb/issues/1718) | Bug fix: as per title.|
| [#1586 Django admin date selector month "Next" and "Prev" emojis/glyphs are missing/invisible](https://github.com/peeringdb/peeringdb/issues/1586) | Makes backend admin controls visible to Admin Committee users.|
| [#1706 Admin Control Panel: viewing ixlan results in 504 Gateway Time-out](https://github.com/peeringdb/peeringdb/issues/1706) | Bug fix: as per title.|

## Release 2.64.0

Beta Announcement Date: 15 January 2025
Release Date: 22 January 2025

| **GitHub issue** | **Summary** |
| ----------------- | ----------- |
| [#1522 Request: A Light/Dark/Auto Mode Toggle](https://github.com/peeringdb/peeringdb/issues/1522) | Introduces Dark Mode and use controls for it.|
| [#1446 v2 Search - extra facility results are returned with exact match search](https://github.com/peeringdb/peeringdb/issues/1446) | Fixes a problem with exact matches in search.|
| [#1517 Searching for an AS number returns less than helpful search results](https://github.com/peeringdb/peeringdb/issues/1517) | Improves search results for AS Numbers.|
| [#1542 v2 search does not find a fac in Charlotte, NC but finds an ix in a fac there](https://github.com/peeringdb/peeringdb/issues/1542) | Improves completeness for location based searches.|
| [#1596 Improvements to search](https://github.com/peeringdb/peeringdb/issues/1596) | Several search improvements.|
| [#1646 Valid search syntax fails to return complete results as expected](https://github.com/peeringdb/peeringdb/issues/1646) | Improves completeness for location based searches.|
| [#1473 Searching for specific facilities (so far Equinix) returns incorrect results](https://github.com/peeringdb/peeringdb/issues/1473) | Improves results for specific facility or IXP searches.|
| [#1704 Advanced Search for Carriers - web UI and data export ](https://github.com/peeringdb/peeringdb/issues/1704) | Improves Advanced Search for Carriers and fixes data export options.|
| [#1628 Search failure for FAC and "diverse serving substations"](https://github.com/peeringdb/peeringdb/issues/1628) | Fixes a problem with advanced search for facilities.|
| [#1712 Search doesn't work](https://github.com/peeringdb/peeringdb/issues/1712) | Fixes a bug with Advanced Search for facilities.|
| [#1659 API key cannot be used to retrieve IX-F import preview](https://github.com/peeringdb/peeringdb/issues/1659) | API Keys can now be used to get previews of IX-F imports.|
| [#1482 Clarify location inside of ORG-a-building](https://github.com/peeringdb/peeringdb/issues/1482) | Floor and suite fields aren't included in output address when not specified. Suite is used when a location within a building is documented.|
| [#1687 Create a "profile" control for changing a person's name](https://github.com/peeringdb/peeringdb/issues/1687) | Users may not change their names themselves, instead of asking the AC to do it for them.|
| [#1674 "[peeringdb.com] Please Confirm Your Email Address" messages should present an https:// URL](https://github.com/peeringdb/peeringdb/issues/1674) | Changes URL to use HTTPS.|
| [#1665 Be specific and correct about login field case sensitivity in error message](https://github.com/peeringdb/peeringdb/issues/1665) | Fixes wording for login pages.|
| [#1652 Django-admin allows setting an ok object back to pending.](https://github.com/peeringdb/peeringdb/issues/1652) | Fixes an internal admin UI issues that allowed objects to be unapproved.|

## Older releases

* [2024 Release Notes](/release_notes/release_notes_2024/)
* [2023 Release Notes](/release_notes/release_notes_2023/)
* [2022 Release Notes](/release_notes/release_notes_2022/)
* [2021 Release Notes](/release_notes/release_notes_2021/)
* [2020 Release Notes](/release_notes/release_notes_2020/)
