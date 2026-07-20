# CP — Consolidated Tools

Runs on Control Panel (Django admin) change pages:
`https://www.peeringdb.com/cp/peeringdb_server/*/*/change/*` (and the `beta.peeringdb.com`
equivalent). This is the script AdminCom members spend the most time in — it covers Network,
Facility, Internet Exchange, Carrier, Campus, Organization, and User review/edit workflows.

See [Installing](index.md#installing) on the overview page if you haven't added this script yet.

!!! tip "📸 Screenshot needed"
    A CP network change page with the script active, wide enough to show the toolbar buttons and
    the status/RIR badges near the page title — used as a general orientation shot at the top of
    this page.

## Update Name — the flagship feature

The **Update Name** toolbar button (secondary action row, below the main toolbar) appears on
every entity type. One click sets the entity's name from its parent organization (for
Organization/Facility/IX pages, it normalizes the org's own name), then saves automatically.

!!! tip "📸 Screenshot needed"
    The "Update Name" button in the secondary action row, before clicking.

What happens under the hood, in order:

1. **Trading-as / DBA splitting.** A combined name like `Foo Corp, trading as Bar Networks`
   is split into Name = `Bar Networks`, with `Foo Corp` routed into the **AKA** field and the
   **Long Name** field.
2. **Person / trade-name splitting** (for RIRs that use this convention, e.g. some LACNIC/
   Guatemala registrations): a name like `EDWIN HERNÁNDEZ PEC (IMPORTADORA Y EXPORTADORA
   INTERCEL)` is split into Name = the trade name, AKA = the person's name, Long Name = the
   original combined string.
3. **RDAP fallback for networks.** If the resulting name still looks like an auto-generated
   handle (all-caps dashed tokens, `AS12345`-shaped strings, NIR registry prefixes like
   `IDNIC-`/`AFRINIC-`), the script looks up the real registrant name via RDAP (using IANA's
   RDAP bootstrap registry to find the right RIR) before giving up.
4. **Housekeeping**: appends ` #<id>` to the name if the entity's status is `deleted` (keeps
   duplicate names distinguishable in audits/history), and clears the deprecated "Floor" field
   on facility-adjacent networks.
5. **Auto-fixes a known validation error**: if the save fails because a POC's visibility is set
   to the deprecated "Private" option, the script flips it to "Users" and retries.
6. **Duplicate-name retry**: if the server rejects the name because another network already has
   it, the script retries once with an ` (AS<asn>)` suffix appended.
7. On success, redirects you straight to the entity's History page so you can see the diff.

!!! tip "📸 Screenshot needed"
    A before/after of the Name / AKA / Long Name fields on a network that went through the
    trading-as or person/trade-name split.

The button is intentionally disabled (with a toast explaining why) while an entity's status is
`pending`, and for a small hard-coded list of "Example Organization" test records — so it can't
accidentally rewrite a record still awaiting initial review, or corrupt the dummy/test org used
for QA.

### Configuring a keyboard shortcut

Update Name can be bound to a keyboard combo so you don't have to scroll to the button on every
record. From the Tampermonkey menu (click the extension icon while on a CP change page):

1. Choose **`CP: Set Update Name Shortcut...`**.
2. Enter a combo such as `Alt+U` or `Ctrl+Shift+N` when prompted. The combo **must** include
   Ctrl, Alt, and/or Meta — Shift alone is rejected — so it can never fire while you're just
   typing into a form field.
3. The menu item relabels itself to confirm, e.g. **`CP: Update Name Shortcut [Alt+U]
   (change...)`**. Choosing it again lets you change or clear the combo.

Pressing the combo simply clicks the real button, so every check above (pending guard, dummy-org
guard, retries) still applies exactly as if you'd clicked it yourself. No shortcut is set by
default. Stored in `localStorage["pdbCpConsolidated.updateNameShortcut"]`.

!!! tip "📸 Screenshot needed"
    The Tampermonkey prompt for entering a shortcut combo, and the resulting relabeled menu item.

## Network review & cleanup

**Reset Information** — appears only on a **deleted** network's change page. Wipes nearly every
editable field back to defaults (text/URL fields, prefix counters, checkboxes, social links,
policy fields), re-derives the name from the organization (same RDAP fallback as Update Name),
and auto-saves. Asks for confirmation first, naming the target network by ID/ASN/name.

!!! tip "📸 Screenshot needed"
    The "Reset Information" button and its confirmation dialog on a deleted network.

**RIR/IRR status badges** — next to the page title on a network change page:
a colored **RIR: `<status>`** badge (green = ok, red = invalid, orange = pending, gray = n/a)
and, when available, an **IRR: `<as-set>`** badge. Hover for the last-updated date.

!!! tip "📸 Screenshot needed"
    The RIR/IRR badges next to a network's page title, ideally one green and one red/orange
    example side by side.

**Inline delete-row highlighting** — any inline row (POC, netfac, netixlan) with its **Delete**
checkbox ticked gets a red-tinted background, so it's obvious what you're about to remove before
you hit Save.

!!! tip "📸 Screenshot needed"
    An inline netixlan or POC row with the Delete checkbox ticked, showing the red highlight.

