# Should PeeringDB Create a New “Carrier” Object?
That was the question we asked two focus groups on 29 June 2021.

![Photo of Mountain Lake in Lens by Paul Skorupskas on Unsplash](images/mountain_lake_in_lens_paul_skorupskas_unsplash.jpg)

## Initial discussion
Our Product Committee and others have been discussing this issue for about six months now. The one thing we could agree on was that we needed to reach out to more of the people involved in buying and delivering these interconnection services to help make a decision.

## Focus groups
To do that we held two focus groups on 29 June 2021. One was scheduled at a time that is good for people in APAC and the west coast of the Americas. The other was scheduled at a time that was good for people in EMEA and the east coast of the Americas.

The discussion included 12 people with significant industry experience in running carriers, exchanges, facilities, and networks. To build a trusted environment we applied the Chatham House Rule, so this blog post describes what was discussed but does not quote anyone or attribute views to any participants.

The focus groups began with a description of the problem and then looked at a simple approach to address it: an object to describe the carrier and associated objects listing the facilities and IXs where they have a presence.

The focus groups then discussed several questions:

* Is there an unmet need?
* Should PeeringDB be the organization to address it?
* What do you feel about the proposed approach?
* Should the proposed approach be adapted in some way? Why?

There was a strong sense across both sessions that it can be a challenge to find out about connectivity options between locations. While putting information about those options in PeeringDB would not eliminate the need for buyers to perform their own due diligence checks, it would simplify the process of finding out who to contact and what they might be able to offer.

There was support for putting this information in PeeringDB because keeping related information in a single database makes things easier for users.

Participants favored starting off with a less complex object and adding detail in future iterations. Including information about whether links between locations were L1, L2, or L3, and owned or leased seemed to be the agreed minimum set of information. That said, there were concerns that keeping this information accurate could be a challenge for multiple reasons, including inaccurate internal asset databases and a desire from marketing people to overclaim. 

Any implementation would need to be well supported by extensions to the API. Despite making it easy for people to rapidly deploy information about new and improved deployments to PeeringDB through the API there was support ensuring that a new object can be created and configured through the web interface.

## Next steps
When the Product Committee has evaluated the feedback we got from these two focus groups it will make a decision on the principle of creating this new object. 

If the decision is to proceed there is work to be done in both designing and naming it. 

* What is the minimum set of information that would be useful to PeeringDB users?
* What name would cause least confusion?

We’ll keep you updated.

If you have an idea to improve PeeringDB you can share it on our [low traffic mailing lists](https://docs.peeringdb.com/#mailing-lists) or create an issue directly on [GitHub](https://github.com/peeringdb/peeringdb). If you find a data quality issue, please let us know at <support@peeringdb.com>.

***

PeeringDB is a freely available, user-maintained, database of networks, and the go-to location for interconnection data. The database facilitates the global interconnection of networks at Internet Exchange Points (IXPs), data centers, and other interconnection facilities, and is the first stop in making interconnection decisions.
