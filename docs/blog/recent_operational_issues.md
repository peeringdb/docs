# Recent Operational Issues

We had some operational issues following the production deployment of [2.76.0](/release_notes/#release-2760). We have a full [root cause analysis](/blog/rca-2.76/) available but we also want to provide a summary and confirm that the issues are resolved.

We completed our transition from VMs to Kubernetes with 2.76.0. As with any major infrastructure migration, we hit a few hiccups along the way — some interactions between the old storage layer and the new environment caused a brief service disruption. We've published a full root cause analysis for those interested in the technical details, but the short version is: we identified and resolved the issues quickly, and PeeringDB is running more reliably than ever on the new platform.

We also introduced rate limiting for unauthenticated web users in the same release. Automated scrapers started testing our new rate limiting shortly after release. We’ve refined the rate limiting and ensured that web browsers can cache more web page elements, reducing the scope of their requests.

We’ve now resolved the main issues and PeeringDB is running normally for web and API users. 

If you have an idea to improve PeeringDB you can share it on our low traffic [mailing lists](https://docs.peeringdb.com/#mailing-lists) or create an issue directly on [GitHub](https://github.com/peeringdb/peeringdb/issues). If you find a data quality issue, please let us know at [support@peeringdb.com](mailto:support@peeringdb.com).

--- 

PeeringDB is a freely available, user-maintained, database of networks, and the go-to location for interconnection data. The database facilitates the global interconnection of networks at Internet Exchange Points (IXPs), data centers, and other interconnection facilities, and is the first stop in making interconnection decisions.
 
