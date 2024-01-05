# Release Notes and Schedule

The release notes list the GitHub issues and a summary of what has changed in PeeringDB software releases.

Each new release has a one week beta test period on the [beta server](https://beta.peeringdb.com/) before it goes live.  The beta and new releases are announced on the [PeeringDB Announce Mailing List](https://lists.peeringdb.com/cgi-bin/mailman/listinfo/pdb-announce) and on [Facebook](https://www.facebook.com/peeringdb), [LinkedIn](https://www.linkedin.com/company/peeringdb) and [X](https://twitter.com/PeeringDB).

## Release schedule

This schedule provides planned dates for PeeringDB’s future releases. We are sharing these dates to help PeeringDB users plan ahead for testing new and improved features in beta. We also want to help volunteer developers know the date on which their code changes are needed for internal testing before beta release.

We provide a rolling schedule. Dates can change, so if you have a question or request please contact us at: [support@peeringdb.com](mailto:support@peeringdb.com).

Our releases are generally deployed at around 04:00 UTC.

| **Release number** | **Internal testing** | **Beta release** | **Production release** |
| -------------- | ---------------- | ------------ | ------------------ |
| 2.54.0 | 2024-01-09 | 2024-01-16 | 2024-01-24 |
| 2.55.0 | 2024-02-07 | 2024-02-14 | 2024-02-21 |
| 2.56.0 | 2024-03-06 | 2024-03-13 | 2024-03-20 |

## Release 2.54.0

Beta Announcement Date: 16 January 2024
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
