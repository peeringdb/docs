# Release Notes and Schedule

The release notes list the GitHub issues and a summary of what has changed in PeeringDB software releases.

Each new release has a one week beta test period on the [beta server](https://beta.peeringdb.com/) before it goes live.  The beta and new releases are announced on the [PeeringDB Announce Mailing List](https://lists.peeringdb.com/cgi-bin/mailman/listinfo/pdb-announce) and on [Facebook](https://www.facebook.com/peeringdb), [LinkedIn](https://www.linkedin.com/company/peeringdb) and [X](https://twitter.com/PeeringDB).

## Release schedule

This schedule provides planned dates for PeeringDB’s future releases. We are sharing these dates to help PeeringDB users plan ahead for testing new and improved features in beta. We also want to help volunteer developers know the date on which their code changes are needed for internal testing before beta release.

We provide a rolling schedule. Dates can change, so if you have a question or request please contact us at: [support@peeringdb.com](mailto:support@peeringdb.com).

Our releases are generally deployed at around 04:00 UTC.

| **Release number** | **Internal testing** | **Beta release** | **Production release** |
| -------------- | ---------------- | ------------ | ------------------ |
| 2.65.0 | 2025-02-05 | 2025-02-12 | 2025-02-19 |
| 2.66.0 | 2025-03-14 | 2025-03-23 | 2025-03-30 |
| 2.67.0 | 2025-04-22 | 2025-04-29 | 2025-04-30 |
| 2.68.0 | 2025-05-07 | 2025-05-14 | 2025-05-21 |
| 2.69.0 | 2025-06-11 | 2025-06-18 | 2025-05-25 |

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
