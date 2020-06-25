# Release Notes

The release notes list the GitHub issues and a summary of what has changed in PeeringDB software releases.

Each new release has a one week beta test period on the [beta server](https://beta.peeringdb.com/) before it goes live.  The beta and new releases are announced on the [PeeringDB Announce Mailing List](https://lists.peeringdb.com/cgi-bin/mailman/listinfo/pdb-announce) and on [Twitter](https://twitter.com/PeeringDB), [LinkedIn](https://www.linkedin.com/company/peeringdb) and [Facebook](https://www.facebook.com/peeringdb).

This page was started in April 2020, and will only have information about PeeringDB releases starting from that date.


## Release 2.21.0
Beta Announcement Date: 24 June, 2020
Release Date: 1 July, 2020

| **GitHub Issue** | **Summary** |
| ----------------- | ----------- |
| [#72 - Enable sort and reverse sort of IP column in IX display](https://github.com/peeringdb/peeringdb/issues/72) | Sort and reverse sort of IP column in IX display are added. Sort of the IP addresses in the expected natural order. The IPv4 address is the primary sort key. The IPv6 address is the secondary key. |
| [#121 - missing delete button for organisations](https://github.com/peeringdb/peeringdb/issues/121) | New feature. An admin user is able to delete an org if it has no live objects under it. |
| [#290 - Offer 2FA](https://github.com/peeringdb/peeringdb/issues/290) | 2FA is offered now. The implementation includes <ul><li> optional 2FA using [TOTP](https://tools.ietf.org/html/rfc6238) is offered</li><li> there is a knob in the user profile to enable and set it up</li><li> email recovery is added using the verified user email address</li><li> an icon is added in the org admin section to denote to org admins if users have 2FA enabled </li></ul> |
| [#352 - Mark IXP peering LAN as bogon](https://github.com/peeringdb/peeringdb/issues/352) | Allow IXP to tag their LAN prefixes as bogons. In general, LAN prefixes should not be visible in the DFZ. If it should be visible, IXPs are able to debogonise them |
| [#356 - Sorting by clicking table headers should use local-compare](https://github.com/peeringdb/peeringdb/issues/356) | Bugfix. Sorting now honours locale-sorting |
| [#519 - Make spelling of traffic levels consistent](https://github.com/peeringdb/peeringdb/issues/519) | This is a bug fix and a minor improvement. Spelling is made consistent and traffic levels up to 100+Tbps are added.|
| [#526 - Show "Last Updated" fields on fac, ix, org records](https://github.com/peeringdb/peeringdb/issues/526) | A "Last Updated" field is visible now for fac, ix, and org objects |
| [#537 - Posting https://www.peeringdb.com onto social media doesn't select a good preview image](https://github.com/peeringdb/peeringdb/issues/537) | Add opengraph image for page preview.|
| [#566 - Should deleted personal data be accessable through the API?](https://github.com/peeringdb/peeringdb/issues/566) | If a poc object is deleted it is made immediately non-gettable via the API, too. In case the corresponding net object was deleted unintentionally the object is still kept in the DB. After 30 days it will be hard-deleted. |
| [#569 - Don't return any POC data with status=deleted](https://github.com/peeringdb/peeringdb/issues/569) | POC objects do have a visibility scope. If a POC record is deleted it should not be able to retrieve it at all, even if visibility had been set to "public" before. The data will still be kept internally for 30 days for rollback if the deletion happened unintentionally. After 30 days the record will be hard-deleted.|
| [#580 - Add a clear error message, when user tries to re-add a previously deleted facility](https://github.com/peeringdb/peeringdb/issues/580) | Bug fix for an unclear behaviour. If a connection from a network to a facility was deleted the user was unable to re-add this connection by themselves and an unclear error message was given. Now, the user is able to re-add the connection. |
| [#618 - Support alternative direction of writing, e.g. Arabic](https://github.com/peeringdb/peeringdb/issues/618) | For right-to-left written languages, the entire layout of the PeeringDB website has to be flipped around. |
| [#644 - Undeleting an ixlan with an emtpy IPv4 XOR IPv6 field throws a silly error](https://github.com/peeringdb/peeringdb/issues/644) |Bugfix for the Admin Committee UI. An empty field was considered to be a legit non-null value and the system hence enforced uniqueness |
| [#650 - Add pointer from API docs to tutorial](https://github.com/peeringdb/peeringdb/issues/650) | A URL is added from the API documentation website to the PeeringDB tutorials |
| [#654 - Add pointer from API docs to tutorial](https://github.com/peeringdb/peeringdb/issues/654) | Bugfix for the Admin Committee UI. |
| [#663 - change default encoding of API calls to 'utf-8'](https://github.com/peeringdb/peeringdb/issues/663) | The output of API calls will change from content-type: application/json; charset=iso-8859-1 to content-type: application/json; charset=utf-8 |
| [#664 - Selection should only present undeleted objects](https://github.com/peeringdb/peeringdb/issues/664) | Admin Committee only related. Only non-deleted should be presented for selection |
| [#666 - Selection should only present undeleted objects](https://github.com/peeringdb/peeringdb/issues/666) | When changing owner of an ix admin GUI borks because of "Ixlan for exchange already exists" |
| [#669 - Add help text to "Add {Facility, Network, Exchange} tab](https://github.com/peeringdb/peeringdb/issues/669) | Added a better help text to make crystal clear that adding a Facility, Network, or Exchange means that you are owning this object. |
| [#679 - Add read-only Superuser](https://github.com/peeringdb/peeringdb/issues/679) | Provide PC members with a read-only access to the Admin UI. |
| [#712 - User is unable to update their net record ](https://github.com/peeringdb/peeringdb/issues/712) | Bug fix. Missing pointer to where the non-compliant value is |


## Release 2.20.2
Beta Announcement Date: N/A
Release Date: 23 April, 2020

| **GitHub Issue** | **Summary** |
| ----------------- | ----------- |
| [#707 - Make source not required for IRR records](https://github.com/peeringdb/peeringdb/issues/707) | Making source not required for IRR records. This requirement was an oversight during implementation of [#151 - Validation of IRR Records] (https://github.com/peeringdb/peeringdb/issues/151) that was released with 2.20.0 - see below. Product Committee revisited the issue after 2.20.0 and reports of concern from community and decided to retract the requirement in an emergency release|

## Release 2.20.1
Beta Announcement Date: N/A
Release Date: 21 April, 2020

| **GitHub Issue** | **Summary** |
| ----------------- | ----------- |
| [#702 - Requests from peeringdb-py error 500](https://github.com/peeringdb/peeringdb/issues/702) | Emergency release for a config change |

## Release 2.20.0
Beta Announcement Date: 15 April, 2020
Release Date: 21 April, 2020

| **GitHub Issue** | **Summary** |
| ----------------- | ----------- |
| [#151 - Validation of IRR Records](https://github.com/peeringdb/peeringdb/issues/151) | To make the IRR as-set/route-set field of more operational value, strict rules apply <ul><li> the as-set/rs-set name has to conform to RFC 2622 (5.1 and 5.2)</li><li> the source may be specified by AS-SET@SOURCE or SOURCE::AS-SET (preferred)</li> <li> valid sources are taken from the list of known IRRs</li><li> multiple values must be separated by either ,, , or , (i.e. comma, space or comma followed by space)</li></ul> |
| [#189 - Improve explanatory and help text](https://github.com/peeringdb/peeringdb/issues/189) | A clear help text is added for requesting affiliation to an organisation.  |
| [#251 - Limit number of concurrent affiliation requests per user](https://github.com/peeringdb/peeringdb/issues/251) | In order to reduce organization affiliation request spamming, the number of pending organization requests has been limited to 5. |
| [#295 Desk pro tickets -> DeskPRO tickets](https://github.com/peeringdb/peeringdb/issues/295)  | This is a bug fix and only affects the Admin UI. |
| [#378 - Add contact information for Facilities (fac) the same way as for ix and net](https://github.com/peeringdb/peeringdb/issues/378) | Contact information is added to Facilities and IXP. |
| [#452 - Org/Network name of a sponsor should not link to /sponsors, only the sponsor badge should](https://github.com/peeringdb/peeringdb/issues/452) | This is a bug fix. From now on only when clicking on the sponsor badge will direct to the sponsor page. |
| [#462 - Route-server URL starting with ssh://](https://github.com/peeringdb/peeringdb/issues/462) |  |
| [#539 - Add attribute 'operational' to 'netixlan'](https://github.com/peeringdb/peeringdb/issues/539) | This is a new feature and allows networks to give early notice to their peers that they soon will show up at an IXP. There is a new check box when adding an IXP connection. By default, a connection is considered operational and the box is ticked. When the connection is still in provisioning status, please untick the box. When viewing, the warning glyphicon is shown right to the network name. The correspondent API object netixlan is enhanced by a boolean field operational defaulting to true. This feature is in line with the [Data Ownership Policy](../gov/misc/2020-04-06_PeeringDB_Data_Ownership_Policy_Document_v1.0.pdf). |
| [#548 - containerize server](https://github.com/peeringdb/peeringdb/issues/548) | Internal software deployment system has been changed to use containers which reduces time spent by the ops team for deployments, allows for better scaling, and reduces the cost of entry for new developers to write and test their code. |
| [#555 - Notes field translate button disappears](https://github.com/peeringdb/peeringdb/issues/555) | This is a bug fix. The "Translate" button is there for a moment and then disappeared. |
| [#557 - Show all languages on beta, even if translation is not ready for prod](https://github.com/peeringdb/peeringdb/issues/557) | As soon as a new translation is starting it is available on the beta to help the translators and to encourage the community for input. |
| [#598 - bug caused by the org affiliationship request without an asn](https://github.com/peeringdb/peeringdb/issues/598) | This is a bug fix and is only relevant for the PeeringDB Admin Committee. |
| [#609 - When creating an ix via the API also return ixlan_id and ixpfx_id](https://github.com/peeringdb/peeringdb/issues/609) | When creating an IX record via API, the call will also return the implicitly created ixlan_id and ixpfx_id. This makes it simpler and reduces the number of calls that need to be made to the API. |
| [#615 - Insert links into ID fields in DESKPRO AUTOASN tickets](https://github.com/peeringdb/peeringdb/issues/615) | This only affects tickets generated for PeeringDB Admin Committee. A link to the object in the UI is added. |
| [#626 - Update API docs](https://github.com/peeringdb/peeringdb/issues/626) | Internal mechanisms for generating the API docs have been updated to current standards. This also allows for easier user contributions to the docs themselves. |
| [#634 - Remove support for python2](https://github.com/peeringdb/peeringdb/issues/634) | Python 2.7 and 3.4 support is being removed from PeeringDB packages. |
| [#636 - Don’t create a new net object, when there only is an ASN block](https://github.com/peeringdb/peeringdb/issues/636) | This is a bug fix and is only relevant for the PeeringDB Admin Committee. |
| [#667 - Fix use autocomplete fields in the admincom controlpanel to speed up loading times](https://github.com/peeringdb/peeringdb/issues/667) | This is a bug fix and is only relevant for the PeeringDB Admin Committee. |

**Notes:** 
[#519 Make spelling of traffic levels consistent](https://github.com/peeringdb/peeringdb/issues/519) is also planned to be added to beta.peeringdb.com in April 2020 however it will NOT be released in the immediate next release (2.20.0). This is in order to allow more time for API users for awareness and testing. It will be added to a future May/June release.







