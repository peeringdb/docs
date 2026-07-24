# FP — Consolidated Tools

Runs on the public PeeringDB frontend: `https://www.peeringdb.com/*` (and `beta.peeringdb.com`),
excluding `/cp/*`. This is the script that's active while you're browsing org/network/facility/
IX/carrier/campus pages and user-manager panels as a regular visitor would, but with AdminCom
shortcuts layered on top.

See [Installing](index.md#installing) on the overview page if you haven't added this script yet.

## Background fixes (no button, nothing to see)

Two small things happen automatically, silently, on every page load:

- A malformed URL with a double slash (`//`) is corrected via a redirect.
- An ASN page that renders as a public "404 Not Found" (because the network isn't visible on the
  frontend, e.g. still pending) redirects you straight to the equivalent CP search by ASN,
  saving a manual re-search.

## Page identity & navigation

**Window/tab titles** are rewritten to something identifiable on entity pages — e.g.
`PDB | NET | as65000 (Example Corp) (a.k.a. Foo) | net.peeringdb.com` — useful when you have many
tabs open during a review session. Cosmetic only, no screenshot needed.

**CP link in the navbar** — a one-click jump straight to the CP root (`/cp/`) is added to the top
navigation bar itself, in both the desktop-expanded and mobile-collapsed variants.

!!! tip "📸 Screenshot needed"
    The top navbar showing the added "CP" link, in both desktop-expanded and mobile-collapsed
    form.

## Entity page toolbar

**CP (`<type>:<id>`)** — a top-right toolbar button on any entity page (network/ASN/org/
facility/carrier/IX) that opens the record's CP change page directly in a new tab. Links that
open a CP page in a new tab are automatically marked with a small 🛠↗ suffix so it's clear where
they lead before you click.

!!! tip "📸 Screenshot needed"
    An entity page's top-right toolbar showing the "CP (net:1234) 🛠↗" button.

On network/ASN pages specifically, two more one-click copy buttons appear — **Copy AS`<N>`**
and **Copy Net Summary** (`AS<asn> | <name> | net_id <id> | <url>`) — plus a **More Tools**
overflow menu with quick external lookups for that ASN: BGP.TOOLS, BGP.HE, RIPEstat, BGPView,
CIDR Report, IPinfo, Cloudflare Radar, RouteViews, and the raw PeeringDB API response.

!!! tip "📸 Screenshot needed"
    The "More Tools" dropdown open on a network page, showing the full list of external lookups.

**Copy URL** — on any entity page, copies `<entity name> | <page URL>` to the clipboard, handy
for pasting record references into tickets or chat.

## Admin Ops toolkit (opt-in, off by default)

This is the richest feature set in the script, but it's hidden until you turn on **Admin Ops
Mode** — nothing described in this section appears otherwise.

Enable it via the Tampermonkey menu command **`FP: Admin Ops Mode [OFF] (toggle to ON)`** (it
relabels itself to confirm once on). When enabled, entity pages gain an **Open API** button and
an **Admin Ops** overflow menu whose contents adapt to the entity type and available data:

| Item | Shows when | What it does |
|---|---|---|
| Open CP Org | Non-org entity with a resolvable parent org | Opens the parent org's CP page. |
| Open CP User Manager | Parent org resolvable | Opens the parent org's CP page, jumped to the user-manager section. |
| Copy Entity IDs | Always | Copies a compact `type=…; id=…; org_id=…; asn=…; …` reference line. |
| Copy Triage Summary | Always | Copies a multi-line summary (type, id, name, org, ASN, website, IRR AS-SET, traffic, URL) ready to paste into a ticket. |
| CP Search Pack | Always | Builds and opens CP account-email search links from the entity's name/ASN/visible org-user info (asks first if it would open more than a couple of tabs). |
| Open Related Objects | Related netixlan/netfac/POC rows visible | Opens those related records' pages, plus the parent org. |
| Email Domain Inspector | Org pages | Tallies the email domains among visible org users and copies a domain→count report — a quick signal for anomalies (one org, many unrelated domains). |
| Validate External Links | Always | Checks up to 8 visible external links (e.g. website) for HTTP errors and copies a status report. |
| Compare UI vs API | Always | Diffs what's rendered on the page against the same fields from the live API, to catch stale/cached rendering. |
| Prefix Sanity Check | Network pages | Flags implausible IPv4/IPv6 prefix counts (negative, or unrealistically high). |
| Suspicious Signals | Always | A quick automated triage checklist: missing/short name, missing website, missing ASN or IRR AS-SET, an org with no visible user emails, or an org whose users span several distinct email domains. |
| Audit Trail Jump | Always | Opens the CP changelist for this entity type, pre-filtered by ID. |
| Soft Reset Form | Always | Clears leftover error/loading states from in-page edits — no data changes. |

Everything in this menu either copies text to the clipboard or opens tab(s) — nothing renders
inline on the page except the menu itself.

!!! tip "📸 Screenshot needed"
    The "Admin Ops" dropdown open on an org page, showing the full conditional item list.

## Org page enhancements

**User-manager row icons** — in the "Users You Can Manage" panel and pending-affiliation-request
list, every row gains:

- 🔍 next to the username — searches CP's account-email admin by username.
- 🪪 next to the username (active users only) — opens that user's CP record directly.
- 🔍 next to each email — searches CP by that email.
- 📋 next to each email — copies it to the clipboard.
- 📋 next to any ASN a requester mentioned in their affiliation request text — copies just the
  digits.
- A compact 🔐 icon replacing the host UI's bulkier 2FA badge.

An **Admin 📧** button near the user-manager's submit button copies the email addresses of the
org's **admin**-role users (not members) to the clipboard in one click.

!!! tip "📸 Screenshot needed"
    An org's user-manager row showing the 🔍/🪪/📋/🔐 icon cluster next to a username and email,
    plus the "Admin 📧" button near the submit button.

**CP edit shortcuts on related-object listings** — every row in an org's Facility, Network,
Internet Exchange, Carrier, and Campus listings gets a small ⚙️ gear-icon link on the right,
opening that specific record's CP change page directly. Applies to every row regardless of
status.

!!! tip "📸 Screenshot needed"
    An org page's Facility (or Network/IX/Carrier/Campus) listing row with the ⚙️ gear icon
    visible on the right edge.

**CP edit shortcuts on OAuth applications** — in the "Manage OAuth Applications" panel, a
**CP (oauth:`<id>`)** button appears next to each application's existing "Details" button,
linking to that application's CP change page.

!!! tip "📸 Screenshot needed"
    The OAuth Applications panel showing the new "CP (oauth:…)" button next to "Details".

## Tampermonkey menu commands

- `FP: Copy URL` / `FP: Copy AS<N>` — click the page's own copy button, if present.
- `FP: Open Admin Console` — opens the current page's CP link, if present.
- `FP: Admin Ops Mode [ON/OFF] (toggle to ON/OFF)` — the switch for the whole Admin Ops toolkit.
- `FP: Debug Mode [ON/OFF] (toggle to ON/OFF)`
- `FP: Log User-Agent (Debug ON/OFF)`
- `FP: Feature Flags (show in console)` / `FP: Feature Flags (reset overrides)`
- `FP: Feature <flagName> [ON/OFF]` — one per flag (`adminOpsMode`, `debugMode`,
  `moduleDispatch`).

## Configuration

### Disabling individual modules

```js
localStorage.setItem("pdbFpConsolidated.disabledModules", '["copy-user-roles"]');
```

Module IDs: `fix-double-slashes`, `asn-404-cp-search-redirect`, `set-window-title`,
`navbar-cp-link`, `admin-console-link`, `copy-record-data`, `admin-workflow-buttons`,
`copy-user-roles`, `org-related-listing-cp-edit-links`, `org-oauth-cp-edit-links`.

### Admin Ops Mode

The practical on/off switch for the toolkit in that section above — toggle it via the
Tampermonkey menu command, or directly:

```js
localStorage.setItem("pdbFpConsolidated.adminOpsMode", "1");   // on
localStorage.removeItem("pdbFpConsolidated.adminOpsMode");     // off
```

### Debug mode

See [Debug mode](index.md#debug-mode) on the overview page — shared with CP and DP.

## Troubleshooting

- **Admin Ops menu isn't showing up** — it's opt-in; confirm `adminOpsMode` is enabled (see
  above) and reload the page.
- **One feature is misbehaving but the rest work fine** — disable just that module (see
  Configuration above) rather than the whole script, and file an issue with the module ID.
