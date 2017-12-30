## Workflow

[Diagram of Workflow](Product_Committee-Workflow.pdf)

The development roadmap is tracked using GitHub issues located at <https://github.com/peeringdb/peeringdb/issues> with the [ZenHub](https://www.zenhub.com/) overlay.

**New Issues** are evaluated to confirm they are legitimate, which may require asking the reporter for feedback. Issues that cannot be reproduced or where the solution is unclear are moved to **Review**. Moving from **New Issues** to **Backlog** does not need much discussion as it is easy to move the issue back or mark it as `wontfix` later.

Once an issue is determined to be valid and coherent with the product vision, it is moved to **Backlog** and labeled as either bug or enhancement. If the issue is considered not to be coherent with the product vision, it will be marked as `wontfix`; the requester always has the option to forward his issue to the PeeringDB board if she disagrees with the assessment by the Product Committee.
If an issue is labeled as a bug, the severity will determine how it will be resolved. P1/P2 bugs are considered service impacting and will be treated by the software vendor under the maintenance agreement, P3/P4 bugs will be treated as product enhancement requests.

Once Product Committee, with developer involvement, decides that no more information is needed to be able to fix/implement an issue, it can move to **PC Candidates**, with a rough estimate. **PC Candidates** should be ordered with more important higher in the list.

Depending on the effort required to implement the issue, development will be done either on project basis or as part of the maintenance agreement. The Product Committee follows a budget release process to fund project based development efforts. Developments that fall within the budget envelope allocated to the Product Committee require no further approval by the board, however 75% of the Product Committee members must agree. 

**Sprint** is the column that is next in the pipeline, encompassing everything that is approved to work on, so development starts immediately. This would be decided by the Product Committee.

All other PeeringDB projects also go through this issue board to decide on priority. For example, when something for peeringdb-py goes into a sprint, an issue will be made on the peeringdb-py project and accessed by the main board.

**Done** means the issue is completed in development and will be pushed to beta for review. Issues are not **Closed** until they are deployed to production.