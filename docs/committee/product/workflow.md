## Workflow

[Diagram of Workflow](Product_Committee-Workflow.pdf)

The development roadmap is tracked using GitHub issues located at <https://github.com/peeringdb/peeringdb/issues> with the [ZenHub](https://www.zenhub.com/) overlay.

**New Issues** Are evaluated to confirm they are actually an issue, which may require asking for feedback. Issues where the solution is unclear or the bug cannot be reproduced are moved to **Review**. Once an issue is determined to be valid and coherent with the product vision, it is moved to **Backlog** and labeled as either bug or enhancement. Moving from New to **Backlog** does not need much discussion as it is easy to move the issue back or mark it as "wontfix" later.

Product Committee members look at the issues and move them **Review** for discussion if the issue seems legit. If it is reported as a bug, attempts are made to reproduce it, failing that, the issue is commented and the original submitter is asked for more information. The issue will then be kept under the category **Review**.

If the issue is considered not to be coherent with the product vision, it will be marked as "wontfix"; the requester always has the option to escalate his issue to the PeeringDB board if she disagrees with the assessment of the Product Committee.

Once Product Committee, with developer involvment, decides that no more information is needed to be able to fix/implement an issue, it can move to **PC Candidates**, with a rough estimate. **PC Candidates** should be ordered with more important higher in the list.

Depending on the effort required to implement the issue, development will be done either on project basis or as part of the maintenance agreement. The Product Committee follows a budget release process to fund project based development efforts. Developments that fall within the budget envelope allocated to the Product Committee require no further approval by the board, however 75% of the Product Committee members must agree. 

**Sprint** is the column that is next in the pipeline, encompassing everything that is approved to work on, so development starts immediately. This would be decided by the Product Committee.

All other PeeringDB projects also go through this issue board to decide on priority. For example, when something for peeringdb-py goes into a sprint, an issue will be made on the peeringdb-py project, and pulled it into that board.

**Done** means the issue is completed in development and will be pushed to beta for review. Issues are not **Closed** until they are deployed to production.