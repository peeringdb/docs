# AdminCom Userscripts

The Admin Committee maintains three browser userscripts that streamline day-to-day moderation
work across the three tools AdminCom members actually use: the PeeringDB Control Panel, the
public PeeringDB site, and the DeskPro support desk. Source lives in the
[`peeringdb/admincom`](https://github.com/peeringdb/admincom) repository, under `user.js/`.

| Script | Runs on | Guide |
|---|---|---|
| **CP — Consolidated Tools** | `peeringdb.com/cp/peeringdb_server/*/*/change/*` (Control Panel change pages) | [CP guide](cp.md) |
| **FP — Consolidated Tools** | `peeringdb.com/*` (public frontend, excluding `/cp/`) | [FP guide](fp.md) |
| **DP — Consolidated Tools** | `peeringdb.deskpro.com/app*` (DeskPro support desk) | [DeskPro guide](deskpro.md) |

!!! tip "📸 Screenshot needed"
    A composite or three side-by-side screenshots showing each script's Tampermonkey icon/badge
    active in the browser toolbar on its respective site (CP change page, a public entity page,
    and a DeskPro ticket).

## Installing

1. Install the [Tampermonkey](https://www.tampermonkey.net/) browser extension.
2. Open the `.meta.js` URL for the script you want (Tampermonkey will offer to install it, and
   will check this URL periodically for updates):
    - CP: `https://raw.githubusercontent.com/peeringdb/admincom/master/user.js/peeringdb-cp-consolidated-tools.meta.js`
    - FP: `https://raw.githubusercontent.com/peeringdb/admincom/master/user.js/peeringdb-fp-consolidated-tools.meta.js`
    - DeskPro: `https://raw.githubusercontent.com/peeringdb/admincom/master/user.js/peeringdb-deskpro-tools.meta.js`
3. Confirm the install prompt. Tampermonkey pulls the matching `.user.js` file automatically.

You only need to install the scripts that match tools you actually use — for example, if you
never touch DeskPro, you can skip the DP script entirely.

!!! tip "📸 Screenshot needed"
    The Tampermonkey "Install this script?" confirmation dialog for one of the three scripts.

## Concepts shared across all three scripts

These scripts were built together and share a few conventions worth knowing before diving into
the per-script guides.

### Modules and feature flags

Each script is broken into small, independently-toggleable **modules** (CP has 27, FP has 10;
the DeskPro script uses a smaller set of **feature flags** instead of modules — see its guide).
If one feature misbehaves, you don't have to disable the whole script — just that module, from
the browser console (F12 → Console tab):

```js
// CP: disable a single module
localStorage.setItem("pdbCpConsolidated.disabledModules", '["reset-network-information"]');

// FP: disable a single module
localStorage.setItem("pdbFpConsolidated.disabledModules", '["copy-user-roles"]');

// Re-enable everything again
localStorage.removeItem("pdbCpConsolidated.disabledModules");
localStorage.removeItem("pdbFpConsolidated.disabledModules");
```

Reload the page after changing this for it to take effect. The per-script guides list every
module ID you can use here.

### Tampermonkey menu commands

Every script registers commands under its Tampermonkey icon (visible when you're on a page the
script runs on) — click the Tampermonkey toolbar icon, then the script's name, to see the list.
Commands include things like debug-mode toggles and, for CP, the flagship "Update Name" shortcut
configuration.

!!! tip "📸 Screenshot needed"
    The Tampermonkey extension menu open, showing one script's list of registered commands.

### Debug mode

All three scripts share one debug-logging switch. Turning it on (via any script's `Debug Mode`
Tampermonkey menu command, or directly with the snippet below) enables verbose console logging
for all of them at once, since CP and FP share an origin (`peeringdb.com`) and DP has its own
copy scoped to `peeringdb.deskpro.com`:

```js
localStorage.setItem('pdbAdmincom.debug', '1');
```

Turn it back off the same way (`'0'` or remove the key) once you're done diagnosing an issue —
it's noisy in normal use.

### Reporting problems

File an issue at [peeringdb/admincom](https://github.com/peeringdb/admincom/issues) — every
script's Tampermonkey `@supportURL` points there too.
