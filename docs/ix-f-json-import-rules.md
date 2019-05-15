# Rules for the IX-F JSON Importer
PeeringDB allows networks and IXes to contol entries via the IX-F JSON import feature.

## General remarks
If and how information is imported heavily depends on the `state` field. So, both network and IX should check what is set. The importer has been modified to act on `active`, `connected`, `operational` or if the `state` is not set at all. If `state` is set to `inactive` nothing is done, even if the network has set `allow_ixp_update` to yes.

If a network is in the IX-F JSON import but not in PeeringDB it is not added.

See [GitHub #474](https://github.com/peeringdb/peeringdb/issues/474) for the exact specification.

## For networks
There is a tick box "Allow IXP Update". Per **default** this is unticked (set to "no")

`allow_ixp_update`: no
- If a network has an IX entry with differing (asn, ipaddr4, ipaddr6), the network IX entry is removed
- If a network has an IX entry with any other differing information (speed, route server peer), this information is not changed
- If a network does not have an entry for the IX, nothing is done

`allow_ixp_update`: yes
- If a network has an IX entry with any differing information, the entry is updated (IPv4, IPv6, speed, route server peer)
- If a network does not have an entry for the IX, one is added
- If a network does not have an entry in the IX member list, the network IX entry is removed

## For IXes
To enable IX-F JSON import, please provide a URL to your IX-F JSON export list. To do so, edit your entry and add the URL in field `LANs`. Make sure that your JSON file is [valid](https://www.ixpdb.net/en/validator/).
