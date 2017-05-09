## Workflow

[Diagram of Workflow](Product_Committee-Workflow.pdf)

The development roadmap is tracked using GitHub issues located at <https://github.com/peeringdb/peeringdb/issues> with the [ZenHub](https://www.zenhub.com/) overlay.

**New Issues** Are evaluated to confirm they are actually an issue, which may require asking for feedback. Once an issue is determined to be valid, it is moved to **Icebox** and labeled either bug or enhancement. Moving from New to **Icebox** does not need much discussion as it is easy to move the issue back or mark it as "wontfix" later. 

Product Committee members look at the issues and move them **Icebox** for discussion if the issue seems legit. If it is reported as a bug, attempts are made to reproduce it, failing that, the issue is commented and the original submitter is asked for more information. The issue will then be kept under the category **New Issues**.

Once Product Committee, with developer involvment, decides that no more information is needed to be able to fix/implement an issue, it can move to **Backlog**, with a rough estimate. **Backlog** should be ordered with more important higher in the list.

**Sprint** is the column that is next in the pipeline, encompassing everything that is approved to work on, so development starts immediately. This would be decided by the Product Committee.

All other PeeringDB projects also go through this issue board to decide on priority. For example, when something for peeringdb-py goes into a sprint, an issue will be made on the peeringdb-py project, and pulled it into that board.

**Done** means the issue is completed in development and will be pushed to beta for review. Issues are not **Closed** until they are deployed to production.