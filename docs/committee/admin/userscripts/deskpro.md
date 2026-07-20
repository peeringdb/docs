# DeskPro — Consolidated Tools

Runs inside DeskPro (`https://peeringdb.deskpro.com/app*`), the support desk AdminCom uses for
network/IX/facility/carrier approval requests, ownership/affiliation requests, and IXLAN
renumbering tickets. Unlike the CP and FP scripts, this one isn't built from small toggleable
modules — it's a set of always-on ticket enrichments plus two opt-in workflow launchers gated by
feature flags.

See [Installing](index.md#installing) on the overview page if you haven't added this script yet.

## Automatic ticket enrichment

All of the following happens automatically as you read a ticket — nothing to click, and it never
touches text you're actively typing in the composer.

### ASN mentions become links

Text like `AS12345`, `ASN12345`, `member ASN: 12345`, or a bare standalone number in a context
that's clearly about an ASN (near IPv4/IPv6 addresses, in a member-table block, or right after a
line mentioning "ASN") is turned into a link to that ASN's PeeringDB page, with the PeeringDB
favicon appended.

The link's label and tooltip then fill in progressively in the background: first with the
resolved network name (`AS12345 (Example Network)`), then — if it resolves — a multi-line
tooltip with the org name and POC list.

!!! tip "📸 Screenshot needed"
    A ticket body with an ASN mention rendered as a link with the small favicon, then a follow-up
    screenshot showing the multi-line tooltip (network name / org / POCs) after it finishes
    loading.

### Organization names become search links

Text matching `wishes to be affiliated to Organization 'Org Name'` (any quote style) turns the
quoted org name into a link to a PeeringDB search for that name — handy for immediately checking
whether the org already exists before approving an affiliation request.

!!! tip "📸 Screenshot needed"
    An affiliation-request ticket with the quoted org name rendered as a search link.

### Existing PeeringDB links get smarter tooltips

Any `peeringdb.com` link already present in a ticket (pasted by a requester, or rendered by
DeskPro itself) gets its tooltip enriched on hover — for example, a `net/1234` link's tooltip
becomes `net/1234 | <name> | AS<asn> | Org <org name> | POCs <role (email), ...>`, and a CP
change-page link's tooltip names the object type and ID. If the linked object turns out to be
missing from the public frontend (e.g. still pending review), the link is silently redirected to
the equivalent CP change page instead of leading to a dead end.

!!! tip "📸 Screenshot needed"
    Hovering an existing `net/1234` (or similar) link in a ticket, showing the enriched tooltip.

### Email addresses get copy/search helpers

Every `mailto:` link in a ticket is decorated with a 📋 (copy) and 🔍 (search-by-email-in-CP)
affordance. Clicking the email text itself copies the address to the clipboard (rather than
opening a mail client) and briefly flashes "Copied: `<email>`" as confirmation.

!!! tip "📸 Screenshot needed"
    A ticket contact row showing an email address with its 📋 and 🔍 icons, and a follow-up shot
    of the "Copied: ..." tooltip right after clicking.

### Malformed CP links are fixed automatically

Any link containing the double-slash typo `peeringdb.com//cp/peeringdb_server` is silently
corrected to the proper single-slash form. Not visually distinctive — nothing to screenshot here.

## Whitelist CMD Generator

Menu command: **`DP: Generate Whitelist CMD`**. Use this while reviewing an IX / Network /
Facility / Carrier approval (or `[SUGGEST]`) ticket that contains a link to that object's CP
change page.

1. Run the command from the Tampermonkey menu while the ticket tab is active.
2. The script finds every PeeringDB object referenced in the ticket, fetches each one live from
   the API (deliberately without caching, so a still-pending object shows up correctly rather
   than as a stale miss), and opens a **Whitelist CMD Generator** modal.
3. If more than one object was found, pick the right one from the dropdown.
4. Confirm or edit the pre-filled **Hostname** field (taken from the object's website).
5. The modal shows the exact domains that will be whitelisted (the hostname, its apex domain, and
   the `www.` variant) and the ready-to-run command, e.g.:

   ```
   pihole allow "example.com" "www.example.com" --comment "PeeringDB DeskPro ticket 12345 - Internet Exchange Request"
   ```

6. Click **Copy** and paste the command into your pihole/ad-blocker admin.

!!! tip "📸 Screenshot needed"
    The full "Whitelist CMD Generator" modal with a populated hostname, candidate domains, and
    generated command.

## IXLAN Renumber launcher

Menu command: **`DP: Renumber IXLAN Peers`**. Use this on a renumbering ticket that mentions an
old and new prefix (any of `->`, `=>`, `→`, or the word "to" between them, for IPv4 and/or IPv6
independently).

1. Run the command while the ticket tab is active.
2. The script scans the ticket for old→new prefix pairs and for a CP `ixlan/{id}/change/` link,
   pre-filling a confirmation modal with whatever it found.
3. Review and edit the IPv4/IPv6 old/new fields and the ixlan ID as needed.
4. Click **Open in CP** — this opens the CP networkixlan changelist with the reviewed values
   encoded in the page's URL fragment, which the [CP script's Renumber IXLAN Peers
   tool](cp.md#renumber-ixlan-peers) reads to pre-populate its own confirmation view.

This launcher never modifies PeeringDB data itself — it only detects the prefix pair, lets you
confirm or correct it, and hands off to CP, where the actual renumbering (with its own review and
confirmation step) happens.

!!! tip "📸 Screenshot needed"
    The "Renumber IXLAN Peers" confirmation modal with pre-filled old/new IPv4 and/or IPv6 rows.

## Menu commands

- `DP: Debug Mode [ON/OFF] (toggle to ON/OFF)`
- `DP: Feature Flags (show)` / `DP: Feature Flags (reset)`
- `DP: <flagName> [ON/OFF]` — one per flag (`whitelistCmdGenerator`, `ixlanRenumber`)
- `DP: Generate Whitelist CMD` — only present while `whitelistCmdGenerator` is enabled
- `DP: Renumber IXLAN Peers` — only present while `ixlanRenumber` is enabled

!!! note
    Toggling `whitelistCmdGenerator` or `ixlanRenumber` takes effect on the **next page load** —
    the corresponding menu command isn't added or removed live.

## Configuration

Both workflow launchers default to **on**. Toggle them from the Tampermonkey menu, or directly:

```js
localStorage.setItem("pdbDp.featureFlags", JSON.stringify({ ixlanRenumber: false }));
```

### Debug mode

See [Debug mode](index.md#debug-mode) on the overview page — shared with CP and FP.

## Troubleshooting

- **Neither launcher command shows up in the Tampermonkey menu** — reload the DeskPro tab after
  changing a feature flag; the commands are only (re-)registered at page load.
- **Whitelist Generator says no PeeringDB object was found** — it only looks at CP change-page
  links currently visible in the active ticket tab; make sure the relevant link is in the ticket
  body and that ticket's tab is the foregrounded one.
