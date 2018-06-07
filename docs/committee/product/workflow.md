## Workflow

[Diagram of Workflow](Product_Committee-Workflow.pdf)

The development roadmap is tracked using GitHub issues located at <https://github.com/peeringdb/peeringdb/issues> with the [ZenHub](https://www.zenhub.com/) overlay.

All members of the Product Committee take part in a _Hot Seat_ schedule with a weekly rotation in order to monitor incoming github issues and ensure the follow-up of existing issues until they are either closed as non-implemented or moved to the backlog. 

**New Issues** are evaluated to confirm they are legitimate, which may require asking the reporter for feedback. Issues that cannot be reproduced or where the solution is unclear are moved to **Review**. Moving from **New Issues** to **Backlog** does not need much discussion as it is easy to move the issue back or mark it as `wontfix` later.

Once an issue is determined to be valid and coherent with the product vision, it is moved to **Backlog** and labeled as either bug or enhancement. If the issue is considered not to be coherent with the product vision, it will be marked as `wontfix`; the requester always has the option to forward his issue to the PeeringDB board if she disagrees with the assessment by the Product Committee.
If an issue is labeled as a bug, the severity will determine how it will be resolved. P1/P2 bugs are considered service impacting and will be treated by the software vendor under the maintenance agreement, P3/P4 bugs will be treated as product enhancement requests.

Every member of the Product Committee may label one issue a month as **PC Candidate**. An issues labeled as **PC Candidate** must have a solution for development fully specified within the Github issue before it can be considered for implementation. Once it is agreed with the developer that no more information is needed to be able to fix/implement an issue, it can be proposed for inclusion in the next sprint to the Product Committee mailing-list. The Product Committee (Vice) Chair will move the agreed upon issues to the **Sprint** column.

Depending on the effort required to implement the issue, development will be done either on project basis or as part of the maintenance agreement. The Product Committee follows a budget release process to fund project based development efforts. Developments that fall within the budget envelope allocated to the Product Committee require no further approval by the board, however 75% of the Product Committee members must agree. 

**Sprint** is the column that is next in the pipeline, encompassing everything that is approved to work on, so development starts immediately. This would be decided by the Product Committee.

All other PeeringDB projects also go through this issue board to decide on priority. For example, when something for peeringdb-py goes into a sprint, an issue will be made on the peeringdb-py project and accessed by the main board.

**Done** means the issue is completed in development and will be pushed to beta for review. Issues are not **Closed** until they are deployed to production.