A couple of quieter safety nets run in the background here too: stale `deleted`-status inline
rows are automatically marked for real deletion on save, and deprecated "Private" POC visibility
is normalized to "Users" so saves aren't rejected for a reason you didn't cause.

## Internet Exchange / IX-F workflow

**Request IXF Import** — toolbar button on an IX change page; triggers a fresh IX-F import via
the API.

**IXF status badge** — next to the IX page title: **IXF: `<status>`** (queued/importing =
orange/blue, finished = green, error = red), hover for the last-import date. If the ixlan
publishes a member list URL, a **Members** link appears alongside it.

!!! tip "📸 Screenshot needed"
    An IX change page showing the "Request IXF Import" button and the IXF status badge together.

## IX-F & netixlan bulk tools (networkixlan changelist)

These three tools live on the **networkixlan changelist** (list page, not a single record's
change page) and are the most powerful — and most consequential — tools in the script. Use them
deliberately; each requires an explicit confirmation before anything is written or deleted.

### Audit IX-F Members

Toolbar button **"Audit IX-F Members"**. Prompts for an ixlan ID if the page isn't already
filtered to one, then fetches that ixlan's upstream IX-F member list and compares it against
PeeringDB's netixlan rows, looking for cases where an IX-F member's IPv4 and IPv6 addresses are
split across two separate PeeringDB rows that should really be one. Presents a table of
candidates with **Re-scan**, **Apply merges**, and **Recent IP changes** actions. Merging keeps
the older (lower-id) row and folds in the missing address, then removes the sibling row.

!!! tip "📸 Screenshot needed"
    The "IX-F Member Audit" modal with a populated candidate table.

### Renumber IXLAN Peers

Toolbar button that opens a modal for bulk-renumbering peers on an ixlan (old prefix → new
prefix). It classifies every affected netixlan row as eligible / no-change / conflict / skipped,
lets you review before applying, and calls out conflicts in a red banner. Typically launched via
a link generated by the [DeskPro renumber tool](deskpro.md#ixlan-renumber-launcher) from a
support ticket, rather than opened cold from CP.

!!! tip "📸 Screenshot needed"
    The "Renumber IXLAN Peers" modal showing a mix of eligible, conflict, and skipped rows.

**Conflict resolution** (opened from inside the Renumber modal when conflicts exist) walks
through a multi-step verification chain (matching ASN, matching ixlan, cross-checking the
current IX-F member list, re-reading the row immediately before any delete) before letting you
proceed, and only enables the delete action once you type the exact ixlan ID into a confirmation
box. Nothing that would lose data is deleted without first merging in whatever fields the
surviving row was missing.

!!! tip "📸 Screenshot needed"
    The conflict-resolution modal, especially the ixlan-ID confirmation box gating the delete
    action.

### Recent IP Changes

A read-only report (reachable as its own toolbar button, or from inside either modal above)
combining live API data with a local log of what the two tools above have done recently — useful
for confirming "did that renumber/merge actually take effect" even after the live data has moved
on. Output is plain text with a **Copy** button.

!!! tip "📸 Screenshot needed"
    The "Recent IP Changes" report window with a few example entries.

## Copy & link helpers (all entity types)

- **API JSON** — opens the entity's raw `/api/<resource>/<id>` response in a new tab.
- **Copy `<Entity>` URL #`<id>`** — copies `Name | https://www.peeringdb.com/<slug>/<id>` to the
  clipboard (label adapts per entity type: Network, Facility, Org, Carrier, IX, Campus).
- **Copy Org URL #`<orgId>`** — same idea, for the parent organization.
- **Copy User Profile URL #`<id>`** — on User pages.
- A small **⧉** copy icon next to almost every rendered field value on the page (skips noisy
  fields like logo/status/IX-F metadata). The **Prefixes** field additionally gets **BGP.HE** and
  **BGP.TOOLS** links that open the prefix directly on those sites.
- **`<Entity>` Website** / **Org Website** buttons that open the relevant Website field, reusing
  the same browser tab on repeat clicks instead of spawning a new one each time.
- **`<Entity>` (FP)** / **Org (FP)** / **Org (CP)** buttons for one-click cross-navigation to the
  public frontend or the parent org's CP page. On an IX page with at least one ixlan, an
  **IXLAN Prefix (CP)** button is added too. If the entity's own status isn't `ok`, the FP button
  is shown disabled and relabeled to say so, rather than sending you to a page that 404s.
- On `networkixlan` change pages specifically: **Org (CP)**, **Network (CP)**, **IX (CP)**
  buttons for quick cross-navigation.

!!! tip "📸 Screenshot needed"
    A change page's secondary action row showing several of these buttons together (Copy URL,
    Website, FP/CP cross-links), plus a close-up of the ⧉ copy icon next to a field.

## Facility-specific helpers

- **Maps** dropdown — Google Maps / Bing Maps / OpenStreetMap, built from lat/long if present,
  otherwise the street address.
- **Search (FP)** — deep-links to the public advanced search filtered by the facility's
  country/state/zip, handy for spotting duplicate facility listings.

!!! tip "📸 Screenshot needed"
    The "Maps" dropdown open, showing its three map-provider options.

