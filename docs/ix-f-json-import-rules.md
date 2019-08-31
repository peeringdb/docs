# Rules for the IX-F JSON Importer (This feature is disabled since 2019-08-30, i.e. the last import ran at 2019-08-30 00:00:00 UTC)
PeeringDB allows networks and IXPs to contol entries via the IX-F JSON import feature.

## General remarks
If and how information is imported heavily depends on the `state` field. So, both the network and the IXP should check what is set. The importer has been modified to act on `active`, `connected`, `operational` or if the `state` is not set at all. If `state` is set to `inactive` nothing is done, even if the network has set `allow_ixp_update` to yes.

If a network is in the IX-F JSON import but not in PeeringDB it is not added.

See [GitHub #474](https://github.com/peeringdb/peeringdb/issues/474) for the exact specification.

## For networks
**Generally, if a network does not have an entry in the IXP member list, the network IXP entry is removed.**

There is a tick box "Allow IXP Update" which governs the behaviour of the import. By **default** this is unticked (set to "no"). If "Allow IXP Update" is ticked, an entry may be created, changed and removed. The entry then is completely governed by the settings in the IX-F JSON import. If "Allow IXP Update" is unticked, an entry may be removed. For details see below.

`allow_ixp_update`: no
- If a network has an IXP entry with differing (asn, ipaddr4, ipaddr6), the network IXP entry is removed
- If a network has an IXP entry with any other differing information (speed, route server peer), this information is not changed
- If a network does not have an entry for the IXP, nothing is done

`allow_ixp_update`: yes
- If a network has an IXP entry with any differing information, the entry is updated (IPv4, IPv6, speed, route server peer)
- If a network does not have an entry for the IXP, one is added

## For IXPs
To enable IX-F JSON import, please provide a URL to your IX-F JSON export list. To do so, edit your entry and add the URL in field `LANs`. Make sure that your JSON file is [valid](https://www.ixpdb.net/en/validator/).
