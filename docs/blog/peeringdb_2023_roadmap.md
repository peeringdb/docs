# PeeringDB's Product Roadmap for 2023
We want to build more agility into our Product Management process in 2023. This blog post describes what we have planned for the start of the year. It also describes how we want to work over the whole year, and how you can help us make good choices.

![PeeringDB Roadmap Image](images/peeringdb_roadmap.jpg)

We are starting the year with features that open new paths to us. Your input will help us choose how we move down them.

[Our roundup of 2022](https://docs.peeringdb.com/blog/2022_product_report/) noted that we have some big things planned for the start of 2023. The two biggest are two new objects. We deployed the first in our January release. The new `carrier` object is a way for providers of high capacity links to show which interconnection facilities they are in. We’ve deployed the minimal possible structure for this new object. We want users to tell us what additional features they cannot do without.

The next big new addition is a `campus` object. This will be a way for interconnection facilities to show that inter-building cross-connects are available with the same ease as those within a building. This will help buyers understand when they don't need to be in the same building as something they want to connect to.

We can expand either or both of these objects. We need your feedback to help us decide what would make them more valuable.

Respondents to our annual surveys have consistently told us that Network Configuration Data is what they value most. They are also quite divided about the website design. Some people love its simplicity and others want something more modern.

We knew that we didn't have enough information to make good decisions on how to improve things for the people who want change without disappointing those who like it the way it is. We have deployed Google Analytics for [beta.peeringdb.com](https://beta.peeringdb.com/) and would like to deploy it to [www.peeringdb.com](http://www.peeringdb.com) and [docs.peeringdb.com](https://docs.peeringdb.com/). This will give us important information about how people use our site. We’ll use this information to understand the problems people experience and develop ways to solve them.

We also have lots of users who rely on [our API](https://www.peeringdb.com/apidocs/) or a [local cache](https://docs.peeringdb.com/howto/peeringdb-py/) of PeeringDB data. So, we want to make it easier for users to identify the deltas between what they have in PeeringDB and their local configuration management. This is the focus on the projects we're taking to the [NANOG 87 Hackathon](https://nanog.org/events/nanog-87-hackathon/).

We want to work with tool developers and anyone who relies on PeeringDB as a source of network configuration data. Ultimately, we'd like to offer a way for users to automatically identify deltas, the changes that could be made, and ways to make or approve those changes.

Across the rest of the year, we'd like to focus on one theme at a time and deliver a set of significant improvements there. Then we can move on to the next relevant theme.

So please let us know how we could make PeeringDB more valuable for your organization. As always, you can submit an issue, or comment on existing issues [in GitHub](https://github.com/peeringdb/peeringdb/issues). But you can also [send us email](mailto:productcom@lists.peeringdb.com) or chat to us at various community events.