## User / security lookups

On a User change page:

- **TOTP Device / Security Key** quick links (single button if there's one device, a dropdown
  if there are several) — jump straight to that MFA device's own admin record.
- **OTP Email** / **OTP Static** links — since those device types don't show inline on the User
  page, these link to a username-filtered search on their respective changelists instead.
- **Search Username** — deep-links to the email-address admin filtered by this user's username,
  a quick way to see every email address tied to an account during an identity/security review.

!!! tip "📸 Screenshot needed"
    A User change page showing the MFA device quick-link buttons/dropdowns.

## Visual state cues

- **Status badges** on the page title: **PENDING** (orange) or **DELETED** (red) for any entity
  in that state; **CHILD OF DUMMY ORGANIZATION** (red) specifically for a facility whose parent
  org is the test/dummy organization. These update live if you change the Status or Org dropdown
  without reloading.
- **Window/tab titles** are rewritten to something identifiable — e.g.
  `PDB CP | NETWORK | Name | Country` — so it's easy to tell CP tabs apart when you have several
  open.
- **History page timestamps** are rewritten from ambiguous 12-hour form ("Sept. 26, 2025,
  10:42 p.m.") to unambiguous 24-hour ISO form, with the original kept as a hover tooltip.

!!! tip "📸 Screenshot needed"
    A pending or deleted entity showing its status badge and background tint near the page title.

## List-page (changelist) diagnostics

- **Analyze Network Names** — on the Network changelist, bulk-scans network names looking for
  ones that appear auto-generated or placeholder (numeric-only, `ASxxxxx`-shaped, NIR registry
  prefixes, "test"/"dummy" keywords, etc.), and copies a worklist (with a link to each record's
  change page) to the clipboard for follow-up.
- **Copy Change Links** — on any entity's changelist, copies every visible row's `/change/` URL
  from the current filtered/paginated view, one per line — useful for building a batch of links
  to review or paste into a ticket.

!!! tip "📸 Screenshot needed"
    The Network changelist toolbar showing the "Analyze Network Names" button, mid-scan
    ("Scanning 3/6" or similar progress text) if possible.

## Approvals

**Approve** / **Reject** buttons on a CarrierFacility change page, calling the corresponding API
endpoint directly.

!!! tip "📸 Screenshot needed"
    The Approve/Reject buttons on a CarrierFacility change page.

## Tampermonkey menu commands

Commands that mirror an on-page button (only appear when that button exists on the current
page):

- `CP: Update Name`
- `CP: Copy Entity URL`
- `CP: Copy User Profile URL`
- `CP: Copy Org URL`
- `CP: Reset Information`

Always-available commands:

- `CP: Set Update Name Shortcut...`
- `CP: Clear Org Name Cache`
- `CP: Clear RDAP Cache`
- `CP: Debug Mode [ON/OFF] (toggle to ON/OFF)`
- `CP: Log User-Agent (Debug ON/OFF)`
- `CP: Feature Flags (show in console)`
- `CP: Feature Flags (reset overrides)`
- `CP: Feature <flagName> [ON/OFF]` — one toggle per advanced feature flag (see below)

## Configuration

### Disabling individual modules

Set `localStorage["pdbCpConsolidated.disabledModules"]` to a JSON array or comma-separated
string of module IDs, then reload the page:

```js
localStorage.setItem("pdbCpConsolidated.disabledModules", '["reset-network-information"]');
```

Module IDs used above, for reference: `set-entity-name-equal-org-name`, `reset-network-information`,
`network-rir-status-badge`, `ixf-import-status-badge`, `request-ixf-import`,
`ixlan-renumber-peers`, `ix-f-member-audit`, `recent-ip-changes`, `copy-frontend-urls`,
`copy-rendered-field-values`, `entity-website-header-links`, `frontend-links`,
`facility-google-maps`, `facility-advanced-search-link`, `user-mfa-device-quick-links`,
`search-user-email-by-username`, `entity-state-visuals`, `set-window-title`,
`history-24h-timestamps`, `network-name-pattern-diagnostics`, `copy-overview-change-links`,
`carrierfac-approve-reject`, `inline-delete-row-highlights`.

### Advanced feature flags

A separate mechanism gates the riskier netixlan bulk tools (all default **on**); manage these
via the Tampermonkey menu commands rather than editing localStorage directly:
`ixlanRenumber`, `ixfMemberAudit`, `conflictResolver`, `recentIpChanges`, `orgUpdateAuditLog`,
`moduleDispatch`, `debugMode`.

### Debug mode

See [Debug mode](index.md#debug-mode) on the overview page — shared with FP and DP.

## Troubleshooting

- **A button/badge you expect isn't showing up** — check you're not on a `pending` entity for
  Update Name, or a non-`deleted` one for Reset Information; both are intentionally gated.
- **One feature is misbehaving but the rest work fine** — disable just that module (see
  Configuration above) rather than the whole script, and file an issue with the module ID.
- **Something feels stale/cached** — `CP: Clear Org Name Cache` and `CP: Clear RDAP Cache` reset
  the two caches this script keeps for name-normalization lookups.
