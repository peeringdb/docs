# IX-F JSON Importer
PeeringDB allows networks and IXPs to update entries via the IX-F JSON import feature.

## General remarks
The Importer abides by the recommendations of the [Data Ownership Task Force](/taskforce/dataownership) and its resulting [Policy Document](/gov/misc/2020-04-06_PeeringDB_Data_Ownership_Policy_Document_v1.0.pdf). Most significantly, this means that unless the tick box "Allow IXP Update" is enabled by a network, published data will not automatically become unpublished nor will unpublished data automatically become published.

## For Networks
There is a tick box "Allow IXP Update" which governs the behavior of the Importer. By **default** this is set to disabled.

If "Allow IXP Update" is enabled, a network entry at an IX may automatically be created, changed, or removed. The network's IX entry is completely governed by the settings in the IX-F JSON data provided by the IX.

If "Allow IXP Update" is disabled, differences in data provided by the IX and the network will result in the following:

- An email to the network with details about the differences.
- An email to the IX with details about the differences.
- Admins for the network will see hints for their network within the PeeringDB web interface. These hints may be accepted or dismissed.
- The network and the IX are encouraged to reach out to each other to resolve any differences.

IXP Update Tools:

- The "Preview" button shows a preview of changes that will be done to your network during the next IX-F import, if "Allow IXP Update" is enabled.
- The "Postmortem" button shows a log of changes done to you network -> exchange connections as a result of IX-F imports.

## For IXPs
To enable IX-F JSON import:

- Make sure that your JSON file is [valid](https://www.ixpdb.net/en/validator/).
- Provide a URL to your IX-F JSON data. To do so, click Edit on your IX web page and set the `IX-F Member Export URL` to the URL and set `Enable IX-F Import` to enabled. You may also set the visibility of your IX-F JSON URL.
- Daily at 0000 UTC, the IX-F JSON data will be retrieved and processed by the Importer. The steps above for networks will then be followed.

If the IX-F JSON `state` field is present, settings of `active`, `connected`, or `operational` may be used to indicate a network is operational, while a setting of `inactive` will be interpreted as the network not being operational. This may be used to denote a network in the process of connecting but not yet active, or a network on hiatus.

IX-F Import Preview:

- The "Preview" button shows the changes that will be performed or suggested, depending on participant network's "Allow IXP Update" setting.
- A JSON form of this preview is available at: https://peeringdb.com/import/ixlan/###/ixf/preview (replace ### with the number that appears in the URL after /ix/ when viewing your IX page)

**Note**: The Importer expects that you also provide IP addresses. If your IX-F JSON has an empty member_list or only contains ASNs, there will be no useful information. You might want to disable the import.

## Further Information
- August 17th, 2020 Data Ownership Policy Implementation Presentation: [slides](/presentation/20200817-dtf-implementation.pdf) and [video](https://youtu.be/mtT_HojbIPs)
