# Release Notes and Schedule

The release notes list the GitHub issues and a summary of what has changed in PeeringDB software releases.

Each new release has a one week beta test period on the [beta server](https://beta.peeringdb.com/) before it goes live.  The beta and new releases are announced on the [PeeringDB Announce Mailing List](https://lists.peeringdb.com/cgi-bin/mailman/listinfo/pdb-announce) and on [Facebook](https://www.facebook.com/peeringdb), [LinkedIn](https://www.linkedin.com/company/peeringdb) and [X](https://x.com/PeeringDB).

## Release schedule

This schedule provides planned dates for PeeringDB’s future releases. We are sharing these dates to help PeeringDB users plan ahead for testing new and improved features in beta. We also want to help volunteer developers know the date on which their code changes are needed for internal testing before beta release.

We provide a rolling schedule. Dates can change, so if you have a question or request please contact us at: [support@peeringdb.com](mailto:support@peeringdb.com).

Our releases are generally deployed at around 04:00 UTC.

| **Release number** | **Internal testing** | **Beta release** | **Production release** |
| -------------- | ---------------- | ------------ | ------------------ |
| 2.78.0 | 2026-04-13 | 2026-04-22 | 2026-04-29 |
| 2.79.0 | 2026-05-05 | 2026-05-13 | 2026-05-20 |
| 2.80.0 | 2026-06-08 | 2026-06-17 | 2026-06-24 |

## Release 2.78.0

Beta Announcement Date: 22 March 2026
Release Date: 29 March 2026

| **GitHub issue** | **Summary** |
| ----------------- | ----------- |
| [#1810 Allow disabling either passwords or TOTP for users with passkeys.](https://github.com/peeringdb/peeringdb/issues/1810) | As title.|
| [#1825 Make "Copy API Query" Feature Available in Advanced Search.](https://github.com/peeringdb/peeringdb/issues/1825) | As title.|
| [#1911 2FA backup codes are not retrivable.](https://github.com/peeringdb/peeringdb/issues/1911) | Fixes bug as per title.|
| [#1918 Double // cause multiple issues with integrations and peeringdb-py.](https://github.com/peeringdb/peeringdb/issues/1918) | Fixes bug as per title.|
| [#1881 Allow 'docker compose' in addition to 'docker-compose'.](https://github.com/peeringdb/peeringdb/issues/1881) | Removes the 'version' in docker-compose.yml and ensures the services restart unless they are stopped, improving upgrades.|
| [peeringdb-py #91 Investigate odd missing relationships during initial syncs.](https://github.com/peeringdb/peeringdb-py/issues/91) | Fixes bug with syncs.|


## Release 2.77.0

Beta Announcement Date: 11 March 2026
Release Date: 18 March 2026

| **GitHub issue** | **Summary** |
| ----------------- | ----------- |
| [#1920 Search not showing current results.](https://github.com/peeringdb/peeringdb/issues/1920) | Fixes bug as per title.|
| [#1805 SLIs for PeeringDB load time.](https://github.com/peeringdb/peeringdb/issues/1805) | Add measures for user experience of www.peeringdb.com.|
| [#1437 Investigate performance tuning opportunities.](https://github.com/peeringdb/peeringdb/issues/1437) | As title.|
| [#1884 Adding manholes as facilities.](https://github.com/peeringdb/peeringdb/issues/1884) | Facilities can now indicate when they do not provide power.|
| [#1873 ASN Comparison - allow users to paste in a comma separated list of ASNs to check.](https://github.com/peeringdb/peeringdb/issues/1873) | As title.|
| [#1872 ASN Comparison - intermittent failure.](https://github.com/peeringdb/peeringdb/issues/1872) | Fixes bug as per title.|
| [#1912 Logging in with a 2FA backup code still require a U2F tap (making them useless).](https://github.com/peeringdb/peeringdb/issues/1912) | Fixes bug as per title.|
| [#1874 Populate Port Location using information from the IX-F import.](https://github.com/peeringdb/peeringdb/issues/1874) | As title.|
| [#1878 Errors and warnings with api-schema.](https://github.com/peeringdb/peeringdb/issues/1878) | Fix schema to avoid errors.|
| [peeringdb-py #128 django-countries dependency missing.](https://github.com/peeringdb/peeringdb-py/issues/128) | As title.|
| [peeringdb-py #129 auto_pdb_load_data.sh fails with MySQL Error Data too long for column 'logo'.](https://github.com/peeringdb/peeringdb-py/issues/129) | As title.|
| [#1918 Double // cause multiple issues with integrations and peeringdb-py.](https://github.com/peeringdb/peeringdb/issues/1918) | Fixes bug as per title.|
| [peeringdb-py #134 peeringdb.client.Client constructor type is too strict.](https://github.com/peeringdb/peeringdb-py/issues/134) | Fixes bug as per title.|
| [peeringdb-py #91 Investigate odd missing relationships during initial syncs.](https://github.com/peeringdb/peeringdb-py/issues/91) | Fixes bug as per title.|
| [#1891 Broken AS-SET checking.](https://github.com/peeringdb/peeringdb/issues/1891) | Fixes bug as per title.|
| [#1886 Drop down button incorrectly placed out of page.](https://github.com/peeringdb/peeringdb/issues/1886) | Fixes bug as per title.|
| [#1877 Auto undelete network.](https://github.com/peeringdb/peeringdb/issues/1877) | Automatically undelete networks when an ASN is reassigned and passes the normal checks. This was previously done manually.|
| [peeringdb-py #128 django-countries dependency missing.](https://github.com/peeringdb/peeringdb-py/issues/128) | As title.|
| [peeringdb-py #129 auto_pdb_load_data.sh fails with MySQL Error Data too long for column 'logo'.](https://github.com/peeringdb/peeringdb-py/issues/129) | As title.|

## Release 2.76.4

Release Date: 2 March 2026

| **GitHub issue** | **Summary** |
| ----------------- | ----------- |
| [#1916 remove empty return-path header.](https://github.com/peeringdb/peeringdb/pull/1916) | Removed the erroneous `Return-Path: <>` header from outbound emails.|


## Release 2.76.3

Release Date: 28 February 2026

| **GitHub issue** | **Summary** |
| ----------------- | ----------- |
| [#1910 OAuth broken with (at least) U2F 2FA keys.](https://github.com/peeringdb/peeringdb/pull/1910) | As title.|

## Release 2.76.2

Release Date: 26 February 2026

| **GitHub issue** | **Summary** |
| ----------------- | ----------- |
| [#1909 skip healthcheck for web page ratelimiting.](https://github.com/peeringdb/peeringdb/pull/1909) | As title.|

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
