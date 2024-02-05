# What happened to our web UI?
We released 2.54.0 to production on 24 January 2024. PeeringDB users quickly made us aware of issues with the release.

The problems centered on the impact of web UI changes on search:

* Users needed to click on the magnifying glass icon to open the search bar
* Some in page searches resulted in a CSRF error
* Other search attempts did not work

We focused on four issues describing problems and developed fixes that addressed them in development and then beta environments. Ultimately, we decided that it was better to rollback the UI changes, so that’s what we did.

2.54.2 is now in production. It has all the features from 2.54.0 except the web UI changes.

## Why did it happen?
Our own internal testing missed the impact of these changes. We thought they were relatively small and planned to make an incremental improvement before introducing our updated design on  preview.peeringdb.com.

That was a mistake.

Also, we’ve had a remarkably good run of stable releases. We think this has contributed to a drop in testing on beta.peeringdb.com. Only about 0.25 percent of users visited beta.peeringdb.com in January 2024.

## How will we improve?
We will be changing our process for introducing big changes.

The first part is to improve our internal testing process.

But we are also considering changes to the beta testing process. Instead of relying on users to speak up if they find a problem on beta.peeringdb.com we could do the reverse. We would only release major changes to production after we have had positive comments from users who have tested on beta.peeringdb.com. 

In some cases, we might need to delay a release – or part of it – until we had that positive input from users.

What do you think? Would you prefer us to require more active involvement from users in beta testing? Let us know on our [user-discuss mailing list](https://lists.peeringdb.com/cgi-bin/mailman/listinfo/user-discuss), through our social media channels, or speak with our volunteers to share your thoughts.

If you have an idea to improve PeeringDB you can share it on our [low traffic mailing lists](https://docs.peeringdb.com/#mailing-lists) or create an issue directly on [GitHub](https://github.com/peeringdb/peeringdb/issues/). If you find a data quality issue, please let us know at [support@peeringdb.com](mailto:support@peeringdb.com).

--- 

PeeringDB is a freely available, user-maintained, database of networks, and the go-to location for interconnection data. The database facilitates the global interconnection of networks at Internet Exchange Points (IXPs), data centers, and other interconnection facilities, and is the first stop in making interconnection decisions.

