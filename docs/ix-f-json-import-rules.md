# Rules for IX-F JSON importer
PeeringDB allows network and IXes to contol entries via the so called IX-F JSON import feature.
## For networks
There is a tick box "Allow IXP Update". Per **default** this is unticked (set to "no")

`allow_ixp_update`: no
- If a network has an IX entry with both invalid IP addresses, the network IX entry is removed
- If a network has an IX entry with any other invalid information (route server peer and speed), nothing is done
- If a network does not have an entry for the IX, nothing is done

`allow_ixp_update`: yes
- If a network has an IX entry with any differing information, the entry is updated (IPv4, IPv6, speed, route server peer)
- If a network does not have an entry for the IX, one is added
- If a network does not have an entry in the IX member list, the network IX entry is removed

## For IXes
To enable IX-F JSON import, please provide a URL to your IX-F JSON export list. To do so, edit your entry and add the URL in field `LANs`. Make sure that your JSON file is [valid](https://ml.ix-f.net/test). 

**Note**: If a state is not set at all, it will be seen as active by default. **If state is set** the importer accepts either `active` or `connected` to qualify the entry for import.
