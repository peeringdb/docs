
# PeeringDB Committees


## Admin Committee


## Product Committee

### Charter

*** DRAFT ***

#### Scope

The PeeringDB Product Committee (PC) is charged with steering the future product development and running the market outreach efforts to continuously improve the value that PeeringDB delivers to the networks registered with PeeringDB, and the broader community.

##### Out of Scope

- The PC does not drive PeeringDB improvements related to the administrative interfaces & functions used by the PeeringDB Admin Committee.
- The PC does not consider PeeringDB improvements related to the server, storage, hosting or network infrastructure.


#### Deliverables

- Gather inputs from stakeholders regarding the evolution of PeeringDB in terms of product features and overall long term objectives.
- Formulate the long term objectives and validate them with the PeeringDB Board and the members of the PeeringDB Governance mailing list.
- Process documentation detailing the treatment of product enhancement requests submitted to the PC.
- Maintain the product roadmap and feature request backlog and makes them publically accessible. 
- Create and maintain PeeringDB product documentation and presentation materials.
- Develop market outreach and evangelisation to increase the uptake of PeeringDB use and improve data quality.
- Propose new features or enhancements based on the long term objectives and validates significant product evolutions with key stakeholders.


#### Collaboration

The PC shall work with other PeeringDB committees to ensure an equitable division of development resources in recognition of the volunteer efforts that are ensuring the daily operations.


#### Participation

The PeeringDB Product Committee members serve a 1 year renewable term. Volunteers can submit their candidacy to the PeeringDB Board. The Board will elect a new Product Committee after the Board election or at any time the Board sees the necessity to ensure the continuity of the Product Committee


#### Communication

- Questions and suggestions for the Product Committee can be sent to <productcom@lists.peeringdb.com>
- Key development communication and community input gathering efforts will be conducted via the PeeringDB Governance Mailinglist [pdb-gov@lists.peeringdb.com](http://lists.peeringdb.com/cgi-bin/mailman/listinfo/pdb-gov)
- All issues and the product roadmap and feature backlog can be found at <https://github.com/peeringdb/peeringdb/issues>


#### Decision Policy

Product Committee members will decide by simple majority vote on contested issues called by the Product Committee Chair


### Workflow

We use GitHub issues located at <https://github.com/peeringdb/peeringdb/issues> with the [ZenHub](https://www.zenhub.com/) overlay.

**New Issues** Evaluate if it's actually an issue, ask for feedback, etc, once it is determined valid, move it to **Icebox** and label it either bug or enhancement. Moving from New to **Icebox** probably doesn't need much discussion, it's quite easy to move back or mark as "wontfix" later. If anyone looks at an issue and it seems legit, move to **Icebox** for discussion. If it's a bug, try to reproduce it, if you can't, comment and ask for more information and leave in new.

Once, with a developer involved, it's decided no more information is needed to be able to fix/implement it, it can move to **Backlog**, with a rough estimate. **Backlog** should be ordered with more important higher in the list.

**Sprint** is the column that's next in the pipeline, which is everything that is approved to work on, so development starts immediately. This would be decided by the Product Committee.

All other PeeringDB projects should go through this issue board since we have to decide priority. For example, when something for peeringdb-py goes into a sprint, we'll make an issue on the peeringdb-py project, and pull it into that board.

**Done** means completed in development, and will be pushed to beta for review. Issues are not **Closed** until they're deployed to production.

