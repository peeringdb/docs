# Data Quality Improvements: IRRs and AS-SET names
*25 August, 2026*

We’ve now implemented the data quality improvements [we wrote about](../data_quality_for_networks/) last month. You can see this in the editor, which suggests the correct IRR for AS-SET names that exist, and tells you when there’s a miss. From our perspective, this is one of the most exciting improvements we’ve made. We’re grateful to James Bensley for proposing it.

![Name validating editor](images/as-set_validation_in _editor.gif)

We’re automatically updating AS-SET names that are already unique to show the IRR they use. We’ll also notify anyone with an ambiguous AS-SET name that they need to update it. We’ll do this over the next few weeks and hope we’ll see a large proportion of these names fixed soon.

We recognise that this is not the end of the road on better data quality. We know that the changes implemented for [#1973](https://github.com/peeringdb/peeringdb/issues/1973) and [#1974](https://github.com/peeringdb/peeringdb/issues/1974) won't immediately deliver perfection. We’ll be monitoring data quality changes over time.

As we notice opportunities for improvement we are publicly documenting them and will implement them. One we noticed is that some organizations operate multiple networks – for instance, a service network and an enterprise network. Human error could lead to a valid hierarchical AS-SET name being used for the wrong network.

So we’ve created [an issue](https://github.com/peeringdb/peeringdb/issues/2036) to lower this risk for a small set of users.

We’ll report on the data quality improvements later in the year.

If you have an idea to improve PeeringDB you can share it on our low traffic [mailing lists](https://docs.peeringdb.com/#mailing-lists) or create an issue directly on [GitHub](https://github.com/peeringdb/peeringdb/issues). If you find a data quality issue, please let us know at [support@peeringdb.com](mailto:support@peeringdb.com).

--- 

PeeringDB is a freely available, user-maintained, database of networks, and the go-to location for interconnection data. The database facilitates the global interconnection of networks at Internet Exchange Points (IXPs), data centers, and other interconnection facilities, and is the first stop in making interconnection decisions.
