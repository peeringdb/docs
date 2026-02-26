# Release Notes and Schedule

The release notes list the GitHub issues and a summary of what has changed in PeeringDB software releases.

Each new release has a one week beta test period on the [beta server](https://beta.peeringdb.com/) before it goes live.  The beta and new releases are announced on the [PeeringDB Announce Mailing List](https://lists.peeringdb.com/cgi-bin/mailman/listinfo/pdb-announce) and on [Facebook](https://www.facebook.com/peeringdb), [LinkedIn](https://www.linkedin.com/company/peeringdb) and [X](https://x.com/PeeringDB).

## Release schedule

This schedule provides planned dates for PeeringDB’s future releases. We are sharing these dates to help PeeringDB users plan ahead for testing new and improved features in beta. We also want to help volunteer developers know the date on which their code changes are needed for internal testing before beta release.

We provide a rolling schedule. Dates can change, so if you have a question or request please contact us at: [support@peeringdb.com](mailto:support@peeringdb.com).

Our releases are generally deployed at around 04:00 UTC.

| **Release number** | **Internal testing** | **Beta release** | **Production release** |
| -------------- | ---------------- | ------------ | ------------------ |
| 2.77.0 | 2026-03-03 | 2026-03-11 | 2026-03-18 |
| 2.78.0 | 2026-04-13 | 2026-04-22 | 2026-04-29 |
| 2.79.0 | 2026-05-05 | 2026-05-13 | 2026-05-20 |
| 2.80.0 | 2026-06-08 | 2026-06-17 | 2026-06-24 |

## Release 2.76.1

Release Date: 26 February 2026

| **GitHub issue** | **Summary** |
| ----------------- | ----------- |
| [#1905 Support 202601 Fixes.](https://github.com/peeringdb/peeringdb/pull/1905) | Fix issue where redis unavailable during negative cache checks could lead to cascading failures.|

## Release 2.76.0

Beta Announcement Date: 18 February 2026
Release Date: 25 February 2026

| **GitHub issue** | **Summary** |
| ----------------- | ----------- |
| [#1849 Add rate limiting for unauthenticated web pages queries.](https://github.com/peeringdb/peeringdb/issues/1849) | As title.|
| [#1846 Page load time dramatically goes up when limiting queries.](https://github.com/peeringdb/peeringdb/issues/1846) | Improves page load time for complex queries.|
| [#1844 Exclude AC members from rate limiting.](https://github.com/peeringdb/peeringdb/issues/1844) | As title.|
| [#1814 Improve Passkey or Security Key login flow.](https://github.com/peeringdb/peeringdb/issues/1814) | As title.|
| [#1889 Security key setup fails on some conditions.](https://github.com/peeringdb/peeringdb/issues/1889) | Fixes a bug where adding a security key before TOTP failed.|
| [#1830 Remove "Require users in your organization to enable 2FA." radio button from Org > Users tab.](https://github.com/peeringdb/peeringdb/issues/1830) | Clean up web UI now MFA is mandatory.|
| [#1855 No way to check if an API key has been created read-only or not.](https://github.com/peeringdb/peeringdb/issues/1855) | Make API Key  permissions visible.|
| [#1870 Ctl/local/setup.sh: input data doesn't fit schema limits.](https://github.com/peeringdb/peeringdb/issues/1870) | Fixes bug that stopped installation of self-hosted instances.|
| [peeringdb-py #133 Field Mismatch Between Cache and Official API.](https://github.com/peeringdb/peeringdb-py/issues/133) | As title.|
| [#1876 UI Inconsistency in Filter Selection (ASN Connectivity Search).](https://github.com/peeringdb/peeringdb/issues/1876) | Web UI improvements for ASN Conectivity searches.|
| [#1862 Cannot upload .png logo.](https://github.com/peeringdb/peeringdb/issues/1862) | Fixes a bug for logos.|
| [#1834 Reverse action order for export interstitial and add color to button.](https://github.com/peeringdb/peeringdb/issues/1834) | Improve web UI grammar for action buttons.|
| [#1838 Affiliation requires ASN, but text on page suggests it isn't required.](https://github.com/peeringdb/peeringdb/issues/1838) | Fixes text to align with policy.|
| [#1779 New web UI is missing "Port Location" field under "Public Peering Exchange Points".](https://github.com/peeringdb/peeringdb/issues/1779) | As title.|
| [#1871 facmerge tool broken as of release 2.68.0.](https://github.com/peeringdb/peeringdb/issues/1871) | Fixes the facmerge tool.|
| [#1499 Stop Ticket Opening Post Object Creation (anti-automat).](https://github.com/peeringdb/peeringdb/issues/1499) | As title.|

## Release 2.75.0

Beta Announcement Date: 22 January 2026
Release Date: 28 January 2026

| **GitHub issue** | **Summary** |
| ----------------- | ----------- |
| [#1822 Integration Testing with Live Elasticsearch.](https://github.com/peeringdb/peeringdb/issues/1822) | Improvements to testing for search.|
| [#1850 Search for network name doesn't work if it contains only digits.](https://github.com/peeringdb/peeringdb/issues/1850) | As title.|
| [#1833 Search for ix in Vietnam gives bad results #1833.](https://github.com/peeringdb/peeringdb/issues/1833) | As title.|
| [#1787 Search fails to identify ALL IX's in fast search option.](https://github.com/peeringdb/peeringdb/issues/1787) | As title.|
| [#1852 Network creation only tests primary e-mail address against IRR records (Issue #1852).](https://github.com/peeringdb/peeringdb/issues/1852) | Adds checks against all addresses when creating a new network.|
| [#1821 Remove default country setting from "Add Exchange" form.](https://github.com/peeringdb/peeringdb/issues/1821) | As title, used to default to USA.|
| [#1605 Unable to save Organization API key permissions for Carrier objects.](https://github.com/peeringdb/peeringdb/issues/1605) | As title.|
| [#1845 Undeleting a network when the parent org is still deleted results in unhelpful 500 error message.](https://github.com/peeringdb/peeringdb/issues/1845) | As title.|
| [#1847 Carrier is missing numbers in overview if there is none.](https://github.com/peeringdb/peeringdb/issues/1847) | As title.|
| [#1640 Add carrier_count to fac object.](https://github.com/peeringdb/peeringdb/issues/1640) | As title.|
| [#1821 Remove default country setting from "Add Exchange" form.](https://github.com/peeringdb/peeringdb/issues/1821) | As title.|
| [#1851 tutorial webserver is broken.](https://github.com/peeringdb/peeringdb/issues/1851) | Fixes for remaining tutorial server issues.|


## Older releases

* [2025 Release Notes](/release_notes/release_notes_2025/)
* [2024 Release Notes](/release_notes/release_notes_2024/)
* [2023 Release Notes](/release_notes/release_notes_2023/)
* [2022 Release Notes](/release_notes/release_notes_2022/)
* [2021 Release Notes](/release_notes/release_notes_2021/)
* [2020 Release Notes](/release_notes/release_notes_2020/)
