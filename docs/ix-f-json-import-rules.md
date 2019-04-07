# Rules for the IX-F JSON importer
PeeringDB allows networks and IXes to contol entries via the IX-F JSON import feature.
## For networks
There is a tick box "Allow IXP Update". Per **default** this is unticked (set to "no")

`allow_ixp_update`: no
- If a network has an IX entry with both differing IP addresses, the network IX entry is removed
- If a network has an IX entry with any other differing information (speed, route server peer), nothing is done
- If a network does not have an entry for the IX, nothing is done

`allow_ixp_update`: yes
- If a network has an IX entry with any differing information, the entry is updated (IPv4, IPv6, speed, route server peer)
- If a network does not have an entry for the IX, one is added
- If a network does not have an entry in the IX member list, the network IX entry is removed

## For IXes
To enable IX-F JSON import, please provide a URL to your IX-F JSON export list. To do so, edit your entry and add the URL in field `LANs`. Make sure that your JSON file is [valid](https://www.ixpdb.net/en/validator/).

**Note**: If a state is not set at all, it will be seen as `active` by default. **If state is set** the importer accepts only `active` or `connected` to qualify the entry for import. If state is set to something else, the **entry will be removed**
