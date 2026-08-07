# PeeringDB Deskpro Public Response Snippets

This document provides a human-friendly index of **Public Response Snippets** used by the **PeeringDB Admin Committee** in Deskpro (`peeringdb.deskpro.com`).

> [!NOTE]
> Public shortcuts can be triggered in Deskpro by typing `;code` (e.g. `;net-approved`). Internal/staff-only snippets, empty snippets, and short snippets (<=3 lines) are excluded.

## Table of Contents

- [1. Network Registration & Approvals](#1-network-registration-approvals)
- [2. Facility & Carrier Management](#2-facility-carrier-management)
- [3. Organization Recovery & Account Verification](#3-organization-recovery-account-verification)
- [4. IP Address & IX-F Conflict Resolution](#4-ip-address-ix-f-conflict-resolution)
- [5. General Administrative & Support Responses](#5-general-administrative-support-responses)

---

## 1. Network Registration & Approvals

### 01 Your request net has been approved

- **Snippet ID**: `#1`
- **Shortcut Code**: `;net-approved`
- **Access Level**: 🌐 Public

```text
Dear {{user.name}} ({{user.email}}),

Congratulations! Your request has been approved. You will need to log out and back in for it to take effect if this is the first object you registered. To benefit most from your entry, fill in all the fields. Especially

- All objects are editable. Hence, never delete one unless you are 100% sure  you don't need it anymore.

- Give your network a nice name. If you have more than one ASN, add the purpose or region of each ASN

- IRR as-set/route-set

- Network Type, offering a variety of types

- Number of IPv4 and IPv6 Prefixes (please note: number of prefixes, not the number of IP addresses or the prefix length mask)

- Traffic Levels and Ratio

- Connections to IXP (so-called Public Peering Exchange Points)

- Presences in Colocation Facilities (so-called Private Peering Facilities)

Don't also forget to add Contact Information. It would be best to have them when adding Public Peering Exchange Points. And don't forget that you registered to interconnect. And how to contact you if there is no Contact Information.

Enjoy using PeeringDB!

Best regards,

{{agent.alias}}
```

### 05 How to add your network to an IXP

- **Snippet ID**: `#3`
- **Shortcut Code**: *None*
- **Access Level**: 🌐 Public

```text
Dear {{user.name}} ({{user.email}}),

Adding your network to an IXP is straightforward. Let's say you want to add yourself as a member of IXP Best-IX

- Log in to PeeringDB with an Admin account

- Go to your network entry (either click on the menu right to your login, choose your organization, then network OR search for your network in the search field)

- Click on edit on the right-hand side

- Make sure you have at least one technical contact information (Technical, NOC or Policy) with visibility "Users" or "Public". If not, add one!

- Start to type in "Best-IX" in the Exchange Field. Best-IX should pop up in the drop-down menu. If Best-IX does not show up, contact owners of Best-IX to add their IX to PeeringDB

- Fill in all the other details

While editing your record, please also check whether the information is up to date.

Best regards,

{{agent.alias}}
```

### 06 How to add your network to a Facility

- **Snippet ID**: `#4`
- **Shortcut Code**: *None*
- **Access Level**: 🌐 Public

```text
Dear {{user.name}} ({{user.email}}),

Adding your network to a Facility is straightforward. Let's say you want to add yourself as a member of Facility Best-Fac.

- Log in to PeeringDB with an Admin account

- Go to your network entry (either click on the menu right to your login, choose your organization, then network OR search for your network in the search field)

- Click on edit on the right-hand side

- Start to type in "Best-Fac" in the Facility Field. Best-Fac should pop up in the drop-down menu. If Best-Fac does not show up, contact owners of Best-Fac to add their Facility to PeeringDB

While editing your record, please also check whether the information is up to date

Best regards,

{{agent.alias}}
```

### 07 Your application for being listed as IXP was not approved

- **Snippet ID**: `#5`
- **Shortcut Code**: `;ix-rejected`
- **Access Level**: 🌐 Public

```text
Dear {{user.name}} ({{user.email}}),

Thank you for submitting your application to be listed as an IXP in PeeringDB. However, based on the information provided, we have not yet concluded that your service meets our requirements to be listed as an Internet Exchange Point within PeeringDB.

A widely accepted definition of an IXP is: An Internet Exchange Point (IXP) is a network facility that enables the interconnection of more than two independent Autonomous Systems to facilitate Internet traffic exchange. An IXP provides interconnection only for Autonomous Systems. It does not require Internet traffic between any pair of participating Autonomous Systems to pass through a third Autonomous System, nor does it alter or otherwise interfere with such traffic

Please provide

- Website: mandatory and must list the IX as a service.

- Participant list: Mandatory and must include at least three independent participants, each with their ASN, IPv4, and IPv6 peering addresses.

- Exchange prefixes: The globally unique IPv4 and/or IPv6 prefixes used on the exchange must have a demonstratable connection to you or your organization, via publicly visible RDAP data.

- We expect your answer within 90 days. If we don't get an answer, your request is denied.

Please note: The three required participants must not include route servers, route collectors, route viewers, or any other Autonomous Systems that are operated by, or affiliated with, the applicant organization, its employees, or its PeeringDB users. 

Best regards,

{{agent.alias}}
```

### 03 Your application for being listed as a Facility was not approved

- **Snippet ID**: `#6`
- **Shortcut Code**: `;fac-rejected`
- **Access Level**: 🌐 Public

```text
Dear {{user.name}} ({{user.email}}),

Thank you for submitting your application for a Facility object in PeeringDB.

Based on the information currently available, we have not yet been able to determine that this location meets our requirements for a Facility object.

PeeringDB Facility Requirements

For PeeringDB purposes, a Facility object is intended to represent a unique colocation or data centre facility that is owned and operated by the submitting organisation. The facility must have an accurate physical address, a public website, and must openly offer colocation or meet-me-room services to the general public as unbundled services.

A Facility object is not intended to represent an office, a point of presence, a customer site, or a location where an organisation only hosts its own services or customer services. If your organisation is a tenant within a larger data centre, the Facility object should normally be submitted by the organisation that owns and operates that data centre facility. Similarly, ownership of a building alone is not sufficient if the submitting organisation does not operate the facility as a public colocation or interconnection site.

What We Need to See

To be listed as a Facility in PeeringDB, the website must clearly show that the facility offers colocation, data centre, or meet-me-room services to the public. The facility should also support network interconnection, including access to more than a single carrier option, so that networks located at the facility can interconnect with other networks.

At present, we could not identify sufficient public information confirming that this location meets those requirements.

Required Documentation

Please update your website or provide a specific public URL that clearly shows:

- the facility name and accurate physical address;

- that your organisation owns and operates the facility;

- that colocation, data centre, or meet-me-room services are openly available to the public as unbundled services; and

- that the facility provides network interconnection options, including more than a single carrier option.

Timeline

We expect your response within 90 days. If we do not receive a response within that period, your request may be denied.

The approval process is described in more detail here:https://docs.peeringdb.com/committee/admin/approval-guidelines/#approving-facility-fac-objects

{{agent.alias}}
```

### 14 How to add a network to your Organisation

- **Snippet ID**: `#9`
- **Shortcut Code**: *None*
- **Access Level**: 🌐 Public

```text
Dear {{user.name}} ({{user.email}}), 

Thank you for using PeeringDB. Adding another network to your organisation is quite easy. 

- Make sure you are logging in

- from the menu right to your username (upper right corner) chose the organisation you want the network to belong to

- Scroll down to the "Manage" section. Click on the 2nd tab "Add network"

- Key in all the pieces of information and press button "Submit Network"

Best regards,

{{agent.alias}}
```

### 08 You application for SUGGESTING a facility was not approved

- **Snippet ID**: `#10`
- **Shortcut Code**: *None*
- **Access Level**: 🌐 Public

```text
Dear {{user.name}} ({{user.email}}),

Thank you for applying to list a Facility in PeeringDB. However, when looking at the services being offered, we conclude that the suggestion is not a Facility.  A Facility does not mean that the company has an office at this address or running a data centre to host their own services or services for their customers. To be listed as a Facility in PeeringDB we would expect that they offer colocation, data centre and/or meet-me-room services to the public.

Please note that 

- Website: mandatory and MUST list colocation as a service. This is missing. Please provide the URL.

- Provide information within 90 days, please. If we don't get more information, the suggestion will be removed.

Best regards,

{{agent.alias}}
```

### 15 How to add your first network to peeringdb

- **Snippet ID**: `#11`
- **Shortcut Code**: *None*
- **Access Level**: 🌐 Public

```text
Dear {{user.name}} ({{user.email}}),

Thank you for wanting to use PeeringDB. Adding your network is quite easy.

- Make sure you are logging into PeeringDB (If you do not have an account, yet. You will need to create one)

- Make sure to confirm your email address (if you have not already done so via the link received in an email)

- From the menu right to your username (upper right corner) chose "profile"

- In the "Affiliate with organization" section. Key in Organization Name and AS Number. Press button "Affiliate"

- Await confirmation of affiliation from PeeringDB. (This step will be either fully automated or manually reviewed. Depending on fetched RIR data)

Best regards,

{{agent.alias}}
```

### 17 You application for adding non-allocated ASN was not approved

- **Snippet ID**: `#14`
- **Shortcut Code**: *None*
- **Access Level**: 🌐 Public

```text
Dear {{user.name}} ({{user.email}}),

You have had tried to create a network in PeeringDB with a non-allocated ASN.

Please note we only accept applications for networks with a valid allocated ASN. RDAP lookups always verify this to the relevant RIR entity.

Best Regards,

{{agent.alias}}
```

### 16 Your PeeringDB IRR as-set/rs-set entry

- **Snippet ID**: `#17`
- **Shortcut Code**: *None*
- **Access Level**: 🌐 Public

```text
Dear PeeringDB user

The value in your IRR as-set/rs-set entry does not exist. In the worst case, that means that your peers are not accepting any prefixes from you. If you are lucky, they still will accept all the prefixes originating from your ASN.

Generally, it's an excellent idea to have an as-set/rs-set. So, what to do

- If you have not yet chosen a name, think about a good name. ASnnnnn:AS-ALL, where nnnnnn is the ASN is a good choice as it is unique across all IRRs

- there are a bunch of IRRs to register your as-set/rs-set. See http://www.irr.net/

- where to register your ASN? The easiest is to register with your RIR as you already have an account there

- AfriNIC: https://www.afrinic.net/services/1871-create-as-set-on-afrinic-whois-database

- ARIN: https://www.arin.net/resources/manage/irr/templates/

- APNIC: https://www.apnic.net/manage-ip/using-whois/guide/as-set/

- LACNIC: https://lacnic.zendesk.com/hc/es/articles/360039152373-Crear-as-set

- RIPE NCC: https://www.ripe.net/manage-ips-and-asns/db/support/documentation/creating-basic-ripe-database-objects

See also this blog article about hierarchical as-sets https://www.manrs.org/2022/12/why-network-operators-should-use-hierarchical-as-sets/ for more information.

Best regards

{{agent.alias}}
```

### 04 Your request ix has been approved

- **Snippet ID**: `#19`
- **Shortcut Code**: `;ix-approved`
- **Access Level**: 🌐 Public

```text
Dear {{user.name}} ({{user.email}}),

Congratulations! Your request has been approved. You will need to log out and back in to take effect if this is the first object registered. To benefit most from your entry, encourage your ASN customers to register with PeeringDB and list their presence at your IXP.

Enjoy using PeeringDB!

Best regards,

{{agent.alias}}
```

### 04 Your request fac has been approved

- **Snippet ID**: `#25`
- **Shortcut Code**: `;fac-approved`
- **Access Level**: 🌐 Public

```text
Dear {{user.name}} ({{user.email}}),

Congratulations! Your request has been approved. You will need to log out and back in to take effect if this is the first object registered. To benefit most from your entry, encourage your ASN, Carrier, and IXP customers to register with PeeringDB and list their presence at your facility.

Enjoy using PeeringDB!

Best regards,

{{agent.alias}}
```

### 07 Your application for being listed as Carrier was not approved

- **Snippet ID**: `#26`
- **Shortcut Code**: `;car-rejected`
- **Access Level**: 🌐 Public

```text
Dear {{user.name}} ({{user.email}}),

Thank you for submitting your application for a Carrier object in PeeringDB.

Based on the information currently available on your website, we have not yet been able to determine that your organisation meets our requirements for a Carrier object.

For PeeringDB purposes, a Carrier object is intended for organisations that publicly offer carrier-grade network infrastructure services such as dark fibre, wavelengths/DWDM, Ethernet transport, MPLS VPN, or similar services delivered over fibre infrastructure they own and operate.

Internet access services alone are not sufficient for a Carrier object. Similarly, services that appear to be resold or leased from another provider, rather than delivered over infrastructure your organisation owns and operates, do not meet our requirements.

Your website is mandatory for this review and must clearly describe the relevant carrier services your organisation provides. At present, we could not identify this information.

Please update your website or provide a specific public URL that clearly shows the carrier services you offer, including the type of services provided and an indication that they are delivered over infrastructure your organisation owns and operates.

We expect your response within 90 days. If we do not receive a response within that period, your request may be denied.

Best regards,

{{agent.alias}}
```

### 04 Your request carrier has been approved

- **Snippet ID**: `#27`
- **Shortcut Code**: `;car-approved`
- **Access Level**: 🌐 Public

```text
Dear {{user.name}} ({{user.email}}),

Congratulations! Your request has been approved. You will need to log out and back in to take effect if this is the first object registered. To benefit most from your entry, please add all of your presences at a Facility. If a Facility is not yet in PeeringDB, suggest it first.

Enjoy using PeeringDB!

Best regards,

{{agent.alias}}
```

### 990 Org name RIPE-NCC-END-MNT for new networks GH#1455

- **Snippet ID**: `#30`
- **Shortcut Code**: `;gh1455`
- **Access Level**: 🌐 Public

```text
Dear {{user.name}} ({{user.email}}),

We have an ongoing problem concerning this ⟶ https://github.com/peeringdb/peeringdb/issues/1455, https://github.com/peeringdb/peeringdb/issues/1520 (unrelated networks end up under the same parent ORG)

I have moved the network to a new organization. ⟶ __INSERT_LINK_TO_NEW_ORGANIZATION__

Please follow the regular procedure to request affiliation (again).

Best regards,

{{agent.alias}}
```

## 2. Facility & Carrier Management

### 20 Deletion prevented: FAC

- **Snippet ID**: `#22`
- **Shortcut Code**: `;deletion-fac`
- **Access Level**: 🌐 Public

```text
Dear {{user.name}} ({{user.email}}),

You tried to delete a facility. However, as long as networks and IXP are connected to a facility, you can't delete it.

Would you please let us know why you want to delete the facility? There might be several reasons. 

- The facility was abandoned entirely.

- The facility has a new owner but still is in operation. If so, who is the new owner?

Please let us know why, and we will be happy to support you.

Best regards and enjoy PeeringDB

{{agent.alias}}
```

### 23 Deletion prevented: IXPFX

- **Snippet ID**: `#24`
- **Shortcut Code**: `;deletion-ixpfx`
- **Access Level**: 🌐 Public

```text
Dear {{user.name}} ({{user.email}}),

You tried to delete an IXP Prefix. However, as long as networks are connected to an IXP, you can't delete it. This also would delete all connections to the IXP

Would you please let us know why you want to delete the IXP Prefix? There might be several reasons. 

- you are turning down the IXP

- you are migrating to a new IXP Prefix

- you are enlarging the IXP Prefix mask

Please let us know why, and we will be happy to support you.

Best regards and enjoy PeeringDB

{{agent.alias}}
```

## 3. Organization Recovery & Account Verification

### 02 Mismatch between company name and email address

- **Snippet ID**: `#2`
- **Shortcut Code**: `;mismatch-email`
- **Access Level**: 🌐 Public

```text
Dear {{user.name}} ({{user.email}}),

We use RDAP and Whois information from the RIR to authenticate requests. To allow for minimum authentication information from RIR, your email address must match. We detected a mismatch and, therefore, are not accepting your application. Please alter your data and reply to this ticket.

These are the email addresses we could fetch from the ASNs belonging to this organization:

Please send a confirmation email from one of the addresses listed above. Alternatively, those on CC, please register and claim your organisation at https://www.peeringdb.com. You may also add the/an authoritative email as secondary email to the requesting account:

Best regards,

{{agent.alias}}
```

### 13 Using one user account to maintain multiple organisations

- **Snippet ID**: `#8`
- **Shortcut Code**: *None*
- **Access Level**: 🌐 Public

```text
Dear {{user.name}} ({{user.email}}),

With PeeeringDB 2.0 you can maintain as many organisations / asn with just one *user* account. This really eases uses of PeeringDB as you only log in once and then you can choose the organisation from the menu right to your username in the upper right corner.

However, if you also want to have separate user accounts, you still can do. As a user account is always bound to a certain mail address, make sure that you have proper authorisation to maintain all asn.

Enjoy using PeeringDB!

Best regards,

{{agent.alias}}
```

### 12 Contact your PeeringDB admins

- **Snippet ID**: `#28`
- **Shortcut Code**: `;contacts-existing-admins`
- **Access Level**: 🌐 Public

```text
Dear {{user.name}} ({{user.email}}),

to gain access to your PeeringDB account or to get affiliated, please contact your PeeringDB admin(s)

Best regards and enjoy using PeeringDB

{{agent.alias}}
```

## 4. IP Address & IX-F Conflict Resolution

### 09 Your application for adding an organisation

- **Snippet ID**: `#7`
- **Shortcut Code**: `;org-rejected`
- **Access Level**: 🌐 Public

```text
Dear {{user.name}} ({{user.email}}),

Thank you for sending in your request for ownership of an organization. However, PeeringDB does not store information about organizations for just this information. Organizations always are parents of other records, like networks, facilities or IXP.

If you want to change your organisation's name, please log in as an Admin and change the name via "Edit". Otherwise, please add more information about why you want us to add your organization.

Best regards,

{{agent.alias}}
```

### 18 Actions from IX-F JSON importer needed

- **Snippet ID**: `#18`
- **Shortcut Code**: *None*
- **Access Level**: 🌐 Public

```text
Dear {{user.name}} ({{user.email}}),

We have to contact you as your network record does not have a technical (Technical, NOC, Policy) contact. Please add one of these role accounts.

The IX-F JSON importer has detected a mismatch between your data and the data published by the exchange. 

Please log in to PeeringDB with an admin account and try to resolve the issues. Reach out to the IX, without involving PeeringDB support if in doubt.

Best regards

{{first_name}} {{last_name}}
```

## 5. General Administrative & Support Responses

### 12 Forgot credentials

- **Snippet ID**: `#12`
- **Shortcut Code**: `;lost-credentials`
- **Access Level**: 🌐 Public

```text
Dear {{user.name}} ({{user.email}}),

to recover your credentials please use

- password: https://peeringdb.com/reset-password

- username: https://peeringdb.com/username-retrieve

Best regards and enjoy using PeeringDB

{{agent.alias}}
```

### 10 Tickets mistakenly sent to PeeringDB Support

- **Snippet ID**: `#13`
- **Shortcut Code**: `;wrong-support-team`
- **Access Level**: 🌐 Public

```text
Dear {{user.name}} ({{user.email}}),

You have written an e-mail to "PeeringDB Support" (4) with the subject line "{{subject}}" for a purpose we do not cover.

Please contact the appropriate entity separately and drop PeeringDB from this conversation!

Please see (0,1,2) for more information about what PeeringDB is and our mission statement (3). We can also recommend using a search engine to look for additional information about PeeringDB yourself (6).

- https://en.wikipedia.org/wiki/PeeringDB

- https://www.de-cix.in/blog/what-to-use-peeringdb

- https://docs.peeringdb.com/faq/#what-is-peeringdb

- https://www.peeringdb.com/about

- https://www.peeringdb.com

- What is PeeringDB: DuckDuckGo, Google, Yahoo, Bing

Best Regards,

{{agent.alias}}
```

### 19 PeeringDB Volunteer (already full)

- **Snippet ID**: `#15`
- **Shortcut Code**: *None*
- **Access Level**: 🌐 Public

```text
Dear {{user.name}} ({{user.email}}),

Thank you for your interest in volunteering with PeeringDB, that means a lot to us!

Unfortunately, we are at full capacity in all our Committees right now, but we will be happy if you come back to us once a spot opens! Usually, we will announce that on every social channel of your choice.

Meanwhile, please join us on our public projects like the translation of PeeringDB to other languages, to enable everyone all around the world to use this great tool: https://docs.peeringdb.com/translation/

Best regards,

{{agent.alias}}
```

### 22 Deletion prevented: POC

- **Snippet ID**: `#21`
- **Shortcut Code**: `;deletion-poc`
- **Access Level**: 🌐 Public

```text
Dear {{user.name}} ({{user.email}}),

You tried to delete the last technical contact for your ASN. However, as long as you have connections to an IXP, we need a technical contact to assist in communication between you and the IXP.

If you want to delete the contact, please remove all IXP connections or add another technical contact first. A technical contact is either a NOC, Policy or Technical role account in your ASN's "Contact Information" section.

Best regards and enjoy PeeringDB

{{agent.alias}}
```

### 09 How to register with PeeringDB

- **Snippet ID**: `#23`
- **Shortcut Code**: *None*
- **Access Level**: 🌐 Public

```text
Dear {{user.name}} ({{user.email}}),

Thank you for contacting PeeringDB. From your email, we don't see which business you are in. Please let us know (URL!). You only need to register with PeeringDB if you maintain an object or are a member of a Carrier, a Facility, an IXP or a Network (aka ASN) and need more information, esp. contact information. Otherwise, you don't need an account, and we most likely will not accept your request.

- Register via https://peeringdb.com/register

- Once approved, affiliate yourself with an organisation via https://peeringdb.com/profile.

- You only need one account to affiliate with many organisations. There is no need to create additional accounts.

- If you only want to research, you will not need an account, but some point-of-contact data may be hidden.

Best regards,

{{agent.alias}}
```

### 991. Redirect feature request to GitHub

- **Snippet ID**: `#34`
- **Shortcut Code**: *None*
- **Access Level**: 🌐 Public

```text
Dear {{alias}} ({{email}}),

Could I convince you to raise that as a feature request at our GitHub issue tracker?

The support email is intended only for support related questions. And feature requests should ideally be raised at the GitHub issue tracker. ;-)

Best,

{{agent.alias}}
```
