# Release Notes

The release notes list the GitHub issues and a summary of what has changed in PeeringDB software releases.

Each new release has a one week beta test period on the [beta server](https://beta.peeringdb.com/) before it goes live.  The beta and new releases are announced on the [PeeringDB Announce Mailing List](https://lists.peeringdb.com/cgi-bin/mailman/listinfo/pdb-announce) and on [Twitter](https://twitter.com/PeeringDB), [LinkedIn](https://www.linkedin.com/company/peeringdb) and [Facebook](https://www.facebook.com/peeringdb).

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
