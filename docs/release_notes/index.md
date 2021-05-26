# Release Notes

The release notes list the GitHub issues and a summary of what has changed in PeeringDB software releases.

Each new release has a one week beta test period on the [beta server](https://beta.peeringdb.com/) before it goes live.  The beta and new releases are announced on the [PeeringDB Announce Mailing List](https://lists.peeringdb.com/cgi-bin/mailman/listinfo/pdb-announce) and on [Twitter](https://twitter.com/PeeringDB), [LinkedIn](https://www.linkedin.com/company/peeringdb) and [Facebook](https://www.facebook.com/peeringdb).

This page was started in April 2020, and only has information about PeeringDB releases starting from that date.

## Release 2.27.1

Beta Announcement Date: 19 May, 2021
Release Date: 26 May, 2021

| **GitHub Issue** | **Summary** |
| ----------------- | ----------- |
| [#946 Evaluate non-google map/geo sources ](https://github.com/peeringdb/peeringdb/issues/946) | Evaluated alternative geo data APIs and selected Melissa. |
| [#802 Extend Advanced Search for IXes and Facilities ](https://github.com/peeringdb/peeringdb/issues/802) | Adds search filters to advanced search (ix capacity search, organization presence search, and network presence search.) |
| [#799 Additional self-selection fields for IX objects ](https://github.com/peeringdb/peeringdb/issues/799) | Added `service_level` and `terms` fields to InternetExchange objects to allow exchanges to share additional ifnormation about their offering. These are supported as filters in the advanced search. |
| [#834 Add ix_count to object fac ](https://github.com/peeringdb/peeringdb/issues/834) | In the API, added a read-only field to `fac` called `ix_count` that counts the number of exchanges the linked to the facility). |
| [#835 Add {ix,fac}_count to object net ](https://github.com/peeringdb/peeringdb/issues/835) | In the API, added read-only fields to `net` called `ix_count` and `fac_count` that count the number of exchanges and facilities linked to the network). |
| [#836 Add fac_count to object ix ](https://github.com/peeringdb/peeringdb/issues/836) | In the API, added a read-only field to `ix` called `fac_count` that counts the number of facilities in which the exchange has a presence. |
| [#922 Circumvent approval of a facility by deleting and re-adding ](https://github.com/peeringdb/peeringdb/issues/922) | Fixed bug where if a user deletes a status "pending" fac, they can re-add it and it will be status "ok" (should be "pending"). |
| [#810 Get rid of the 'Protocols supported' fields / UI for IXes ](https://github.com/peeringdb/peeringdb/issues/810) | Removed `proto_unicast`, `proto_multicast`, and `proto_ipv6` fields from `ix` UI. The fields remain in the v2 api but `proto_ipv6` and `proto_unicast` will be populated from the existance of protocols in the exchange's `ixpfx` records. |
| [#985 500 Error on advanced search ](https://github.com/peeringdb/peeringdb/issues/885) | Resolved an issue where unauthenticated users got a 500 error in advanced search. |


## Release 2.26.1

Beta Announcement Date: 14 April, 2021
Release Date: 21 April, 2021

| **GitHub Issue** | **Summary** |
| ----------------- | ----------- |
| [#883 IXF-Importer: minimise emails to Support/DeskPRO/AC ](https://github.com/peeringdb/peeringdb/issues/883) | This change collates all importer suggestions into a single e-mail notification. |
| [#931 Limit the number of requests for affiliation to an ASN/org to 1 ](https://github.com/peeringdb/peeringdb/issues/931) | Limits the number of affiliation request to an ASN to just one. Provides visual feedback on subsequent request attempts. |
| [#913 API should do an IP6 address instead of a string match ](https://github.com/peeringdb/peeringdb/issues/913) | Normalizes how IPv6 addresses are stored in the database and updates existing IPv6 addresses in the databases and elsewhere. |


## Release 2.26.0

Beta Announcement Date: 10 March, 2021
Release Date: 24 March, 2021

| **GitHub Issue** | **Summary** |
| ----------------- | ----------- |
| [#266 Add API Keys ](https://github.com/peeringdb/peeringdb/issues/266) | This release introduces organization level [API Keys](https://github.com/peeringdb/peeringdb/blob/master/docs/api_keys.md). |
| [#827 Make GUI and API feature equivalent ](https://github.com/peeringdb/peeringdb/issues/827) | PeeringDB has a GUI and an API. This issue is a reminder to keep both feature equivalent. |
| [#865 Allow arbitrary decimal places as input for longitude and latitude. Systems rounds to six ](https://github.com/peeringdb/peeringdb/issues/865) | Allow arbitrary length of inputs to latitude and longitude. Round to 6 digits (including Google Maps output). |
| [#902 Add "long name" or "aka" field to 'fac' records ](https://github.com/peeringdb/peeringdb/issues/266) | add fields `aka` and `name_long` to object `fac`, `ix`, `net`, and `org`. |
| [#937 Geocode for org is broken ](https://github.com/peeringdb/peeringdb/issues/937) | This was fixed through work on #940. |
| [#939 Replace Validation Error with Validation "Warning" for geolocation validation ](https://github.com/peeringdb/peeringdb/issues/939) | If our address validation service cannot find an address corresponding to the user-inputed address it will allow the object to be saved and raise a "validation warning" in the meta object of the API response. The web UI will display a pop-up based on this warning. |
| [#940 Return geo-normalized fields as "suggested address" ](https://github.com/peeringdb/peeringdb/issues/940) | In an effort to normalize addresses, the system may overwrite the user input. In case of a mismatch, the user now is prompted with a "suggested address" and either confirms or rejects. In case of rejection, the address is taken as provided by the user. Please keep an eye on what you provided and what is suggested. The suggestion may flip street name and house name as well as cut off postal codes. |
| [#918 drop travis ci and move to github actions ](https://github.com/peeringdb/peeringdb/issues/918) | Changed CI environment to improve deployment speed. |

## Release 2.25.0

Release Date: 3 February, 2021

| **GitHub Issue** | **Summary** |
| ----------------- | ----------- |
| [#246 IXF should be IX-F ](https://github.com/peeringdb/peeringdb/issues/246) | This release introduces various spelling corrections. |
| [#828 IX-F importer: Handle ipv4/ipv6 on same vlan but separate connections ](https://github.com/peeringdb/peeringdb/issues/828) | This issue deals with how the IX-F importer handles information from the IX-F JSON import. PeeringDB handles both the IPv4 as well as the IPv6 address in the same object (`netixlan`). And from a peering partner pov this is ok as it doesn't matter whether these addresses are on the same interface or even same router. However, IX-F JSON differentiates. For the time being, the importer combines IPv4 and IPv6 if both are set to an operational status in the IX-F JSON. |
| [#846 IX-F importer: if ixf_ixp_member_list_url is null then ixf_ixp_import_enabled can't be true ](https://github.com/peeringdb/peeringdb/issues/846) | Apply logic to the meaning of `ixf_ixp_member_list_url`. i.e. only allow `ixf_ixp_import_enabled` to be set to `true` if a URL is specified. |
| [#875 "IXF-Importer: improved handling of how contacts are joined into direct conflict resolution deskpro tickets"](https://github.com/peeringdb/peeringdb/issues/875) | Resolved an issue where responses to automatically generated Deskpro tickets were routed to the wrong ticket. |
| [#878 IXF-Importer: reorder of email content ](https://github.com/peeringdb/peeringdb/issues/878) | This is mainly an internal improvement. And fixes also not disclosing private IXP information to the public. |
| [#882 IXF-Importer: don't abort when there is nothing to import ](https://github.com/peeringdb/peeringdb/issues/882) | If there is nothing to import from an IX-F JSON don't abort with an error message. |
| [#893 IX-F Importer: history of changes per ixlan & netixlan ](https://github.com/peeringdb/peeringdb/issues/893) | Fixed bug related to the logging of importer changes. |
| [#896 IX-F Importer: Bogus output of "Preview" tool ](https://github.com/peeringdb/peeringdb/issues/896) | Fixed a bug in the preview tool, where `invalid member type ignored` messages weren't filtered for the network viewing the preview. |
| [#888 Type issue when overriding settings through environment variables for numeric types ](https://github.com/peeringdb/peeringdb/issues/888) | Fixed a bug and now ensure that overrides are coerced to the correct expected type. |
| [#872 Update dependencies ](https://github.com/peeringdb/peeringdb/issues/872) | Updated container to python 3.9 and addressed all dependencies.|
| [#694 add syntactic sugar for entering port speeds ](https://github.com/peeringdb/peeringdb/issues/694) | Simplifies the UI for editing port speeds to make it more human friendly. |
| [#717 Loading time issue /cp facility view ](https://github.com/peeringdb/peeringdb/issues/717) | Fixed slow load or timeouts for loading data for some facilities |
| [#837 Provide a friendlier explanation when entering / changing a phone number ](https://github.com/peeringdb/peeringdb/issues/837) | Provides a tooltip to help people enter E.164 formatted telephone numbers. |
| [#541 When looking at a network record, show last updated ix<->net or fac<->net date ](https://github.com/peeringdb/peeringdb/issues/541) | Improved information about when records were last updated. |


## Release 2.24.0

Beta Announcement Date: 4 November, 2020
Release Date: 11 November, 2020

| **GitHub Issue** | **Summary** |
| ----------------- | ----------- |
| [#381 Network type: Add "Government"](https://github.com/peeringdb/peeringdb/issues/381) | “Government” added as a network type. |
| [#463 Add new network type for networks that provide network services](https://github.com/peeringdb/peeringdb/issues/463) | “Network Services" for networks whose function is to provide specialized services, like DNS, RDAP, Whois or DDoS protection added as a network type. |
| [#745 Add “Route Collector” network type](https://github.com/peeringdb/peeringdb/issues/745) | “Route Collector” added as a network type.|
| [#747 Clean up info_type if name contains "Route Servers" or "Route Collector"](https://github.com/peeringdb/peeringdb/issues/747) | Data cleanup related to #745. All networks with route collectors have now been properly classified.|
| [#665 Drop ixlan name from displaying at "Peers at this Exchange Point"](https://github.com/peeringdb/peeringdb/issues/665) | Simplified the user interface by removing the name of the ixlan as there is now just one ixlan per exchange point. |
| [#775 Misleading tooltip of prefix limit fields](https://github.com/peeringdb/peeringdb/issues/775) | NO Improved the user interface with better language in the tooltip. The distinction between maximum prefix length and maximum number of prefixes should now be clearer. |
| [#814 Suppress RDAP call for contact data/handles for NIC\.br // AUTOTOOL](https://github.com/peeringdb/peeringdb/issues/814) | Internal tool change. This change suppresses calls for contact data over RDAP because NIC.br is no longer allowed to provide direct calls for personal data. |
| [#803 Searching for a user in /cp/peeringdb\_server/userorgaffiliationrequest results in 500](https://github.com/peeringdb/peeringdb/issues/803) | Internal tool change. Fixed an error that could return a 500 error on some searches. |
| [#688 Automate creation of Release Notes](https://github.com/peeringdb/peeringdb/issues/688) | Internal tool change. A new script that extracts data from Github milestones to build the markdown for the release notes page. |
| [#851 sponsorship\_notify RuntimeWarning \(was: End of Sponsorship notification email is no longer working\)](https://github.com/peeringdb/peeringdb/issues/851) | Internal tool change to improve the tracking of sponsorship renewals. |
| [#861 add explicit order for fields in admin control panel](https://github.com/peeringdb/peeringdb/issues/861) | Internal tool change. Display fields in an explicit order. |
| [#850  IX\-F Importer: Repeated emails are being generated for things already emailed](https://github.com/peeringdb/peeringdb/issues/850) | Internal procedure optimisation. A series of improvements to the IX-F importer tool. These changes are all related to improving notifications about data quality that were developed by the Data Ownership Task Force. |
| [#856 IX\-F Importer: Make hyperlinks clickable when creating DeskPRO tickets](https://github.com/peeringdb/peeringdb/issues/856) | See #850. |
| [#857 IX\-F Importer: intermittent issue with speed validation](https://github.com/peeringdb/peeringdb/issues/857) | See #850. |
| [#858 IX\-F Importer: Make pdb\_deskpro\_publish command ignore importer tickets](https://github.com/peeringdb/peeringdb/issues/858) | See #850. |
| [#859 IX\-F Importer: ERROR: 'IXFMemberData' object has no attribute 'ixf\_log\_entry'](https://github.com/peeringdb/peeringdb/issues/859) | See #850. |
| [#860 IX\-F Importer Blocker: "Days until DeskPRO ticket is created" should now be ignored/removed, such that no ticket or emails happen after a delay](https://github.com/peeringdb/peeringdb/issues/860) | See #850. |



## Release 2.23.0
Beta Announcement Date: 30 September, 2020
Release Date: 7 October, 2020

| **GitHub Issue** | **Summary** |
| ----------------- | ----------- |
| [#833 - IX-F Importer: Add failed email resending](https://github.com/peeringdb/peeringdb/issues/833)| Implement re-send mechanic for emails that could not be sent (indicated by a sent value of null). When re-sending an email add a note to the email stating "This email could not be delivered initially and may contain stale information". Add a field to the admin-com import emails table to show this note as well. Update sent if send is successful|
| [#832 - IX-F Importer: suggested update when it should be add + remove](https://github.com/peeringdb/peeringdb/issues/832)| In some edge cases a deletion will end up as a requirement incorrectly to a legitimate new entry still. See #770 #816 |
| [#831 - [prod] IX-F importer: NameError: name 'EmailMultiAlternatives' is not defined ](https://github.com/peeringdb/peeringdb/issues/831)| Fixes broken email function of `ix-f` importer |
| [#826 - Make technical poc mandatory when adding a netixlan](https://github.com/peeringdb/peeringdb/issues/826)| Upon creating a netixlan object check that net has at least one (`Technical`, `NOC`, `Policy`) `poc` and that the `poc` has an e-mail address. If not ask them to create one first. Visibility of at least one (`Technical`, `NOC`, `Policy`) `poc` has to be "Users" resp. "Public" |
| [#825 - [beta] IX-F importer: Make Importer return non-zero when there is an error that Ops should see](https://github.com/peeringdb/peeringdb/issues/825)| Improvements to `ix-f` importer that allow for easier notification and tracking of errors for the Ops team|
| [#824 - IX-F Preview - shows the consolidated delete operation when it shouldn't ](https://github.com/peeringdb/peeringdb/issues/824)| Simplified the UI for consolidated modifications to improve user understanding |
| [#759 - Describe the 'never-via-routeservers' flag](https://github.com/peeringdb/peeringdb/issues/759)| Add tooltip for never-via-routeservers option: "Indicates if this network will announce its routes via route servers or not"|
| [#571 - Facility registration tool adds identifier ](https://github.com/peeringdb/peeringdb/issues/571)| Fixes small UI bug in facility registration tool used by the Admin Committee |
| [#481 - Add min_speed and max_speed to ixlan](https://github.com/peeringdb/peeringdb/issues/481)| Based on the discussion in #475 adds a new global setting that limits `netixlan` speed values now. It's not a property on the ixlan anymore.|
| [#371 - Clean up users in verification queue](https://github.com/peeringdb/peeringdb/issues/371)| A tool to delete user entries older than 90 days from the so-called verification queue and run it on a regular schedule|
| [#370 - Make Website mandatory for suggesting a facility](https://github.com/peeringdb/peeringdb/issues/370)| Website is now mandatory when suggesting a facility but zipcode only mandatory for countries that have zipcodes |
| [#321 - Typos in locale](https://github.com/peeringdb/peeringdb/issues/321)| Fixes a number of typographical errors|

## Release 2.22.0
Beta Announcement Date: 15 July, 2020
Release Date: 26 August, 2020

| **GitHub Issue** | **Summary** |
| ----------------- | ----------- |
| [#249 - Add the IX-F Member Export URL to the ixlan API endpoint](https://github.com/peeringdb/peeringdb/issues/249) | There are two new fields in the ixlan section resp. the ixlan object, called ixf_ixp_member_list_url and ixf_ixp_member_list_url_visible. The first one contains the URL to the IX-F import file while the second governs the visibility of the URL. Values are the same as for the poc object, namely "Public", "Users" and "Private", defaulting to "Private" (i.e. or users who are members of the org). |
| [#268 - Database: unique constraints](https://github.com/peeringdb/peeringdb/issues/268) | This issue fixes internal DB behaviour. |
| [#358 - Lock ASN once the record is created](https://github.com/peeringdb/peeringdb/issues/358) | Once a network has been created, the field asn is made read-only. As the ASN is unique there is no reason to change it. Making the field read-only is to prevent unwanted side effects. |
| [#431 - Null 'rencode' from facility](https://github.com/peeringdb/peeringdb/issues/431) | Null out all values for legacy unused rencode field, and make it read only to prepare for removal in PDB v3 [#625] (https://github.com/peeringdb/peeringdb/issues/625). |
| [#600 - Visibility for "Allow IXP update" switch](https://github.com/peeringdb/peeringdb/issues/600) | A new field is added to the API net object, called allow_ixp_update. Furthermore, a line is added in global stats in the footer with a count (called "Automated Networks") of the networks which have "Allow IXP Update" enabled. |
| [#649 - Possible for 'ok' ixpfx to exist in 'pending' ixlan](https://github.com/peeringdb/peeringdb/issues/649) | This issue fixes an internal bug. |
| [#683 - Add net_count_ixf field to ix object](https://github.com/peeringdb/peeringdb/issues/683) | A field is added to the API object ix, called net_count_ixf, which indicates the number of net objects the exchange has in their IX-F JSON if they provide one. Otherwise, the value is null. |
| [#696 - Lock some objects from being deleted by the owner](https://github.com/peeringdb/peeringdb/issues/696) | To protect operational data objects fac, ix, ixlan and org are prevented from being deleted as long as there are other objects related to it. First, these objects must be deleted before the object itself can be deleted. The attempt to delete such a protected object gives an error message and also opens a ticket with the PeeringDB support. |
| [#697 - Creating, changing, and deleting a netixlan object](https://github.com/peeringdb/peeringdb/issues/697) | We completely re-implemented the way a connection to an exchange is handled. This new procedure allows both for a safe heads up a network can give to their peers as well as a safe way for exchanges to get rid of stale entries. Moreover, it allows networks to easily acknowledge new entries at exchanges which use the IX-F importer feature. See also the webinar for detailed information on this new procedure. |


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
Release Date: 23 April, 2020

| **GitHub Issue** | **Summary** |
| ----------------- | ----------- |
| [#707 - Make source not required for IRR records](https://github.com/peeringdb/peeringdb/issues/707) | Making source not required for IRR records. This requirement was an oversight during implementation of [#151 - Validation of IRR Records] (https://github.com/peeringdb/peeringdb/issues/151) that was released with 2.20.0 - see below. Product Committee revisited the issue after 2.20.0 and reports of concern from community and decided to retract the requirement in an emergency release|

## Release 2.20.1
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
| [#462 - Route-server URL starting with ssh://](https://github.com/peeringdb/peeringdb/issues/462) | Add SSH as supported protocol. |
| [#539 - Add attribute 'operational' to 'netixlan'](https://github.com/peeringdb/peeringdb/issues/539) | This is a new feature and allows networks to give early notice to their peers that they soon will show up at an IXP. There is a new check box when adding an IXP connection. By default, a connection is considered operational and the box is ticked. When the connection is still in provisioning status, please untick the box. When viewing, the warning glyphicon is shown right to the network name. The correspondent API object netixlan is enhanced by a boolean field operational defaulting to true. This feature is in line with the [Data Ownership Policy](../gov/misc/2020-04-06_PeeringDB_Data_Ownership_Policy_Document_v1.0.pdf). |
| [#548 - containerize server](https://github.com/peeringdb/peeringdb/issues/548) | Internal software deployment system has been changed to use containers which reduces time spent by the ops team for deployments, allows for better scaling, and reduces the cost of entry for new developers to write and test their code. |
| [#555 - Notes field translate button disappears](https://github.com/peeringdb/peeringdb/issues/555) | This is a bug fix. The "Translate" button is there for a moment and then disappeared. |
| [#557 - Show all languages on beta, even if translation is not ready for prod](https://github.com/peeringdb/peeringdb/issues/557) | As soon as a new translation is starting it is available on the beta to help the translators and to encourage the community for input. |
| [#598 - bug caused by the org affiliationship request without an asn](https://github.com/peeringdb/peeringdb/issues/598) | This is a bug fix and is only relevant for the PeeringDB Admin Committee. |
| [#609 - When creating an ix via the API also return ixlan_id and ixpfx_id](https://github.com/peeringdb/peeringdb/issues/609) | When creating an IX record via API, the call will also return the implicitly created ixlan_id and ixpfx_id. This makes it simpler and reduces the number of calls that need to be made to the API. |
| [#615 - Insert links into ID fields in DESKPRO AUTOASN tickets](https://github.com/peeringdb/peeringdb/issues/615) | This only affects tickets generated for PeeringDB Admin Committee. A link to the object in the UI is added. |
| [#626 - Update API docs](https://github.com/peeringdb/peeringdb/issues/626) | Internal mechanisms for generating the API docs have been updated to current standards. This also allows for easier user contributions to the docs themselves. |
| [#634 - Remove support for python2](https://github.com/peeringdb/peeringdb/issues/634) | Python 2.7 and 3.4 support is being removed from PeeringDB packages. |
| [#636 - Don't create a new net object, when there only is an ASN block](https://github.com/peeringdb/peeringdb/issues/636) | This is a bug fix and is only relevant for the PeeringDB Admin Committee. |
| [#667 - Fix use autocomplete fields in the admincom controlpanel to speed up loading times](https://github.com/peeringdb/peeringdb/issues/667) | This is a bug fix and is only relevant for the PeeringDB Admin Committee. |
